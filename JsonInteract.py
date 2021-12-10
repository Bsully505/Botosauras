import json


# what i implemented
# Add Random Player

# Edit Player Stats

# Get All Players

#

# Add Inventory Item

# Still need to implement
# Delete character
# insert all Stats
class TestingChar:

    def AddPlayer(self, PlayerUser, *args):
        f = open('Char.json')
        dict = {}
        data = json.load(f)
        AlreadyExist = False
        for i in data['characters']:
            if (i == PlayerUser):
                AlreadyExist = True
        if (AlreadyExist is False):
            # insert new player

            dataSet = []
            try:
                dataSet = {
                    "Strength": args.strength,
                    "Dexterity": args.dexterity,
                    "Constitution": args.constitution,
                    "Intelligence": args.intelligence,
                    "Wisdom": args.wisdom,
                    "Charisma": args.charisma,
                }
            except:
                dataSet = {
                    "Strength": 0,
                    "Dexterity": 0,
                    "Constitution": 0,
                    "Intelligence": 0,
                    "Wisdom": 0,
                    "Charisma": 0
                }
            # end of except
            data['characters'][PlayerUser]['AbilityScore'] = dataSet
            data['characters'][PlayerUser]["Inventory"] = {}
            a_file = open("Char.json", "w")
            json.dump(data, a_file, indent=4)
            a_file.close()

        f.close()

    def EditPlayerStats(self, User, StatName, NewValue):
        f = open('Char.json')
        dict = {}
        data = json.load(f)
        for i in data['characters']:
            if (i == User):
                for z in data['characters'][i]:
                    # currently at users json
                    dict = data['characters'][i]['AbilityScore']
                    res = dict.pop(StatName, None)
                    if (res):
                        dict['StatName'] = NewValue
                        data['characters'][i]['AbilityScore'] = dict
                        return "Success"
                    else:
                        return "Failure"

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
            if (i == player):
                return data['characters'][i]

    def GetPlayer(self, User):
        f = open('Char.json')
        dict = {}
        data = json.load(f)
        for i in data['characters']:
            if (i == User):
                dict[i] = data['characters'][i]
                return dict

    def PrintPlayerStats(self, PlayerUser):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        for i in data['characters']:
            if (i == PlayerUser):
                for z in data['characters'][i]:
                    for j in data['characters'][i][z]:
                        print(f"{z} :{j}")
                        dict[z] = j
        return dict

    def InsertIntoInventory(self, User, Item):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        for i in data['characters']:
            if (i == User):  # I am at the characters index
                # get inventory
                for z in data['characters'][i]:
                    if (z == 'Inventory'):
                        dict = data['characters'][i][z]
                        dict[Item] = 1
                        data['characters'][i][z] = dict
                        if Item in data:
                            dict[Item]=2
        a_file = open("Char.json", "w")
        json.dump(data, a_file, indent=4)
        a_file.close()

    def DeleteInventoryItem(self, User, item):
        f = open('Char.json')

        data = json.load(f)

        res = data['characters'][User]["Inventory"].pop(item, None)
        if (res):
            a_file = open("Char.json", "w")
            json.dump(data, a_file, indent=4)
            a_file.close()
            return "Success"
        return "Failure"

    def PrintInventory(self, User):
        f = open('Char.json')
        dict = []
        data = json.load(f)
        for i in data['characters']:
            if (i == User):  # I am at the characters index
                # get inventory
                return data['characters'][i]['Inventory']  # returns the dict of the inventory
        return 'No Such Player'
    def PrintWholeJsonFile(self):
        return json.load(open('Char.json'))

    def Print(self,User):
        fp = open("Char.json")
        data = json.load(fp)
        #  Use the slicing to get a particular value from a json file.
        print(data['characters'][User]['Inventory'])
    
    def DeletePlayer(self,User):
        fp = open("Char.json")
        data = json.load(fp)
        print(User)
        res = data['characters'].pop(User, None)
        if(res):
            a_file = open("Char.json", "w")
            json.dump(data, a_file, indent=4)
            a_file.close()
            return 'Success'
        return 'Failure'
            
        
        


if __name__ == '__main__':
    print(TestingChar.PrintWholeJsonFile(TestingChar))