#
#
#       Created by Harry Shepherd
#   ハリーシェッパードによって生み出した
#
#
import os
import json
def main():
    #Check if dictionary already exists
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'formDictionary.txt')
   
    try:
       with open(my_file) as output:
         print("File Found")
    except IOError:
       #If it doesnt, then make a new one
       print("File Not Found")
       print("Creating New File...")

       createNewDict(my_file)

    if os.stat(my_file).st_size == 0:
        print("Empty File")
        print("Creating Dictionary")
        createNewDict(my_file)

    while True:
        x = input("]")
        interpret(x, my_file)

def createNewDict(file):
    #The default dictionary
    thisdict={
        "thames water": 0,
        "skanska": 0,
        "costain": 0,
        "tideway": 0
    }
    with open(file, "w") as f:
        #Writes it to the text file in json format
        #so it can be read as a dictionary later on
        f.write(json.dumps(thisdict, indent=4)) #json.loads does the opposite
        f.close()
    print("Created New File")

def updateDictValue(file, key, value):
    try:
        with open(file, "r") as f:
            json_data = json.loads(f.read())
            f.close()
        #Check is the key exists in the dictioanry
        if key in json_data:
            #Updates value
            json_data[key] = value
            with open(file, "w") as f:
                f.write(json.dumps(json_data, indent=4))
                f.close()
                print("Updating key {} to {}".format(key, value))
        else:
            print("No such key exists")
    except Exception as e:
        print("There was an error updating the key.\n{}".format(e))

def readDict(file):
    try:
        with open(file, "r") as f:
            #Just prints the dictionary out
            print(f.read())
            f.close()
    except Exception as e:
        print("There was an error reading the file.\n{}".format(e))

def createNewKey(file, key, value):
    try:
        with open(file, "r") as f:
            json_data = json.loads(f.read())
            f.close()
        if key in json_data:
            #Checks if key exists, if so then stops function
            print("This key already exists")
            return
        #This creates a new key
        json_data[key.lower()] = value

        with open(file, "w") as f:
            f.write(json.dumps(json_data, indent=4))
            f.close()
        print("Created new key {} with value {}".format(key.lower(), value))
    except Exception as e:
        print("There was an error creating a new key\n{}".format(e))

def removeKey(file, key):
    try:
        with open(file, "r") as f:
            json_data = json.loads(f.read())
            f.close()
        try:
            #Delete the key in the dictionary
            del json_data[key.lower()]
        except KeyError:
            print("The given key does not exist")
            return
        with open(file, "w") as f:
            f.write(json.dumps(json_data, indent=4))
            f.close()
        print("Removed key {}".format(key.lower()))
    except Exception as e:
        print("There was an error removing the key.\n{}".format(e))
        
def interpret(command, file):
    #Just looks for a bunch of commands.
    #There is probably (almost definitely) a FAR better way to do this
    #I don't know how to properly make an interpreter. Thats something
    #I should probably learn in the future.
    if(command.lower() == "help"):
        print("Commands:\n - Update\n   - Update a key in dictionary\n - Create\n   - Create blank dictionary\n - Cls\n   - Clears screen\n - CreateKey\n   - Creates new key in dictionary\n - RemoveKey\n   - Removes key in dictionary")

    #Updates dictionary key
    elif(command.lower() == "update"):
        print("Key to update:")
        y = input("]")
        print("Value to update to:")
        z = input("]")
        updateDictValue(file, y, z)

    #Creates default dictionary - erases everything in process
    elif(command.lower() == "create"):
        print("Are you sure? This will erase the current dictionary. Y/N")
        y = input("]")
        if(y.lower == "y"):
            createNewDict(file)
        elif(y.lower == "n"):
            print("Aborting...")

    #Prints dictionary
    elif(command.lower() == "read"):
        readDict(file)

    #Clears screen
    #Only works if the .py is run - Wont work if the script is opened via interpreter e.g IDLE
    elif(command.lower() == "cls"):
        clear = lambda: os.system('cls')
        clear()

    #Creates new key in dictionary
    elif(command.lower() == "createkey"):
        print("Key to create:")
        y = input("]")
        print("Value to assign to:")
        z = input("]")
        createNewKey(file, y, z)

    #Removed key in dictionary
    elif(command.lower() == "removekey"):
        print("Key to remove:")
        y = input("]")
        removeKey(file, y)

    else:
        print("Command Unknown")
      
if __name__== "__main__":
   main()
