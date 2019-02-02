import morse as morse
import sys
import time

def slowType(text):
    for c in text + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def morseInput():
    goodChoice = False
    while not goodChoice:
        if not goodChoice:
            print('''Enter your message in Morse.
            >>> ''', end = '')
            buffer = input()
            buffer = morse.decodeMorse(buffer)
        if "<CNF>" in buffer:
            print("\n\n\nString was not recognised, try again\n\n\n")
        else:
            return buffer

def proceedYesNo(c):
    c = c.lower()
    if c in {"yes", "y"}:
        print("Good.")
        return True
    else:
        if c in {"no", "n", "quit", "exit"}:
            print("You wish.")
            exit()
        else:
            print("Input not recognised")
hasCable = False
def roomExplore():
    keepAtIt = True
    while keepAtIt:
        c = input()
        c = c.lower()
        if c in {"quit","exit"}:
            print("You wish.")
            break
        elif c in {"look around", "look", "explore"}:
            slowType("The room is dark, the only light source seems to be the old computer screen sitting on a desk and the pale moonlight coming through a window in front of you. You can hear some crows in the distance.")
            slowType("Your friends are all tired from the other decoding done and would really want to go home and rest.")
            slowType("There seems to be some some server racks in the back of the room, as well as an empty vending machine.")
        elif c in {"look at server", "look at servers", "look at server racks", "look at racks", "look at rack", "go to server", "go to servers"}:
            slowType("Some old servers, seemed to be used for teaching classes, none appear to be online, surely no one will miss a cable...")
        elif c in {"take cable","take the cable"}:
            slowType("Which cable?")
        elif c in {"take ethernet cable", "take the ethernet cable"}:
            hasCable = True
            slowType("You got the ethernet cable.")
        elif c in {"connect to internet"}:
            slowType("There's no connection to the internet.")
        elif c in {"hint", "hints", "help"}:
            slowType("      Not used to text adventures huh? You might want to look around. Use verbes and nouns")
        elif c in {"plug the cable", "plug the ethernet cable", "plug cable", "plug ethernet cable", "plug in computer"}:
            if hasCable:
                slowType("You plug the ethernet cable into the old computer.")
                slowType("        Good, good, there should be a router behind the desk.")
                slowType("You plug the other end into the dusty router.")
                keepAtIt = False
            else:
                slowType("You don't have a cable to plug in.")
        else:
            print("Input not recognised")
    