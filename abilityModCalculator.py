import math

## This is how the ability score modifier is calculated for DND


def _getModifier(abilityScore):
    return math.floor((abilityScore - 10)/2)