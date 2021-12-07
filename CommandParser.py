
from DiceRoller import DiceRoller
from RollForDamage import RollForDamage
from Help import Help
from CriticalAttack import CriticalAttack
from AddPlayer import AddPlayer
from Item import Item
from JsonInteract import TestingChar

class CommandParser():
    def parse(command):
        #command should be in context of !(key command) (parameters)
        key = command.split(' ')[0].upper()
        switcher={
            'R':lambda: DiceRoller.getRoll(DiceRoller,'!'+command),
            'M':lambda: RollForDamage.processCommand(RollForDamage,'! '+command),
            'A':lambda: CriticalAttack.Attackroll(CriticalAttack),
            'H':lambda: Help.getHelp(),
            'I':lambda: Item.initialQuestion(),
            'AP': lambda: AddPlayer.AddPlayer(AddPlayer,command.split(" ")[1],command.split(" ")[2]),
            'ARP': lambda: AddPlayer.AddRandPlayer(AddPlayer,command.split(" ",1)[1]),
            'PAP': lambda: TestingChar.GetAllPlayers(),
            'AddI': lambda: TestingChar.InsertIntoInventory(TestingChar,command.split(" ")[0],command.split(" ")[1]),
            'PI': lambda: TestingChar.PrintInventory(TestingChar,command.split(" ")[0])
        }
        return(switcher.get(key, lambda:"You did not enter a correct command type !H to get commands")())

        