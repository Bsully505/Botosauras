
from DiceRoller import DiceRoller
from RollForDamage import RollForDamage
from Help import Help
from CriticalAttack import CriticalAttack
from AddPlayer import AddPlayer

class CommandParser():
    def parse(command):
        #command should be in context of !(key command) (parameters)
        key = command.split(' ')[0].upper()
        switcher={
            'R':lambda: DiceRoller.getRoll(DiceRoller,'!'+command),
            'M':lambda: RollForDamage.processCommand(RollForDamage,'! '+command),
            'A':lambda: CriticalAttack.Attackroll(CriticalAttack),
            'H':lambda: Help.getHelp(),
            'AP': lambda: AddPlayer(command.split(" ")[1],command.split(" ")[2])
        }
        return(switcher.get(key, lambda:"You did not enter a correct command type !H to get commands")())

        