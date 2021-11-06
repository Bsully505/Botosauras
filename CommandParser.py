
from DiceRoller import DiceRoller
from RollForDamage import RollForDamage

class CommandParser():
    def parse(command):
        #command should be in context of !(key command) (parameters)
        key = command.split(' ')[0]
        switcher={
            'r':DiceRoller.processCommand(DiceRoller,'!'+command),
            'M':RollForDamage.processCommand(RollForDamage,'!'+command)
        }
        return(switcher.get(key, "Invalid entry"))

        