import requests 
from InterfaceCharacter import Character
import json
import random
 
class AddPlayer:
    url = 'https://slackevent.herokuapp.com/'
    def AddPlayer(self,is_DM,User):
        #try:
            self.AddPlayerNew(self,User)
            #res =requests.post(self.url+'PostChar', json= {"type":is_DM,"User":User})
            return 'Success'
        #except:
         #   return 'Failure'
    
    def AddPlayerNew(self,PlayerUser,*args):
                f = open('Char.json')
                dict = {}
                data = json.load(f)
                f.close()
                AlreadyExist = False
                for i in data['characters']:
                        if(i == PlayerUser):
                                AlreadyExist = True
                if(AlreadyExist is False):
                #insert new player
                
                        dataSet = []
                        try:
                                dataSet=  { 
                                "Strength" : args.strength,
                                "Dexterity" : args.dexterity,
                                "Constitution" : args.constitution,
                                "Intelligence" : args.intelligence,
                                "Wisdom" :  args.wisdom,
                                "Charisma" : args.charisma,
                                }
                        except:
                                dataSet=   {
                                "Strength" : self.AbilityRoll(self),
                                "Dexterity" : self.AbilityRoll(self),
                                "Constitution" : self.AbilityRoll(self),
                                "Intelligence" : self.AbilityRoll(self),
                                "Wisdom" : self.AbilityRoll(self),
                                "Charisma" : self.AbilityRoll(self)
                                }
                        #end of except
                        data['characters'][PlayerUser] = {'AbilityScore':{},'Inventory':{}}

                        data['characters'][PlayerUser]['AbilityScore'] = dataSet

                        data['characters'][PlayerUser]['Inventory'] = {}
                        
                        a_file = open("Char.json", "w")
                        json.dump(data, a_file, indent = 4)
                        a_file.close()         
                
                
    def AbilityRoll(self):
        lowest =10
        total = 0
        for i in range(0,4):
                #rolling d6
            temp = random.randint(1,6)
            if(temp<lowest):
                lowest = temp
            total += temp
        total -=lowest
        return total

    def AddRandPlayer(self,Name):
        f = open('Char.json')
        RandChar = Character(Name)
        dict = {}
        data = json.load(f)
        AlreadyExist = False
        for i in data['characters']:
            if(i == Name):
                AlreadyExist = True
        if(AlreadyExist ==False):
            data['characters'][Name] = {"AbilityScore":{"Strength":RandChar.Strength,"Dexterity": RandChar.Dexterity,"Constitution": RandChar.Constitution,"Intelligence": RandChar.Intelligence,"Wisdom":RandChar.Wisdom,"Charisma":RandChar.Charisma},"Inventory":{},"Race":RandChar.Race,"Age":RandChar.Age,"Gender":RandChar.Gender,"Speed":RandChar.Speed }
            a_file = open("Char.json", "w")
            json.dump(data, a_file)
            a_file.close()
            
            
if __name__ == '__main__':
    print(AddPlayer.AddPlayer(AddPlayer,False,"Sully1"))