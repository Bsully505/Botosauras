import json


class TestingChar:

    def AddPlayer(self,PlayerUser,*args):
        f = open('Char.json')
        dict = {}
        data = json.load(f)
        AlreadyExist = False
        for i in data['characters']:
            if(i == PlayerUser):
                AlreadyExist = True
        if(AlreadyExist is False):
            #insert new player
           
            dataSet = []
            try:
                dataSet=  { 
                    "strength" : args.strength,
                    "dexterity" : args.dexterity,
                    "constitution" : args.constitution,
                    "intelligence" : args.intelligence,
                    "wisdom" :  args.wisdom,
                    "charisma" : args.charisma,
                    }
            except:
                dataSet=   {
                    "strength" : 0,
                    "dexterity" : 0,
                    "constitution" : 0,
                    "intelligence" : 0,
                    "wisdom" : 0,
                    "charisma" : 0
                    }
            #end of except
            data['characters'][PlayerUser] = dataSet
            a_file = open("Char.json", "w")
            json. dump(data, a_file)
            a_file.close()
            
    
                
        f.close()

    def GetAllPlayers(self):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        AlreadyExist = False
        for i in data['characters']:
            print(i)
            dict.append(i)
        return dict

    def findPlayer(self, player):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        for i in data['characters']:
            if(i == player):
                return data['characters'][i]

    def PrintPlayerStats(self,PlayerUser):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        for i in data['characters']:
            if(i ==PlayerUser):
                for z in data['characters'][i]:
                        for j in data['characters'][i][z]:
                                print(f"{z} :{j}")
                                dict[z] = j


if __name__ =='__main__':
    TestingChar.AddPlayer(TestingChar,'Bryan')
    print(TestingChar.GetAllPlayers(TestingChar))