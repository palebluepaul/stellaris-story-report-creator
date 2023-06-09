import openai
import logging

class Agent:
    def __init__(self, agent_config, mode, api_key, logger):
        self.agent_config = agent_config
        self.mode = mode
        self.api_key = api_key
        self.logger = logger
        self.temperature = agent_config['temperature'] if 'temperature' in agent_config else 0.7
        self.max_tokens = agent_config['max_tokens'] if 'max_tokens' in agent_config else 500


    def call_agent(self, content):
        # Generate the message to the chat model
        message = {
            'role': 'system',
            'content': self.agent_config['system']
        }
        message2 = {
            'role': 'user',
            'content': self.agent_config[self.mode] + content
        }

        self.logger.info(f"Prompt to OpenAI API: {message['content']} {message2['content']}")

        # Call OpenAI's GPT-4 chat completion API
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[message, message2],
          max_tokens=self.max_tokens,
          temperature=self.temperature
        )

        output = response['choices'][0]['message']['content']
        self.logger.info(f"Response from OpenAI API: {output}")

        # Return the response
        return output
