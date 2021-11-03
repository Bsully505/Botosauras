from playerDetails.AbilityScores import AbilityScores
from playerDetails.AbilityScores.SavingThrows import SavingThrows


class Abilities:
    def __init__(self, _player):
        self.proficiencyBonus = 0
        self.abilityScores = AbilityScores(_player)
        self.savingThrows = SavingThrows(_player)
