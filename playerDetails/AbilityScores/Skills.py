import math


class Skills:
    def __init__(self, _parent):
        self.parent = _parent
        self.skills = {
            "strength": {
                "athletics": {
                    "proficient": True,
                    "modifier": 0,
                },
            },
            "dexterity": {
                "acrobatics": {
                    "proficient": False,
                    "modifier": 0,
                },
                "sleight of hand": {
                    "proficient": False,
                    "modifier": 0,
                },
                "stealth": {
                    "proficient": False,
                    "modifier": 0,
                },
            },
            "intelligence": {
                "arcana": {
                    "proficient": False,
                    "modifier": 0,
                },
                "history": {
                    "proficient": False,
                    "modifier": 0,
                },
                "investigation": {
                    "proficient": False,
                    "modifier": 0,
                },
                "nature": {
                    "proficient": False,
                    "modifier": 0,
                },
                "religion": {
                    "proficient": False,
                    "modifier": 0,
                },
            },
            "wisdom": {
                "animal handling": {
                    "proficient": False,
                    "modifier": 0,
                },
                "insight": {
                    "proficient": False,
                    "modifier": 0,
                },
                "medicine": {
                    "proficient": False,
                    "modifier": 0,
                },
                "perception": {
                    "proficient": False,
                    "modifier": 0,
                },
                "survival": {
                    "proficient": False,
                    "modifier": 0,
                },
            },
            "charisma": {
                "deception": {
                    "proficient": False,
                    "modifier": 0,
                },
                "intimidation": {
                    "proficient": False,
                    "modifier": 0,
                },
                "performance": {
                    "proficient": False,
                    "modifier": 0,
                },
                "persuasion": {
                    "proficient": False,
                    "modifier": 0,
                },
            }
        }

    #Calculates a specific ability modifier for a skill.
    # The formula is given by the 5e rulebook
    def _calculateModifier(self, abilityScore):
        return math.floor((abilityScore - 10)/2)

    # Calculates the skill modifiers for every skill
    # If a skill is considered proficient, it will also have the players proficiency bonus added to the skills modifier
    def calculateAllModifiers(self):
        for ability in self.skills:
            for skill in self.skills[ability]:
                if (self.skills[ability][skill]["proficient"]):
                    self.skills[ability][skill]["modifier"] = self._calculateModifier(
                        getattr(self.parent.abilityScores, ability)) + self.parent.proficiencyBonus
                else:
                    self.skills[ability][skill]["modifier"] = self._calculateModifier(
                        getattr(self.parent.abilityScores, ability))
