# Text To SQL With LlamaIndex Workflow

This project provides a system that analyzes natural language queries and converts them into SQL queries while performing security checks. It uses a Large Language Model (LLM) to determine user intent and assess the safety of SQL queries. Additionally, it presents query results and performance metrics to the user.

## Features

- **Intent Analysis**: Analyzes natural language queries from users to determine SQL or chat intent.
- **SQL Generation**: Converts natural language queries into secure SQL queries.
- **Security Checks**: Evaluates SQL queries and user prompts for security.
- **Result Formatting**: Presents query results and performance metrics to the user.
- **Error and Security Breach Logging**: Logs errors and security breaches.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ardasamett/Text2SQL_Agent-llamaindex.git
   cd Text2SQL_Agent-llamaindex
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the database:
   ```bash
   python create_sqllite.py
   ```

4. Start using the agent with main.ipynb  

## Usage

- Use the `run_sql_agent(natural_query: str)` function to provide a natural language query and perform SQL analysis.
- Use the `PrintManager` class to view outputs in a formatted and colorized manner.

## Contributing

If you would like to contribute, please submit a pull request or open an issue.
