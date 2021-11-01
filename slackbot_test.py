from slackbot import SlackBot
import requests

# This is the webhook that allows us to post to #general in SER300 Slack
URL = "https://hooks.slack.com/services/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"

# Initialize the slackbot. This is the object that we will be able to use to process the requests and get the responses
sb = SlackBot() 

# Roll a d20
message = sb.get_roll20_message()
# Post to the URL which in turn sends a message to #general in SER300 Slack
print(requests.post(URL, json={'text':message}))