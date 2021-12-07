import requests 
from InterfaceCharacter import Character
import json
 
class AddPlayer:
    url = 'https://slackevent.herokuapp.com/'
    def AddPlayer(self,is_DM,User):
        
        res =requests.post(self.url+'PostChar', json= {"type":is_DM,"User":User})
        return res.text
    
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
    AddPlayer.AddPlayer(AddPlayer,"Sully")