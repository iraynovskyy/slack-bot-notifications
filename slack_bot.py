import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
from datetime import datetime
from pytz import timezone

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
message_motivation = f'do not lose your life... https://www.youtube.com/shorts/Oy9kDTuHjKQ, https://www.youtube.com/watch?v=u_ktRTWMX3M&ab_channel=MulliganBrothers, <@{user_id}>'
message_sport = f'do sport 15 mins! <@{user_id}>, for own better health, look and social life'
message_courses = f'watch courses 20-30 mins! <@{user_id}>, for self-development and pass the table of Progress...BASICS...architecture'


# Get the current time in the Europe/Kyiv time zone
kyiv_timezone = timezone('Europe/Kyiv')
current_time = datetime.now(kyiv_timezone)
current_time_custom = current_time.strftime('%H:%M:%S / Kyiv zone')  # ('%Y-%m-%d %H:%M:%S %Z%z')
print(f'The app has started working at {current_time_custom}...')


def send_message(msg):
    try:
        # Call the chat.postMessage API method with the channel ID and message text
        response = client.chat_postMessage(
            channel=channel_id,
            text=msg
        )
        print('Message sent: ', response['ts'])
    except SlackApiError as e:
        print('Error sending message: ', e)


# send starting message
send_message('The app has started working! Have a Great Day!')

# # Schedule the send_message function to Motivate every day at 9:30am
schedule.every().day.at("09:30", "Europe/Kyiv").do(
    lambda: send_message(message_motivation))  # todo add logic to motivate again at 23:00

# Schedule the print_do_sport function to Motivate every day at 11pm
schedule.every().day.at("23:00", "Europe/Kyiv").do(
    lambda: send_message(message_motivation))  # todo add some logic to press OK not OK...gather statisctics?!

# # Schedule the print_do_sport function for Sport every day at 10am
schedule.every().day.at("09:45", "Europe/Kyiv").do(
    lambda: send_message(message_sport))

# # Schedule the print_do_cources function for Self-Development run every day at 5:30pm
schedule.every().day.at("14:30", "Europe/Kyiv").do(
    lambda: send_message(message_courses))

# Loop forever, checking if the scheduled function should be run
while True:
    schedule.run_pending()
    time.sleep(1)
