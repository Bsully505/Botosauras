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
from ListOfPlayers import Players



# instantiate Slack client
load_dotenv()

PlayerList = Players()
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

    json_dict = request.get_json()
    is_dm = json_dict["type"]
    User = json_dict["User"]
    player = Player(is_dm,User)
    PlayerList.addPlayer(player)


    return {"Players": PlayerList.ReturnPlayers()}


@App.route('/PrintPlayers',methods = ['GET'])
def PrintPlayer():
    val = " "
    for i in Players.ReturnPlayers():
        val = val +" and " +i
        print(val)
        
    return f"<h1> This should be all of your Players {val}</h1>"
        




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



if __name__ == "__main__":
    #SlackWeb.chat_postMessage(channel='#random', text='message')
    App.run(port=3000)
    

    