
from DiceRoller import DiceRoller
from RollForDamage import RollForDamage
from Help import Help
from CriticalAttack import CriticalAttack

class CommandParser():
    def parse(command):
        #command should be in context of !(key command) (parameters)
        key = command.split(' ')[0]
        switcher={
            'r':DiceRoller.getRoll(DiceRoller,'!'+command),
            'M':RollForDamage.processCommand(RollForDamage,'!'+command),
            'A':CriticalAttack.Attackroll(CriticalAttack),
            'H':Help.getHelp()
        }
        return(switcher.get(key, "You did not enter a correct command type !H to get commands"))

        