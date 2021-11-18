from playerDetails.Player import Player
tim = Player(False, "Timothy")

tim.abilities.abilityScores.strength = 20
tim.abilities.savingThrows.calculateAllModifiers()

print(tim.get())
