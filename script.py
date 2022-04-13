#!/usr/bin/env python3
# Bugs include: Select sorcerer == crash
# This is so stupid but it helped kill an hour 
import json
import random

class spellClass:
    bard = 'Bard'
    cleric = 'Cleric'
    druid = 'Druid'
    paladin = 'Paladin'
    ranger = 'Ranger'
    sorcerer = 'Sorcerer'
    warlock = 'Warlock'
    wizard = 'Wizard'

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   

  
# Input: class name
# Process: Filter json by class (user input)
# Select random spell from new list
# Output: spell name
def chooseSpell(className):
    # Load the data from the local spells.json file
    with open('spells.json') as f:
        data = json.load(f)
        # Filter the data by class
        filteredData = [spell for spell in data if spell['class'] == className]
        # Select random spell
        randomSpell = filteredData[random.randint(0, len(filteredData) - 1)]
        # Print random spell
        return randomSpell['name']


# Print out list of all spellClass variables
# Then take user input for class
# Return class name
def chooseClass():
    print("Bard")
    print("Cleric")
    print("Druid")
    print("Paladin")
    print("Ranger")
    print("Sorcerer")
    print("Warlock")
    print("Wizard")
    print()
    className = input("\n" + color.BOLD + color.UNDERLINE + "Choose a class: " + color.END)
    # Error handling
    while className not in spellClass.__dict__.values():
        className = input("\n" + color.BOLD + color.UNDERLINE + "Choose a class: " + color.END)

    # Return class name
    return className

if __name__ == '__main__':

    status = True

    # Main Loop
    while status == True:
        # Print random entry
        print('\n' + color.BOLD + chooseSpell(chooseClass()) + color.END + '\n')
        # Continue loop or break
        v = input("Another? [" + color.GREEN + 'y' + color.END + '/' + color.RED + 'n' + color.END + ']').lower()
        if v == 'n':
            break
        if v == 'y':
            continue