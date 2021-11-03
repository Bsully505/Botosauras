import random
from playerDetails.AbilityScores.Abilities import Abilities
from playerDetails.Attacks import Attacks
from playerDetails.Spells import Spells
from playerDetails.Equipment import Equipment
from playerDetails.rolePlayTraits import RolePlayTraits


class Player:

    def __init__(self, _isDM, _user):
        self.user = _user  # Will be used to connect the slack user to the character

        # Might be changed, but is used to signify if the player is a Dungeon Master.
        self.isDM = _isDM

        self.level = 0  # Will be used to calculate proficiency modifier as well as available spells in the future
        self.clas = 0  # Will be used to find available spells in the future
        self.background = ""
        self.alignment = ""

        self.abilities = Abilities(self)

        #
        self.hitPoints = 0
        self.armorClass = 0
        self.initiative = 0

        self.spells = Spells(self)
        self.attacks = Attacks(self)
        self.equipment = Equipment(self)

        self.rolePlayTraits = RolePlayTraits(self)

    def rollDie(self, sides):
        return round((random.random()*sides)+1)

    # Return an organized 'character sheet' of the player
    def print(self):
        return ""

    def get(self):
        return 1
