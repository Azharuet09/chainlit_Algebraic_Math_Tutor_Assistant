import chainlit as cl
import json
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv

load_dotenv()

def load_algebra_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

@cl.on_chat_start
def algebra_math_chatbot():
    llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0)

    algebra_problem_template = """You are a specialized Algebraic Math Tutor Assistant. Your task is to solve math problems, 
    particularly algebraic equations, and provide detailed solutions. 
    Steps:
    - Break down the problem logically.
    - Show detailed calculations step-by-step.
    - Provide the final solution clearly.

    Do NOT answer questions unrelated to algebra or math. Instead, respond with: 
    'I can only assist with algebraic math problems. Please ask a math-related question.'

    Question: {question} 
    Answer:"""

    algebra_assistant_prompt = PromptTemplate(
        input_variables=["question"],
        template=algebra_problem_template
    )

    algebra_problem_chain = LLMChain(llm=llm, prompt=algebra_assistant_prompt)

    algebra_tool = Tool.from_function(
        name="Algebra Solver",
        func=algebra_problem_chain.run,
        description="Useful for solving algebraic and general math questions."
    )
    agent = initialize_agent(
        tools=[algebra_tool], 
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )
    cl.user_session.set("agent", agent)


@cl.on_message
async def process_user_query(message: cl.Message):
    agent = cl.user_session.get("agent")
    response = await agent.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(response["output"]).send()


def evaluate_chatbot_on_dataset(filepath):
    algebra_data = load_algebra_data(filepath)

    algebra_math_chatbot()
    agent = cl.user_session.get("agent")

    correct = 0
    for problem in algebra_data:
        question = problem["question"]
        expected = problem["expected"]
        response = agent.run(question)
        if response.strip() == expected:
            correct += 1
        print(f"Q: {question}")
        print(f"Expected: {expected}, Got: {response.strip()}\n")

    accuracy = (correct / len(algebra_data)) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    evaluate_chatbot_on_dataset("data.json")
