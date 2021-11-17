import os
import time
import re
from slackeventsapi import SlackEventAdapter
from threading import Thread
from slack_sdk import WebClient
from flask import Flask, Response,request
from dotenv import load_dotenv
from DiceRoller import DiceRoller
from CommandParser import CommandParser
import json
import requests
from playerDetails.Player import Player



# instantiate Slack client
load_dotenv()
global players 
players = []
url = 'https://slackevent.herokuapp.com/'
App=Flask(__name__)

#SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
#slack_token = os.environ['SLACK_BOT_TOKEN']
#VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
slack_token = os.getenv('SLACK_BOT_TOKEN')
VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN')
slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, '/slack/events',App)  


SlackWeb = WebClient(slack_token)

@App.route('/slack/events', methods=['POST'])
def event_hook():
    
    json_dict = request.get_json()
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return


@App.route('/', methods=['POST'])
def event_hook_if_starting_base():
    
    json_dict = request.get_json()
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return

@App.route('/PostChar', methods=['POST'])
def PostCharStats():
    val =400
    try:
        json_dict = request.get_json()
        try:
            is_dm = json_dict["type"]
            val= 401
            User = json_dict["User"]
        except:
            return {"status": val}
        try:
            val = 402
            player = Player(is_dm,User)
            val = 403
            players.append(player.user)
        except:
            return {"status": val}
        return {"status": 200}
    except:
        return{"status": 400}

@App.route('/PrintPlayers',methods = ['GET'])
def PrintPlayer():
    val = " "
    for i in players:
        val = val +" " +i
        print(val)
    return f"<h1>{val}</h1>"
        




@slack_events_adapter.on("app_mention")
def handle_mentions(event_data):
    #Parse thought the line to determine what the bot has to do 
    event = event_data["event"]
    if('!' in event['text']):
        command = event['text'].split('!')[1]
        resultval = CommandParser.parse(command)
        SlackWeb.chat_postMessage(
        channel=event["channel"],
        text=f"Results: {resultval}",
        )
    else:
        SlackWeb.chat_postMessage(
        channel=event["channel"],
        text=f"You did not enter a correct command type !H to get commands",
        )





@App.route('/')
def index():
    #SlackWeb.chat_postMessage(channel='#random', text='message')
    return "<h1>Welcome to our server !!</h1>"

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    print("reaches here")
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "!insert Player" in message.get('text'):
        mes = message.get('text').split(" ")
        if(mes.size>3):
            isDm = False
            if(mes[2].upper() == "TRUE"):
                isDm = True
            data = {"type"}
            res =requests.post(url+'PostChar', json= {"type":isDm,"User":mes[3]})
            SlackWeb.chat_postMessage(
        channel=event_data["channel"],
        text=res.status_code,
        )
        else:
            SlackWeb.chat_postMessage(
        channel=event_data["channel"],
        text=f"You did not enter a correct command type !H to get commands",
        )


if __name__ == "__main__":
    #SlackWeb.chat_postMessage(channel='#random', text='message')
    App.run(port=3000)
    

    