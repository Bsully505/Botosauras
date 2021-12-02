#import dnd_character.classes as dnd
import random

'''
Author Bryan Sullivan
Date Worked on: Novmeber 27
improvements to add:
-be able to include in args users input on what they want aka if they want the race to be Halfling
-include the skills versatility
-include more phisical attriutes like the actual height in cm not just the size medium 
-half-Elf,Human  needs to be able to learn a random language
-implement HP and Subrace


'''

class Character:
    global Name
    global Race
    global SubRace
    global Age
    global Strength
    global Dexterity
    global Constitution
    global Wisdom
    global Intelligence
    global Charisma 
    global Hp
    global Languages
    global Gender
    global Size 
    global Speed
    global abilities
   
    
    def __init__(self,Name,*args):
        self.abilities = ['Strength','Dexterity','Constitution','Wisdom','Intelligence','Charisma']
        self.Gender = self.DeterineGender()
        self.Name = Name
        self.Race = self.GetRandomRace()
        abilityScores = {"Strength":self.AbilityRoll(),"Dexterity":self.AbilityRoll(),"Constitution":self.AbilityRoll(),"Wisdom":self.AbilityRoll(),"Intelligence":self.AbilityRoll(),"Charisma":self.AbilityRoll()}
        abilityScores = self.RaceAbilityModifier(self.Race, abilityScores)

        for i in abilityScores.keys():
            exec(f"self.{i} = {int(abilityScores[i])}")
        
  
        #Player1 = eval(f"dnd.{race}(name = \"{Name}\",level=1)")
        #print(Player1.wisdom)
        
    def GetRandomRace(self): 
        Races = ['Dragonborn','Dwarf','Elf','Gnome','Half-Elf','Halfling','Half-Orc','Human','Tiefling']
        return Races[random.randint(0,len(Races)-1)]
    def AbilityRoll(self):
        lowest =10
        total = 0
        for i in range(0,4):
            #rolling d6
            temp = random.randint(1,6)
            if(temp<lowest):
                lowest = temp
            total += temp
        total -=lowest
        return total
    def DeterineGender(self):
        if(random.randint(0,1)==0):
            return "Female"
        else:
            return "Male"
        
    def RaceAbilityModifier(self,race,AbilityDict):
        if(race ==  'Dragonborn'):
            AbilityDict['Strength'] =  AbilityDict['Strength'] +2
            AbilityDict['Charisma'] = AbilityDict['Charisma']+1
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(15,70)
            self.Languages = ['Common','Draconic']
            return AbilityDict    
        elif(race == 'Dwarf'):
            AbilityDict['Constitution'] =  AbilityDict['Constitution'] +2
            self.Speed = 25
            self.Size = "Medium"
            self.Age = random.randint(50,300)
            self.Languages = ['Common','Dwarvish']
            return AbilityDict
        elif(race == 'Elf'):
            AbilityDict['Dexterity'] =  AbilityDict['Dexterity'] +2
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(100,725)
            self.Languages = ['Common','Elvish']
            return AbilityDict
        elif(race == 'Gnome'):
            AbilityDict['Intelligence'] =  AbilityDict['Intelligence'] +2
            self.Speed = 25
            self.Size = "Small"
            self.Age = random.randint(50,375)
            self.Languages = ['Common','Gnomish']
            ##subsRace Deep Gnome, Rock Gnome
            return AbilityDict
        elif(race == 'Half-Elf'):
            AbilityDict['Charisma'] =  AbilityDict['Charisma'] +2
            adjuster1 = self.getRandomAbility("Charisma")
            AbilityDict[adjuster1] = AbilityDict[adjuster1] +1
            adjuster2 = self.getRandomAbility("Charisma")
            AbilityDict[adjuster2] = AbilityDict[adjuster2] +1
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(20,150)
            self.Languages = ['Common','Elvish']
            return AbilityDict
        elif(race == 'Halfling'):
            AbilityDict['Dexterity'] =  AbilityDict['Dexterity'] +2
            self.Speed = 25
            self.Size = "Small"
            self.Age = random.randint(20,120)
            self.Languages = ['Common','Halfling']                
            return AbilityDict
        elif(race == 'Half-Orc'):
            AbilityDict['Strength'] =  AbilityDict['Strength'] +2
            AbilityDict['Constitution'] =  AbilityDict['Constitution'] +1
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(15,60)
            self.Languages = ['Common','Orc']                
            return AbilityDict
        elif(race == 'Human'):
            AbilityDict['Strength'] =  AbilityDict['Strength'] +1
            AbilityDict['Dexterity'] =  AbilityDict['Dexterity'] +1
            AbilityDict['Constitution'] =  AbilityDict['Constitution'] +1
            AbilityDict['Wisdom'] =  AbilityDict['Wisdom'] +1
            AbilityDict['Intelligence'] =  AbilityDict['Intelligence'] +1
            AbilityDict['Charisma'] =  AbilityDict['Charisma'] +1
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(18,80)
            self.Languages = ['Common']                
            return AbilityDict
        elif(race == 'Tiefling'):
            AbilityDict['Intelligence'] =  AbilityDict['Intelligence'] +1
            AbilityDict['Charisma'] =  AbilityDict['Charisma'] +2
            self.Speed = 30
            self.Size = "Medium"
            self.Age = random.randint(18,85)
            self.Languages = ['Common','Infernal']                
            return AbilityDict
    
    
    def getRandomAbility(self,DontInclude):  
        temp= self.abilities[len(self.abilities)-1]
        if(DontInclude):
            while(temp ==DontInclude):
                temp= self.abilities[len(self.abilities)-1]
        return temp
               
if __name__ == '__main__':
    player = Character("Bryan")

    print(f"Name: {player.Name}")
    #print(f"Hp: {player.Hp}")
    print(f"Age: {player.Age}")
    print(f"Gender: {player.Gender}")
    print(f"Race: {player.Race}")
    #print(f"SubRace: {player.SubRace}")
    print(f"Size: {player.Size}")
    print(f"Speed: {player.Speed}")
    print(f"Languages: {player.Languages}")
    print(f"Strength: {player.Strength}")
    print(f"Dexterity: {player.Dexterity}")
    print(f"Constitution: {player.Constitution}")
    print(f"Wisdom: {player.Wisdom}")
    print(f"Intelligence: {player.Intelligence}")
    print(f"Charisma: {player.Charisma}") 
    

    
    

    


