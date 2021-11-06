import math
class SavingThrows:
    def __init__(self, _parent):
        self.parent = _parent
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

    # Calculates the proficiency bonus modifiers for every proficiency bonus
    # If a saving throw is considered proficient, it will also have the players proficiency bonus added to the proficiency bonus modifier
    def calculateAllModifiers(self):
        for ability in self.abilities:
            if self.abilities[ability]["proficient"]:
                self.abilities[ability]["modifier"] = self._calculateModifier(
                    getattr(self.parent.abilityScores, ability)) + self.parent.proficiencyBonus
            else:
                self.abilities[ability]["modifier"] = self._calculateModifier(
                    getattr(self.parent.abilityScores, ability))
