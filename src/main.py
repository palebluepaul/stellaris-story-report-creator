import os
import sys
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from agent import Agent

def main(mode, input_file):
    # Load API key from environment
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # Create a logger
    logger = logging.getLogger(__name__)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    logging.basicConfig(filename=f'logs/{timestamp}.log', level=logging.INFO)

    # Read the agent configuration
    with open('config/agent_config.json', 'r') as f:
        agent_config = json.load(f)

    # Read the input file
    with open(input_file, 'r') as f:
        request = f.read()

    # Call the novelist agent
    novelist = Agent(agent_config['novelist'], mode, openai_api_key, logger)
    novelist_output = novelist.call_agent(request)

    # Call the editor agent
    editor = Agent(agent_config['editor'], mode, openai_api_key, logger)
    editor_feedback = editor.call_agent(novelist_output)

    # Call the novelist agent again with the editor's feedback
    revised_output = novelist.call_agent(editor_feedback)

    # Write the revised output to a file in the output directory
    output_file = os.path.join('output', f'{os.path.splitext(os.path.basename(input_file))[0]}_{timestamp}_output.txt')
    with open(output_file, 'w') as f:
        f.write(revised_output)

    logger.info(f'Successfully wrote output to {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python main.py <mode> <input_file>')
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]

    main(mode, input_file)
