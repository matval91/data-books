from transformers import TransformersClient
import os
client = TransformersClient(os.environ['HF_API_TOKEN'])

# Define the chat ID and message text
chat_id = 'test_mv'
message = {'text': 'Hello, world!'}

# Send the message to the chat
response = client.send_message(chat_id, message)

# Print the response
print(response)