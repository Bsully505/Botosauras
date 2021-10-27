import random

class DiceRoller:
   
    def roll20():
        return round((random.random()*19)+1)

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

    #the reason for only allowing these numbers is due to the boardgame in which the players only have dice of 20,12,10,8,6,4
    def whichRoll(self,num):
        if(num>13):
            return self.roll20()
        if(num>11):
            return self.roll12()
        if(num>9):
            return self.roll10()
        if(num>7):
            return self.roll8()
        if(num>5):
            return self.roll6()
        if(num>3):
            return self.roll4()
        return 0


    def processCommand(self, command):
        #the format of this command should be !(numberofRoles)D(number of sides on dice)A(advnatage or disadvantage or neutral)S(Skills)
        # Removes ! from command and splits at [space-separated] parameters
        usableCommand = command.split('!')[1].split(' ')
        
        print("COMMAND:", usableCommand)

        diceRoll = usableCommand[0].split('D')

        #determine how many roles will happen
        numOfRoles= diceRoll[0]
        print("# ROLLS:", numOfRoles)
        
        #obtain the type of dice used 
        diceSides = diceRoll[1]
        print("DICE SIDES:", diceSides)


        #get the advantage variable 
        #D = disadvantage
        #N = neutral
        #A = advantage


        advOrDis = usableCommand[2]

        skill = int(usableCommand[1])

        return (numOfRoles, advOrDis, diceSides, skill)

    
    def getRoll(self,command):
        (numOfRoles, advOrDis, diceSides, skill) = self.processCommand(self, command)

        total = 0
        # Roll the dice the specified number of times and add the results to the total
        for i in range(0,int(numOfRoles)):
            # If advantage, roll the die twice and take the higher result
            if (advOrDis == 'A'):
                total = total +  max(self.whichRoll(self,int(diceSides)),self.whichRoll(self,int(diceSides))) + skill
            elif (advOrDis == 'D'):
                total = total +  min(self.whichRoll(self,int(diceSides)),self.whichRoll(self,int(diceSides))) + skill
            else:
                total = total + (self.whichRoll(self,int(diceSides))+skill)

        return total


            
    
    
    


if (__name__ == "__main__"):
    #+2 will be replaced with a skill that will then be used to calculate the bonus to be added
    DiceRoller.getRoll(DiceRoller,'!1D20 +2 A')

