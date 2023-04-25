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


# Define a function to print 'sport'
def print_do_sport():
    print(f'do sport 15 mins! <@{user_id}>, for own better health, look and social life')


def print_do_courses():
    print(f'watch courses 20-30 mins! <@{user_id}>, for self-development and pass the table of Progress...BASICS...architecture')


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
schedule.every().day.at("06:25").do(send_message)

# Schedule the print_do_sport function to run every day at 10am
schedule.every().day.at("06:55").do(print_do_sport)

# Schedule the print_do_cources function to run every day at 5:30pm
schedule.every().day.at("14:30").do(print_do_courses)

# Loop forever, checking if the scheduled function should be run
while True:
    schedule.run_pending()
    time.sleep(50)
