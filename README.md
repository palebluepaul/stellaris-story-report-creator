
# Stellaris Story and Report Generator

This Python program uses the OpenAI GPT-4 model to generate stories and reports based on a race from the game Stellaris. It has two modes - `story` and `report`, and uses different agents (characters with specific roles) for content generation.

## Project Structure

- `main.py`: The main script that drives the whole project.
- `agent.py`: Contains the Agent class that interacts with the OpenAI API.
- `agent_config.json`: Configuration for the different agents.
- `input`: Directory to put your input text files.
- `output`: Directory where the program will write the generated stories or reports.
- `logs`: Directory where the program will write the logs.

## How to Use

1. First, ensure you have Python 3.7 or later installed.
2. Install the required Python packages with `pip install -r requirements.txt`.
3. Set your OpenAI API key in your environment variables.
4. Write your request in a text file and save it in the `input` directory.
5. Run the script with `python main.py [mode] [input_file]` where `[mode]` is either `story` or `report`, and `[input_file]` is the path to your input text file.

The generated story or report will be written to a new text file in the `output` directory. The program also creates a log file for each run in the `logs` directory.

## Configuration

You can configure the different agents used by the program by editing the `agent_config.json` file. Each agent has a `system` prompt, and a `story` and `report` prompt. The `system` prompt describes the role of the agent, and the `story` and `report` prompts are used to instruct the agent to write a story or a report. Each agent can also have a `max_tokens` and a `temperature` parameter that controls the length and randomness of the generated text, respectively.
