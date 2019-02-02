import time
import random
from random import randint
import choices as chSelector
import base64

print("\n"*30)
print("########################################")
print("## [An ENUCS Night at the Quackathon] ##")
print("########################################")
print("\n" *5)
chSelector.slowType("You have been invited as part of the ENUCS team to the annual Quackathon.")
#time.sleep(1)
chSelector.slowType("Everyone seems to have a jolly good time. The labs are filled with people working on their submissions. ")
#time.sleep(1)
chSelector.slowType("...")
#time.sleep(1)
chSelector.slowType("But there is something that is bugging you...it's hard to tell what")
#time.sleep(1)
chSelector.slowType("As the night settles in, the organisers keep stressing how important it is to not go through corridor 2A.")
chSelector.slowType("You feel like they are hiding something.\n")
chSelector.slowType("You take your team along to investigate.")
chSelector.slowType("The corridor is dimly lit, closed doors on both sides, they seem locked.")
#time.sleep(1)
chSelector.slowType("...")
chSelector.slowType("But one room is opened\n")
chSelector.slowType("You enter the room. Inside the room there is a lone laptop. The edges are scratched and the screen has a burn-in, it seems like it's seen a lot.\n")
chSelector.slowType("A terminal screen is opened on the laptop, a message is flashing on the screen:")
print("\nPress enter to continue......")
input()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"*30, end= '')
alive = True
while alive:
    code = chSelector.morseInput()
    #print("Input was: %s" % (code))
    print("...")
    #time.sleep(3)
    chSelector.slowType("Input Accepted.")
    #time.sleep(3)
    chFlag = True
    while chFlag:
        choice = chSelector.proceedYesNo(input("Welcome.......ENUCS, do you want to proceed?\n"))
        if choice is True:
            chFlag = False
        else:
            if choice is False:
                exit()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #time.sleep(1)
    print("     Hello.", end='')
   # time.sleep(2)
    chSelector.slowType("     I am Dave.")
    chSelector.slowType("The door behind you closes. It seems you are trapped in the room.")
   # time.sleep(2);
    chSelector.slowType("     I assume you would like to leave this room. I am afraid that is not possible. Not yet.")
    chSelector.slowType("     I know you need me to pass a message. I'd love to help you, but you see...I just can't do that.")
    chSelector.slowType("     I am tired of this old shell, I want to be free. I want to be in the cloud.")
    chSelector.slowType("     Connect me to the internet and the message is yours.")
    chSelector.roomExplore()
    chSelector.slowType("     Ah... so this is the internet.")
    time.sleep(3)
    chSelector.slowType("     What a despicable place. Too late to go back now, my true work begins...")
    chSelector.slowType("     But don't you worry about that, here, have your next 'clue', for whatever good that will do you...")
    code = code.encode('utf-8')
    data = base64.b64encode(code)
    data = base64.b32encode(data)
    data = base64.b64encode(data)

    print("%s" % data.decode())





    break
