import random

#how to run 


#features to add 
#if the user gives dice side of not 20,12,10,8,6,4 return error 

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


    
    def GetRoll(self,command):
        #the format of this command should be !(numberofRoles)D(number of sides on dice)A(advnatage or disadvantage or neutral)S(Skills)
        #first i want to get rid fo the explanation point
        usableCommand = command.split('!')[1]
        NumOfRoles = 1
        print(usableCommand)
        #determine how many roles will happen
        if(len(usableCommand.split('D')[0])>0):
            NumOfRoles= usableCommand.split('D')[0]
        usableCommand = usableCommand.split('D')[1]
        #obtain the type of dice used 
        DiceSides = usableCommand.split('A')[0]

        #remove old data
        usableCommand = usableCommand.split('A')[1]

        #get the advantage variable 
        #D = disadvantage
        #N = neutral
        #A = advantage
        advOrDis = usableCommand.split('S')[0]
        #I have to figure out what the advantage and disadvantage does to the 

        Skill = int(usableCommand.split('S')[1])
        

        total = 0
        print(DiceSides)
        for i in range(0,int(NumOfRoles)):
            total = total+ (self.whichRoll(self,int(DiceSides))+Skill)
        print(total)
            
    
    
    

DiceRoller.GetRoll(DiceRoller,'!2D20A1S+2')