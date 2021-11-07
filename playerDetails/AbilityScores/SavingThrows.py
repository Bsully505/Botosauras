import math
class SavingThrows:
    def __init__(self, test):
        self.test = test
        self.abilities = {
            "strength": {
                "proficient": True,
                "modifier": 0,
            },
            "dexterity": {
                "proficient": False,
                "modifier": 0,
            },
            "constitution": {
                "proficient": False,
                "modifier": 0,
            },
            "intelligence": {
                "proficient": False,
                "modifier": 0,
            },
            "wisdom": {
                "proficient": False,
                "modifier": 0,
            },
            "charisma": {
                "proficient": False,
                "modifier": 0,
            }
        }

    def _calculateModifier(self, abilityScore):
        return math.floor((abilityScore - 10)/2)

    def calculateAllModifiers(self):
        ##Strength
        if (self.abilities["strength"]["proficient"]):
            self.abilities["strength"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.strength) + self.test.proficiencyBonus
        else:
            self.abilities["strength"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.strength)

        ##Dexterity
        if (self.abilities["dexterity"]["proficient"]):
            self.abilities["dexterity"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.dexterity) + self.test.proficiencyBonus
        else:
            self.abilities["dexterity"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.dexterity)

        ##Constitution
        if (self.abilities["constitution"]["proficient"]):
            self.abilities["constitution"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.constitution) + self.test.proficiencyBonus
        else:
            self.abilities["constitution"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.constitution)

        ##Intelligence
        if (self.abilities["intelligence"]["proficient"]):
            self.abilities["intelligence"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.intelligence) + self.test.proficiencyBonus
        else:
            self.abilities["intelligence"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.intelligence)

        ##Wisdom
        if (self.abilities["wisdom"]["proficient"]):
            self.abilities["wisdom"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.wisdom) + self.test.proficiencyBonus
        else:
            self.abilities["wisdom"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.wisdom)

        ##Charisma
        if (self.abilities["charisma"]["proficient"]):
            self.abilities["charisma"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.charisma) + self.test.proficiencyBonus
        else:
            self.abilities["charisma"]["modifier"] = self._calculateModifier(
                self.test.abilityScores.charisma)