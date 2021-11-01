from DiceRoller import DiceRoller

# Used to organize different messages that will be sent from the slackBot


class SlackBot:

    #Roll a d20 using the diceroller and compose the message to be sent
    def get_roll20_message(self):
        return "Rolling a D20... " + str(DiceRoller.roll20())
