import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule

# SLACK_API_TOKEN = '<is in .env locally>'

import boto3

ssm = boto3.client('ssm', region_name='eu-north-1')
response = ssm.get_parameter(Name='ihor-slack-bot-notification-token', WithDecryption=True)
SLACK_API_TOKEN = response['Parameter']['Value']
# print('SLACK_API_TOKEN===', SLACK_API_TOKEN)

# Set the Slack API token
# client = WebClient(token=os.environ['SLACK_API_TOKEN'])
client = WebClient(token=SLACK_API_TOKEN)

# Set the channel ID or name
channel_id = 'slack-bot'

# Set the message text
user_id = 'U04AGMSV29L'
message_text = f'do not lose your life... https://www.youtube.com/shorts/Oy9kDTuHjKQ, https://www.youtube.com/watch?v=u_ktRTWMX3M&ab_channel=MulliganBrothers, <@{user_id}>'
# message_text = 'Hello, world test Ihor ed !'

# while True:
#     try:
#         # Call the chat.postMessage API method with the channel ID and message text
#         response = client.chat_postMessage(
#             channel=channel_id,
#             text=message_text
#         )
#         print('Message sent: ', response['ts'])
#     except SlackApiError as e:
#         print('Error sending message: ', e)
#
#     # Wait for 1 minute
#     time.sleep(5)

print('app started! working...')
def send_message():
    try:
        # Call the chat.postMessage API method with the channel ID and message text
        response = client.chat_postMessage(
            channel=channel_id,
            text=message_text
        )
        print('Message sent: ', response['ts'])
    except SlackApiError as e:
        print('Error sending message: ', e)

# Schedule the send_message function to run every day at 9am
schedule.every().day.at("09:25").do(send_message)

# Loop forever, checking if the scheduled function should be run
while True:
    schedule.run_pending()
    time.sleep(50)
