
from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
from playerDetails.AbilityScores.Skills import Skills

import json




class Abilities:
    def __init__(self, _player):

       self.proficiencyBonus = 0
       self.abilityScores = AbilityScores(_player)
       self.savingThrows = SavingThrows(self)
       self.parseFile(_player)

    def parseFile(_player):
        f = open('characters.json')

        data = json.load(f)

        for i in data['characters']:
            if(i is _player._user):
                for z in data['characters'][i]:
                        for j in data['characters'][i][z]:
                                print(f"{z}: {j} ")
                print()
            
            
        f.close()

def main(self,_player):
        self.parseFile()
        self.proficiencyBonus = 0
  
        self.abilityScores = AbilityScores(_player)
        Abilities(self,_player)
        self.savingThrows = SavingThrows(self)
        self.skills = Skills(self)

