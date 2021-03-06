import math

class AbilityScores:
    def get(self):
        return [
            {"name": "STRENGTH", "modifier": self._calculateModifier(
                self.strength), "score": self.strength},
            {"name": "DEXTERITY", "modifier": self._calculateModifier(
                self.dexterity), "score": self.dexterity},
            {"name": "CONSTITUTION", "modifier": self._calculateModifier(
                self.constitution), "score": self.constitution},
            {"name": "INTELLIGENCE", "modifier": self._calculateModifier(
                self.intelligence), "score": self.intelligence},
            {"name": "WISDOM", "modifier": self._calculateModifier(
                self.wisdom), "score": self.wisdom},
            {"name": "CHARISMA", "modifier": self._calculateModifier(
                self.charisma), "score": self.charisma}
        ]

    def _calculateModifier(self, abilityScore):
        return math.floor((abilityScore - 10)/2)
      
    global player 
    global strength 
    global dexterity 
    global constitution 
    global intelligence 
    global wisdom 
    global charisma 
    def __init__(self, _player,*args):
            self.player = _player
            try:

                    self.strength = args.strength
                    self.dexterity = args.dexterity
                    self.constitution = args.constitution
                    self.intelligence = args.intelligence
                    self.wisdom =  args.wisdom
                    self.charisma = args.charisma
            except:

                    self.strength = 0
                    self.dexterity = 0
                    self.constitution = 0
                    self.intelligence = 0
                    self.wisdom = 0
                    self.charisma = 0

    def get(self):
        return {
                    "Strength":self.strength,
                    "Dexterity":self.dexterity,
                    "Constitution":self.constitution,
                    "Intelligence":self.intelligence ,
                    "Wisdom":self.wisdom ,
                    "Charisma":self.charisma 
            }
