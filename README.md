# Personal Finance AI

Personal Finance AI is an intelligent financial planning assistant powered by AI agents. It provides personalized financial advice by analyzing various aspects of your financial situation, including budgeting, investments, and risk management.

## Features

- Interactive chat interface using Streamlit
- Leverages OpenAI's swarm framework. 
- Specialized AI agents for different financial domains:
  - Financial Planning Orchestrator
  - Risk Management
  - Investment Strategy
  - Budget Analysis

## Prerequisites

- Python 3.11
- Poetry (for dependency management)

## Installation

1. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

1. Activate the Poetry environment:
   ```
   poetry shell
   ```

2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Enter your OpenAI API key in the sidebar.

5. Start chatting with the AI to get personalized financial advice!

## Project Structure

- `main.py`: The main Streamlit application file
- `agents.py`: Defines the specialized AI agents
- `utils.py`: Utility functions for message formatting
- `pyproject.toml`: Project dependencies and configuration managed by Poetry

## Configuration

The application requires an OpenAI API key to function. You can enter this key in the sidebar of the Streamlit app.
