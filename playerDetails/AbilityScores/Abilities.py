from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
from playerDetails.AbilityScores.Skills import Skills
from Player import Player 
import json


class Abilities:
    def __init__(self, _player):

       self.proficiencyBonus = 0
       self.abilityScores = AbilityScores(_player)
       self.savingThrows = SavingThrows(self)

    def parseFile():
        f = open('characters.json')

        data = json.load(f)

        for i in data['characters']:

            print(i)
            
        f.close()

def main(self):
        self.parseFile()
        self.proficiencyBonus = 0
        _player = Player(False,'Sully505')
        self.abilityScores = AbilityScores(_player)
        Abilities(self,_player)
        self.savingThrows = SavingThrows(self)
        self.skills = Skills(self)

