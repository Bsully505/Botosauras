import random

class RollForDamage:

    #range of 1-20
    def roll20():
        return round((random.random()*19)+1)
    #range of 1-12
    def roll12():
        return round((random.random()*11)+1)
    #range of 1-10
    def roll10():
        return round((random.random()*9)+1)
    #range of 1-8
    def roll8():
        return round((random.random()*7)+1)
    #range of 1-6 aka regular die
    def roll6():
        return round((random.random()*5)+1)
    #range of 1-4
    def roll4():
        return round((random.random()*3)+1)

    #checking cases to roll the dice with the corresponing number of sides
    def pickDiceRoller(numOfSides):
        switcher{
            20: roll20(),
            12: roll12(),
            10: roll10(),
            8: roll8(),
            6: roll6(),
            4: roll4(),
        }
        return switcher.get(numOfSides, "Invalid entry")

    def processCommand(self, command):
        #the format of this command should be !M (numberofRoles)D(number of sides on dice)
        # Removes ! from command and splits at [space-separated] parameters
        usableCommand = command.split('!')[1].split(' ')

        print("COMMAND:", usableCommand)

        if usableCommand[0] == 'M':
            diceRoll = usableCommand[1].split('D')

            #determine how many roles will happen
            numOfRoles= diceRoll[0]
            print("# ROLLS:", numOfRoles)

            #obtain the type of dice used
            diceSides = diceRoll[1]
            print("DICE SIDES:", diceSides)

            sum = 0
            for i in range(numOfRoles):
 	              sum += pickDiceRoller(diceSides)

            return sum

        else
            return "Invalid entry"
