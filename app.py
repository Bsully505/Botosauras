import os
import time
import re
from slackeventsapi import SlackEventAdapter
from threading import Thread
from slack_sdk import WebClient
from flask import Flask, Response,request
from dotenv import load_dotenv
import json



# instantiate Slack client
load_dotenv()

App=Flask(__name__)
greetings= {'hi','hello','hope you have a good day'}

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
slack_token = os.environ['SLACK_BOT_TOKEN']
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

#SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
#slack_token = os.getenv('SLACK_BOT_TOKEN')
#VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN')


SlackWeb = WebClient(slack_token)



@App.route('/', methods=['POST'])
def event_hook():
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return

slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, endpoint= "/slack/events"
)  

@slack_events_adapter.on('app_mention')
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            if any(item in command.lower() for item in greetings):
                message = (
                    "Hello <@%s>! :tada:"
                    % message["user"]  # noqa
                )
                SlackWeb.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)



@App.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"




if __name__ == "__main__":
    SlackWeb.chat_postMessage(channel='#random', text='message')
    App.run(port=3000)
    

    