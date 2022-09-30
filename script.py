#!/usr/bin/env python3
# This is so stupid but, it helped kill an hour
import json
import random


class SpellClass:
    bard = 'Bard'
    cleric = 'Cleric'
    druid = 'Druid'
    paladin = 'Paladin'
    ranger = 'Ranger'
    sorcerer = 'Sorcerer'
    warlock = 'Warlock'
    wizard = 'Wizard'


class Color:
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
def choose_spell(class_name):
    # Load the data from the local spells.json file
    with open('spells.json') as f:
        data = json.load(f)
        # Filter the data by class
        filteredData = [spell for spell in data if class_name in spell['class']]
        # Select random spell
        randomSpell = filteredData[random.randint(0, len(filteredData) - 1)]
        # Print random spell
        return randomSpell['name']


# Print out list of all SpellClass variables
# Then take user input for class
# Return class name
def choose_class():
    print("Bard")
    print("Cleric")
    print("Druid")
    print("Paladin")
    print("Ranger")
    print("Sorcerer")
    print("Warlock")
    print("Wizard")
    print()
    class_name = input("\n" + Color.BOLD + Color.UNDERLINE + "Choose a class: " + Color.END)
    # Error handling
    while class_name not in SpellClass.__dict__.values():
        class_name = input("\n" + Color.BOLD + Color.UNDERLINE + "Choose a class: " + Color.END)

    # Return class name
    return class_name


if __name__ == '__main__':

    status = True

    # Main Loop
    while status is True:
        # Print random entry
        print('\n' + Color.BOLD + choose_spell(choose_class()) + Color.END + '\n')
        # Continue loop or break
        v = input("Another? [" + Color.GREEN + 'y' + Color.END + '/' + Color.RED + 'n' + Color.END + ']').lower()
        if v == 'n':
            break
        if v == 'y':
            continue
