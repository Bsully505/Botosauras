from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
from playerDetails.AbilityScores.Skills import Skills
from TestingChar import TestingChar


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
                                "strength" : args.strength,
                                "dexterity" : args.dexterity,
                                "constitution" : args.constitution,
                                "intelligence" : args.intelligence,
                                "wisdom" :  args.wisdom,
                                "charisma" : args.charisma,
                                }
                        except:
                                dataSet=   {
                                "strength" : 0,
                                "dexterity" : 0,
                                "constitution" : 0,
                                "intelligence" : 0,
                                "wisdom" : 0,
                                "charisma" : 0
                                }
                        #end of except
                        data['characters'][PlayerUser] = dataSet
                        a_file = open("Char.json", "w")
                        json. dump(data, a_file)
                        a_file.close()
                

                        
                f.close()

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