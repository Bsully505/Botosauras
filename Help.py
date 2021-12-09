class Help:
    def getHelp():
        helper = 'Helping with commands \n'
        rollingHelp = ' Roll a dice: !R (amount of dice rolled)D(number of sides on dice ex 4,8,10,12,20) skill value advantageStatus all seperated by spaces ex !r 1D20 +2 A\n'
        helper +=rollingHelp
        AttackCritHelp = 'AttackCrit: !A: no params, returns true or false\n'
        helper+= AttackCritHelp
        DamageHelp = 'Attack: !M (numberOfRolls)D(SidesofDice)ex !M 1D20 would roll once with the dice being a 20 sided dice\n'
        helper +=DamageHelp
        AddRandomPlayer = 'Adding Random Player: !ARP (Name) this will create a random Character generator\n'
        helper += AddRandomPlayer
        AddRandomPlayer = 'Print All Players: !PAP no Params just prints out all the names of the characters\n'

        return helper