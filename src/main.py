import os
import sys
import json
import openai
from dotenv import load_dotenv

def main(mode, input_file):
    # Load API key from environment
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Read the agent configuration
    with open('config/agent_config.json', 'r') as f:
        agent_config = json.load(f)['novelist']

    # Read the input file
    with open(input_file, 'r') as f:
        request = f.read()

    # Generate the message to the chat model
    message = {
        'role': 'system',
        'content': agent_config['system']
    }
    message2 = {
        'role': 'user',
        'content': agent_config[mode] + request
    }

    # Call OpenAI's GPT-4 chat completion API
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[message, message2]
    )

    # Use the response as the output
    output = response['choices'][0]['message']['content']

    # Write the output to a file in the output directory
    output_file = os.path.join('output', f'{os.path.splitext(os.path.basename(input_file))[0]}_output.txt')
    with open(output_file, 'w') as f:
        f.write(output)

    print(f'Successfully wrote output to {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python main.py <mode> <input_file>')
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]

    main(mode, input_file)
