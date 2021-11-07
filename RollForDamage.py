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
    def pickDiceRoller(self,numOfSides):
        switcher= {
            20:lambda: self.roll20(),
            12:lambda: self.roll12(),
            10:lambda: self.roll10(),
            8:lambda: self.roll8(),
            6:lambda: self.roll6(),
            4:lambda: self.roll4(),
        }
        
        val = switcher.get(numOfSides, "Invalid entry")()
        print(val)
        return val

    def processCommand(self, command):
        #the format of this command should be !M (numberofRoles)D(number of sides on dice)
        # Removes ! from command and splits at [space-separated] parameters
        usableCommand = command.split('!')[1].split(' ',1)[1]

        print("COMMAND:", usableCommand)

        try:
            diceRoll = usableCommand.split('D')

            #determine how many roles will happen
            numOfRoles= diceRoll[0].split(' ')[1]
            print("# ROLLS:", numOfRoles)

            #obtain the type of dice used
            diceSides = diceRoll[1]
            print("DICE SIDES:", diceSides)

            sum = 0
            for i in range(0,int(numOfRoles)):
                    print('Is running')
                    print(int(diceSides))
                    sum += (self.pickDiceRoller(int(diceSides)))
            return sum
        except:
            return "Invalid entry"