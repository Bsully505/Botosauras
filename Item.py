
#inventory list
inventory = []
class Item:
    
    def AddItemToInventory(self,User,ItemName):
        #this is supposed to call the JsonInteract Class and use the InsertIntoInventory(self,User,Item): function to insert into inventory
        print(f"Adding {ItemName} into {User}\'s Inventory")
        
    def RemoveItemFromInventory(self,User,ItemName):
        #this is supposed to call the JsonInteract Class and the function def DeleteInventoryItem(self,User,item):
        print(f"Removing {ItemName} into {User}\'s Inventory")
    oldList = [];
    y = ""
    def initialQuestion(self):
        # Ask user if they want to add item or open a previous list (saved as text file)
        print("would you like to add an item or open a previous list?: ")
        choice = input()
        #if the input is not open or add
        while not (choice == "open" or choice == "add"):
            print("Enter open or add: ")
            choice = input()
            #if input is open, take user to opening a previous doc
        if(choice == ("open")):
            print("what is your username?: ")
            self.y = input()
            Item.ReadandMakeList(Item)
            #if input is add, take user to adding an item
        if(choice == ("add")):
            Item.AddItem(Item)
#Adding an item
    def AddItem(self):
        #ask user their name so the file can be named
        print("what is your username?: ")
        self.y = input()
        print("What item would you like to add?: ")
        x = input()
        #add input to an inventory list
        inventory.append(x)
        print(x + " was added to your inventory")
        print("Would you like to add another item? (Y or N): ")
        answer = input()
        #if they do not answer Y or N
        while not(answer == "Y" or answer == "N"):
            print("please enter 'Y' or 'N'")
            answer = input()
            #if yes loop to ask them if they would like to keep adding items
        while(answer == ("Y")):
            print("What item would you like to add?: ")
            x = input()
            #add input to inventory list
            inventory.append(x)
            print("Would you like to add another Item?: ")
            answer = input()
            #check if answer is Y or N WITHIN the while loop
            while not (answer == "Y" or answer == "N"):
                print("please enter 'Y' or 'N'")
                answer = input()
        #if answer is N then inventory all done and print and save it
        if(answer == ("N")):
            print("here is your inventory: ")
            Item.PrintAndSavingList(Item)


#Printing and saving inventory
    def PrintAndSavingList(self):
        # Using a for loop print Inventory List
        #self.y refers to the username
        with open(self.y +'.txt', 'w') as f:
            for i in inventory:
                print(i)
                #write the list onto the file
                f.write(i)
                #add a comma so the reader can turn it back into a list DO NOT REMOVE COMMA
                f.write(",")
    #if player wants to remove an item
    def ReadAndRemove(self):
        import csv
        import os.path
        #check if the file exists
        file_exists = os.path.exists(self.y + ".txt")
        #if file exists run code to remove an item
        if (file_exists):
            with open(self.y + ".txt") as f:
                line = csv.reader(f, delimiter=',')
                #place text into a new list which can be edited
                oldList = (list(line)[0])
                print(oldList)
                print("what item would you like to remove? ")
                x = input()
                #if the item the user specified is not found in the file
                if x not in oldList:
                    print("item not found, please enter an item you have with correct spelling and capitalization: ")
                    x = input()
                #if the item the user specified is in the file
                if x in oldList:
                    #remove the item the user specified
                    oldList.remove(x)
                    print("here is your inventory: ")
                    #overwrite the file using the  oldList array
                    with open(self.y + '.txt', 'w') as f:
                        for i in oldList:
                            print(i)
                            f.write(i)
                            f.write(",")
                    print(oldList)
        #if the file does not exist, print error message
        if not (file_exists):
            print("file does not exist")


    #To read the list already made
    def ReadandMakeList(self):
        import csv
        import os.path
        #check if the username text exists
        file_exists = os.path.exists(self.y+".txt")
        #if the username text file does exist
        if(file_exists):
            with open(self.y+".txt") as f:
                line = csv.reader(f, delimiter=',')
                # place text into a new list which can be edited
                oldList = (list(line)[0])
                print(oldList)
                #ask user if they want to add or remove an item
                print("Would you like to add or remove an item: ")
                x = input()
                #if the input is not add or remove, make sure they enter it correctly
                while not(x == "remove" or x == "add"):
                    print("please enter 'add' or 'remove': ")
                    x = input()
                #if the input is remove then send the user to the ReadAndRemove function
                if(x == "remove"):
                    Item.ReadAndRemove(Item)
                #if the input is add then allow player to make altercations to the text file
                if(x == "add"):
                    print("Would you like to add another item? (Y or N): ")
                    answer = input()
                    #Ensure the answer is either Y or N
                    while not(answer == "Y" or answer == "N"):
                        print("please enter 'Y' or 'N'")
                        answer = input()
                    #same loop from AddItem where the user is asked to add an item and can keep going until finished
                    while (answer == ("Y")):
                        print("What item would you like to add?: ")
                        x = input()
                        #update the oldList array
                        oldList.append(x)
                        print("Would you like to add another Item?: ")
                        answer = input()
                        #ensure the answer is Y or N WITHIN the while loop
                        while not (answer == "Y" or answer == "N"):
                            print("please enter 'Y' or 'N'")
                            answer = input()
                    #if the user is finished, overwrite the file with the oldList array which was just made
                    if (answer == ("N")):
                        print("here is your inventory: ")
                        with open(self.y + '.txt', 'w') as f:
                            for i in oldList:
                                print(i)
                                f.write(i)
                                #IMPORTANT keep comma in order for the file reader to make the text file back into a list
                                f.write(",")
                        print(oldList)
        #if the file for the specified username does not exist, print error message
        if not(file_exists):
            print("file does not exist")

Item.initialQuestion(Item)

