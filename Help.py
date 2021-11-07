class Help:
    def getHelp():
        helper = 'Helping with commands \n'
        rollingHelp = ' Roll a dice: !r (amount of dice rolled)D(number of sides on dice ex 4,8,10,12,20) skill value advantageStatus all seperated by spaces ex !r 1D20 +2 A\n'
        helper +=rollingHelp
        AttackCritHelp = 'AttackCrit: !A: no params, returns true or false\n'
        helper+= AttackCritHelp
        DamageHelp = 'Attack: !M\n'
        helper +=DamageHelp
        return helper