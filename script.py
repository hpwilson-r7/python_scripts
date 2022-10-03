#!/usr/bin/env python3
# This is so stupid but it helped kill an hour
# Error when wrong input is put in

import json
import random
import textwrap


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
        chosenSpell = randomSpell['desc'].split(".")
        return Color.GREEN + randomSpell['name'] + Color.END + "\n" + textwrap.fill(
            ((chosenSpell[0]).replace("<p>", "") + ". " + chosenSpell[1] + "."), width=100)



# Print out list of all SpellClass variables
# Then take user input for class
# Return class name
def choose_class():
    print("+ " + "Bard - An inspiring magician")
    print("+ " + "Cleric - A priestly champion")
    print("+ " + "Druid - A priest of the Old Faith")
    print("+ " + "Paladin - A holy warrior")
    print("+ " + "Ranger - A warrior")
    print("+ " + "Sorcerer - A spellcaster")
    print("+ " + "Warlock - A wielder of magic")
    print("+ " + "Wizard - A scholarly magic-user")
    print()
    class_name = input(Color.BOLD + "Choose a class:" + Color.END + " ").capitalize()
    # Error handling
    while class_name not in SpellClass.__dict__.values():
        class_name = input(Color.BOLD + "Choose a class:" + Color.END + " ")

    # Return class name
    return class_name


if __name__ == '__main__':
    # Title
    print()
    title = Color.BOLD + "SOARCERER'S SPELLBOOK" + Color.END
    sparkle = Color.GREEN + "+" + Color.END + Color.RED + "=" + Color.END
    print(sparkle * int(len(title) / 2))
    print((" " * int(len(title) / 8)) + title)
    print(sparkle * int(len(title) / 2))
    print()
    status = True

    # Main Loop
    while status is True:
        # Print random entry
        print('\n' + Color.BOLD + choose_spell(choose_class()) + Color.END + '\n')
        # Continue loop or break
        v = input(
            Color.BOLD + "Choose Another?" + Color.END + " [" + Color.GREEN + 'y' + Color.END + '/' + Color.RED + 'n' + Color.END + ']' + "\n").lower()
        print()
        if v == 'n':
            print(Color.RED + Color.BOLD + "May the sprint begin!" + Color.END)
            break
        if v == 'y':
            continue
