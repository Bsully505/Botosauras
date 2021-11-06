from playerDetails.AbilityScores.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows
from playerDetails.AbilityScores.Skills import Skills


class Abilities:
    def __init__(self, _player):
        self.proficiencyBonus = 0
        self.abilityScores = AbilityScores(_player)
        self.savingThrows = SavingThrows(self)
        self.skills = Skills(self)
