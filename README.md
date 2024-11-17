
# Algebraic Math Tutor Assistant

## Overview
The **Algebraic Math Tutor Assistant** is an interactive chatbot built using **Chainlit**, **LangChain**, and **OpenAI GPT-3.5**. It is designed to solve algebraic math problems, providing detailed step-by-step solutions. The assistant also evaluates its performance on a dataset of algebra problems to measure accuracy.

This tool is perfect for students, educators, or anyone looking to better understand algebraic concepts through automated problem-solving and explanations.

## Prerequisites
1. **OpenAI API Key**: You need a valid API key from OpenAI.
2. **Python Environment**: Ensure Python 3.8 or higher is installed.
3. **Chainlit Account**: You need a Chainlit account to run the application.

### Step 1: Set Up a Virtual Environment

#### For Windows
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

#### For Ubuntu
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Step 2: Install Dependencies
Install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Environment
1. Create a `.env` file in the root directory and set your OpenAI API key, if you don't get it please open the `sample.env.txt` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

### Step 4: Run the Chatbot

To run the chatbot and start interacting with the Algebraic Math Tutor Assistant, execute the following command:
```bash
chainlit run chatbot.py
```

This will start the Chainlit application, and you can begin chatting with the assistant.

### Step 5: Interact with the Chatbot
1. Send algebraic math questions to the chatbot.
2. The assistant will respond with a step-by-step breakdown of the solution.

### Step 6: Evaluate the Chatbot Performance
The assistant can be evaluated on a dataset of algebraic problems. This is useful to check the accuracy of the solutions the assistant generates.

1. The `evaluate_chatbot_on_dataset` function loads a JSON dataset containing algebraic problems and checks if the assistant's responses match the expected answers.
2. You can use a dataset file named `data.json` to test the chatbot.

## Example Usage
1. **Input**: `Solve for x: 2x + 3 = 7`