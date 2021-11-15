# Python3 code to iterate over a list
inventory = []
class Item:

    def initialQuestion(self):
        # Ask user if they want to add item or open a previous list (saved as text file)
        print("would you like to add an item or open a previous list?: ")
        choice = input()
        if (choice == ("open")):
            Item.ReadPreviousInventory(Item)
        else:
            Item.AddItem(Item)

    def AddItem(self):
        print("What item would you like to add?: ")
        x = input()
        inventory.append(x)
        print(x + " was added to your inventory")
        print("Would you like to add another item? (Y or N): ")
        answer = input()
        while(answer == ("Y")):
            print("What item would you like to add?: ")
            x = input()
            inventory.append(x)
            print("Would you like to add another Item?: ")
            answer = input()
        if(answer == ("N")):
            print("here is your inventory: ")
            Item.PrintAndSavingList(Item)
        else:
            print("please enter 'Y' or 'N'")
            answer = input()


    def PrintAndSavingList(self):
        # Using a for loop print Inventory List
        with open('readme.txt', 'w') as f:
            for i in inventory:
                print(i)
                f.write(i)
                f.write("/n")

    def ReadPreviousInventory(self):
        f = open("readme.txt", "r")
        print(f.read())
        inventory = f.readlines()
        for i in f.readlines():
            print(i)
            print(",")


Item.initialQuestion(Item)

