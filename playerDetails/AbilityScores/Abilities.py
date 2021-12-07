from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
from playerDetails.AbilityScores.Skills import Skills
from JsonInteract import TestingChar
import random


import json




class Abilities:
        def __init__(self, _player ,*args):
                if(self.PlayerExist(_player.user)):
                        self.proficiencyBonus = 0
                        self.abilityScores = AbilityScores(_player,self.parseFile(_player))
                        self.savingThrows = SavingThrows(self)
                else:
                        self.AddPlayer(_player.user,*args)
                        self.proficiencyBonus = 0
                        self.abilityScores = AbilityScores(_player,self.parseFile(_player))
                        self.savingThrows = SavingThrows(self)


        def parseFile(self,_player):
                f = open('playerDetails/AbilityScores/characters.json')
                dict = {}
                data = json.load(f)

                for i in data['characters']:
                        if(i == _player.user):
                                for z in data['characters'][i]:
                                        for j in data['characters'][i][z]:
                                                dict[z]= j 
                        
                f.close()
                return dict

        def PlayerExist(self,PlayerUser,*args):
                f = open('Char.json')
                dict = {}
                data = json.load(f)
                AlreadyExist = False
                for i in data['characters']:
                        if(i == PlayerUser):
                                AlreadyExist = True
                return AlreadyExist

        def AddPlayer(self,PlayerUser,*args):
                f = open('Char.json')
                dict = {}
                data = json.load(f)
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
                                "Strength" : self.AbilityRoll(),
                                "Dexterity" : self.AbilityRoll(),
                                "Constitution" : self.AbilityRoll(),
                                "Intelligence" : self.AbilityRoll(),
                                "Wisdom" : self.AbilityRoll(),
                                "Charisma" : self.AbilityRoll()
                                }
                        #end of except
                        data['characters'][PlayerUser]['AbilityScore'] = dataSet
                        data['characters'][PlayerUser]['Inventory'] = {}
                        a_file = open("Char.json", "w")
                        json. dump(data, a_file, indent = 4)
                        a_file.close()
                

                        
                f.close()
                
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

        def GetAllPlayers(self):
                f = open('Char.json')
                data = json.load(f)
                for i in data['characters']:
                        print(i)
                        dict.append(i)
                return dict

        def PrintPlayerStats(self,PlayerUser):
                f = open('Char.json')
                dict = []
                data = json.load(f)
                for i in data['characters']:
                        if(i ==PlayerUser):
                                for z in data['characters'][i]:
                                        for j in data['characters'][i][z]:
                                                print(f"{z} :{j}")
                                                dict[z] = j
                return dict



def main(self,_player):
        self.parseFile()
        self.proficiencyBonus = 0
  
        self.abilityScores = AbilityScores(_player)
        Abilities(self,_player)
        self.savingThrows = SavingThrows(self)
        self.skills = Skills(self)