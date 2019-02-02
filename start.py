import time
import random
from random import randint
import choices as chSelector
import morseDecrypt as morse
print ("\n"*30)
print ("########################################")
print ("## [An ENUCS Night at the Quackathon] ##")
print ("########################################")
print ("\n" *5)

print ("You have been invited as part of the ENUCS team to the annual Quackathon.")
#time.sleep(1)
print ("Everyone seems to have a jolly good time. The labs are filled with people working on their submissions. ")
#time.sleep(1)
print ("...")
#time.sleep(1)
print ("But there is someting that is bugging you...it's hard to tell what")
#time.sleep(1)
print ("As the night settles in, the organisers keep stressing how important it is to not go through corridor 2A.")
print ("You feel like they are hiding something.\n")
print ("You take your team along to investigate.")
print ("The corridor is dimly lit, closed doors on both sides, they seem locked.")
#time.sleep(1)
print ("...")
print ("But one room is opened\n")
print ("You enter the room. Inside the room there is a lone laptop. The edges are scratched and the screen has a burn-in, it seems like it's seen a lot.\n")
print ("A terminal screen is opened on the laptop, a message is flashing on the screen:")
print ("Press enter to continue......")
input()
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"*4)
print('''Enter your message in Morse.
Notice that:
    1- Use / to separate the letters and space to separate words.
    2- Your message must contain only letters and numbers.
    3- '?' in output means that your input was unknowed.
    >>> ''', end = '')
buffer = input()
print ("Input was: %s" % ("".join(morse.decode(buffer))))
