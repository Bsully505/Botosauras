
from DiceRoller import DiceRoller
from RollForDamage import RollForDamage
from Help import Help
from CriticalAttack import CriticalAttack
from AddPlayer import AddPlayer
from JsonInteract import TestingChar
from Item import Item

class CommandParser():
    def parse(command):
        #command should be in context of !(key command) (parameters)
        key = command.split(' ')[0].upper()
        
        switcher={
            'R':lambda: DiceRoller.getRoll(DiceRoller,'!'+command),
            'M':lambda: RollForDamage.processCommand(RollForDamage,'! '+command),
            'A':lambda: CriticalAttack.Attackroll(CriticalAttack),
            'H':lambda: Help.getHelp(),
            'AP': lambda: AddPlayer.AddPlayer(AddPlayer,command.split(" ")[1],command.split(" ")[2]),
            'ARP': lambda: AddPlayer.AddRandPlayer(AddPlayer,command.split(" ",1)[1]),
            'PAP': lambda: TestingChar.GetAllPlayers(TestingChar),
            'ADDI': lambda: Item.AddItemToInventory(Item,command.split(" ")[1],command.split(" ")[2]),
            'I': lambda: Item.PrintInventory(Item,command.split(" ")[1]),
            'RI':lambda: Item.ReadAndRemove(Item,command.split(" ")[1],command.split(" ")[2])
        }
        
        return(switcher.get(key, lambda:"You did not enter a correct command type !H to get commands")())
        
            #return("Error on Server side make sure you wrote a correct command")
if __name__ == '__main__':
    print(CommandParser.parse('ADDI Sully Sword'))