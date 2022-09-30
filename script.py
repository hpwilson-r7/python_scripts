#!/usr/bin/env python3
# Bugs include: Select sorcerer == crash
# This is so stupid but it helped kill an hour
import json
import random
import textwrap


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
        return color.GREEN + randomSpell['name'] + color.END + "\n" + textwrap.fill(randomSpell['desc'], width=100)


# Print out list of all spellClass variables
# Then take user input for class
# Return class name
def chooseClass():
    print("+ " + "Bard - An inspiring magician whose power echoes the music of creation")
    print("+ " + "Cleric - A priestly champion who wields divine magic in service of a higher power")
    print("+ " + "Druid - A priest of the Old Faith, wielding the powers of nature and adopting animal forms")
    print("+ " + "Paladin - A holy warrior bound to a sacred oath")
    print(
        "+ " + "Ranger - A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization")
    print("+ " + "Sorcerer - A spellcaster who draws on inherent magic from a gift or bloodline")
    print("+ " + "Warlock - A wielder of magic that is derived from a bargain with an extraplanar entity")
    print("+ " + "Wizard - A scholarly magic-user capable of manipulating the structures of reality")
    print()
    className = input(color.BOLD + color.UNDERLINE + "Choose a class:" + color.END + " ")
    # Error handling
    while className not in spellClass.__dict__.values():
        className = input(color.BOLD + color.UNDERLINE + "Choose a class:" + color.END + " ")

    # Return class name
    return className


if __name__ == '__main__':
    # Title
    print()
    title = color.BOLD + "SOARCERER'S SPELLBOOK" + color.END
    sparkle = color.GREEN + "+" + color.END + color.RED + "=" + color.END
    print(sparkle * int(len(title) / 2))
    print(title)
    print(sparkle * int(len(title) / 2))
    print()
    status = True

    # Main Loop
    while status == True:
        # Print random entry
        print('\n' + color.BOLD + chooseSpell(chooseClass()) + color.END + '\n')
        # Continue loop or break
        v = input(
            "Another? [" + color.GREEN + 'y' + color.END + '/' + color.RED + 'n' + color.END + ']' + "\n").lower()
        print()
        if v == 'n':
            print(color.RED + color.BOLD + "May the sprint begin!" + color.END)
            break
        if v == 'y':
            continue
