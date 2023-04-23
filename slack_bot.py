import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_API_TOKEN = 'xoxb-4348796765079-5117507520707-Cj7EhYhqv5SxNke3EfExYaHw'

# Set the Slack API token
# client = WebClient(token=os.environ['SLACK_API_TOKEN'])
client = WebClient(token=SLACK_API_TOKEN)

# Set the channel ID or name
channel_id = 'slack-bot'

# Set the message text
user_id = 'U04AGMSV29L'
message_text = f'Hello, world test Ihor <@{user_id}>!'
# message_text = 'Hello, world test Ihor ed !'

while True:
    try:
        # Call the chat.postMessage API method with the channel ID and message text
        response = client.chat_postMessage(
            channel=channel_id,
            text=message_text
        )
        print('Message sent: ', response['ts'])
    except SlackApiError as e:
        print('Error sending message: ', e)

    # Wait for 1 minute
    time.sleep(5)
