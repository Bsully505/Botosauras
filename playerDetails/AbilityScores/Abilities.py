from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
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