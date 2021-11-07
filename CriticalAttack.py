import random
class CriticalAttack:
    def Attackroll(self):
        roll = random.randint(1,20)
        total = 0
        critical = False
        print ("your roll is: " + str(roll))
        total = total + roll
        print("total: " + str(total))
        if(roll == 20):
            critical = True
        while(critical == True):
            roll = random.randint(1,20)
            print("Critical hit: your new roll is: " + str(roll))
            total = total + roll
            print("total value is : " + str(total))
            if(roll != 20):
                critical = False
if (__name__ == "__main__"):
    #+2 will be replaced with a skill that will then be used to calculate the bonus to be added
    CriticalAttack.Attackroll(CriticalAttack)
