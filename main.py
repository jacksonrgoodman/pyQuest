from html import entities
import os
import random
import math
import time
from pprint import pprint
from data.entities.actors import *
from data.scripts.logic import *


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')









# ? Geme Generation
# * Creating the Game.


levelBoss = False
# clear()
# splash()
# time.sleep(2)
# clear()
# gameTitle()
# print()
# print()
pprint('Press any key to start the game. Enter "Exit" to exit.')
print(">", end="")
choice = input()
if choice == "Exit" or choice == "exit":
    clear()
    exit()
input()
clear()
# ? Conan
# * This Generates the player as Conan.
genCharacter = hero(100, 10, 11, 12, 1, 14, "Conan")
# * Prints the stats
pprint(vars(genCharacter))
print(genCharacter.name, ", you are the hero.", sep="", end="\n \n")
print(">", end="")
input()
# * Runs the Battle until someone dies
whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)
# whoDied = battle(enemyGen(levelBoss), genCharacter)
# gameOver(whoDied)
pprint(vars(genCharacter))
print("End")
input()


class_data = createClass()

character = hero(100, class_data[0], class_data[1],
                 class_data[2], class_data[3], class_data[4], class_data[5])
print(class_data)
pprint(vars(character))
