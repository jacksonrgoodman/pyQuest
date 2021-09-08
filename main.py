import os
import random
import math
import time
from pprint import pprint


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ? Hero
# * Class of the player. The stats.


class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    # ? Getters
    # * How we can get the value of a statistic we are trying to change.

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getLuck(self):
        return self.luck

    def getRanged(self):
        return self.ranged

    def getDefence(self):
        return self.defence

    def getMagic(self):
        return self.magic

    def getName(self):
        return self.name

    # ? Setters
    # * How we can set the value of a statistic we are trying to change.

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setLuck(self, newLuck):
        self.luck = newLuck

    def setRanged(self, newRanged):
        self.ranged = newRanged

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setMagic(self, newMagic):
        self.magic = newMagic

    def setName(self, newName):
        self.name = newName


# ? Enemy
# * Class of the generic enemy. The stats.

class enemy:
    # ? On initialize
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename

    # ? Getters
    # * How we can get the value of a statistic we are trying to change.

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.chance

    def getName(self):
        return self.name

    # ? Setters
    # * How we can set the value of a statistic we are trying to change.

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setSpecial(self, newSpecial):
        self.special = newSpecial

    def setChance(self, newChance):
        self.chance = newChance

    def setName(self, newName):
        self.name = newName

# ? Boss
# * Inherits properties from Enemy


class boss (enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)

        self.superMove = EsuperMove

    def getSuper(self):
        return self.superMove

    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

# ? Enemy Generation
# * Generates a random generic enemy, taking in the boolean for whether or not a levelBoss is generated.


def enemyGen(levelBoss):
    temp = []
    # * opens the adjectives.txt file read only
    file = open("adjectives.txt", "r")
    lines = file.readlines()
    # * pick random adjective from lines
    adjective = lines[random.randint(0, len(lines)-1)][:-1]
    # * closes adjectives.txt
    file.close
    # * opens the enemies.txt file, read only
    file = open("enemies.txt", "r")
    lines = file.readlines()
    # * pick random name from lines
    enemyName = lines[random.randint(0, len(lines)-1)][:-1]
    # * closes enemies.txt
    file.close

    if levelBoss == False:
        # ? if is not a levelBoss
        health = random.randint(50, 100)
        attack = random.randint(1, 10)
        chance = random.randint(1, 10)
        special = random.randint(10, 20)

        return enemy(health, attack, special, chance, adjective+" "+enemyName)
    else:
        # ? if is a levelBoss
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        chance = random.randint(1, 8)
        special = random.randint(50, 60)
        superMove = random.randint(100, 200)
        return boss(health, attack, special, chance, adjective+" "+enemyName, superMove)

# ? Enemy Attack
# * Generates an enemy, tqaking in the boolean for whether or not a levelBoss is generated.


def enemyAttack(hitChance, attackValue, name, defence):
    print(name, "strikes out!")
    hit = random.randint(0, 10)
    if hitChance >= hit:
        print(name, "'s attack lands!!!")
        loss = attackValue - defence
        print("You stagger, losing", loss, "HP.")
        return math.ceil(loss)
    else:
        print("The enemy misses.")
        return 0

# ? Hit Chance
# * Checks if a stat


def hitChance(luck):
    hit = random.randint(0, 4)
    if luck < hit:
        print("You Missed!")
        return False
    else:
        print("You hit the enemy!")
        return True

# ? Is dead
# * checks if something is dead


def isDead(health):
    if health < 1:
        return True
    else:
        return False

# ? Loot
# * takes character, character's luck


def loot(luck, genCharacter):
    # * chance to loot
    lootChance = random.randint(0, 4)
    if luck < lootChance:
        print("The enemy had no items.")
        input()
    else:
        tableNum = random.randint(0, 4)
        lootTableList = ["items", "ranged", "defence", "magic", "attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType+".txt", "r")
        lines = file.readlines()

        print("...")

        item = random.randint(0, len(lines)-1)

        itemLine = lines[item]

        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])
        print("The enemy dropped a", name, ".")
        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack()+value)
            print("Your new Attack is...")
            print(genCharacter.getAttack())
            input()
        elif itemType == "ranged":
            genCharacter.setRanged(genCharacter.getRanged()+value)
            print("Your new Ranged Attack is...")
            print(genCharacter.getRanged())
            input()
        elif itemType == "defence":
            genCharacter.setDefence(genCharacter.getDefence()+value)
            print("Your new Defence is...")
            print(genCharacter.getDefence())
            input()
        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic()+value)
            print("Your new Magic Attack is...")
            print(genCharacter.getMagic())
            input()
        else:
            if splitItemLine[2] == "luck":
                genCharacter.setLuck(genCharacter.getLuck()+value)
                print("Your new Luck is...")
                print(genCharacter.getLuck())
                input()
            elif splitItemLine[2] == "health":
                genCharacter.setHealth(genCharacter.getHealth()+value)
                print("Your new Health is...")
                print(genCharacter.getHealth())
                input()

# ? Game Over
# * How the game ends


def gameOver(enemyDead):
    if enemyDead == True:
        print("You are victorius!")
        input()
    else:
        print("You have died!")
        print("BetterLuck Next Time!")
        exit()

# ? Battle
# * Battle Dialogue


def battle(genEnemy, genCharacter):
    print("Fight Start")
    print("Enemy: ", genEnemy.getName())
    pprint(vars(genEnemy))
    battle = True
    while battle == True:

        print("1. SWORD ATTACK\n2. RANGED ATTACK\n3. MAGIC ATTACK")
        choice = input()

        while choice != "1" and choice != "2" and choice != "3":
            print("Invalid Command.")
            print("1. SWORD ATTACK\n2. RANGED ATTACK\n3. MAGIC ATTACK")
            choice = input()
        if choice == "1":
            damage = genCharacter.getAttack()
        elif choice == "2":
            damage = genCharacter.getRanged()
        else:
            damage = genCharacter.getMagic()
        print("You hurl your attack!")
        hit = hitChance(genCharacter.getLuck())
        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print("Your attack has landed!")
            print("Your deal", damage, "damage!")
            print(genEnemy.getName(), "now has", genEnemy.getHealth(), "HP.")
            input()
        else:
            print("Your attack missed!")
            input()
        enemyDead = isDead(genEnemy.getHealth())
        if enemyDead == False:
            genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(
            ), genEnemy.getAttack(), genEnemy.getName(), genCharacter.getDefence()))

            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False
            else:
                print("Your character's remaining health is",
                      genCharacter.getHealth(), "HP.")
                input()
        else:
            battle = False
            print("You have defeated", genEnemy.getName(), "!")
            input()
            print("You check", genEnemy.getName(), "for any items.")

            loot(genCharacter.getLuck(), genCharacter)

            return True

# Game Title


def gameTitle():
    print("                _______________________________________________________________________________")
    print("              / \                                                                              \.")
    print("              |  |                                                                             |.")
    print("               \_|               ████████▄   ███    █▄     ▄████████    ▄████████     ███      |.")
    print("                 |              ███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄   |.")
    print("                 |              ███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██   |.")
    print("                 |              ███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀   |.")
    print("                 |     ___ _ _  ███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███       |.")
    print("                 |    | . | | | ███    ███  ███    ███   ███    █▄           ███     ███       |.")
    print("                 |    |  _|_  | ███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███       |.")
    print("                 |    |_| |___| ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀      |.")
    print("                 |   __________________________________________________________________________|___")
    print("                 |  /                                                                             /.")
    print("                 \_/_____________________________________________________________________________/.")


def splash():
    print("                           .,,uod8B8bou,,.")
    print("              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.")
    print("         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||")
    print("         !...:!TVBBBRPFT||||||||||!!^^""'     ||||")
    print("         !.......:!?|||||!!^^""'              ||||")
    print("         !.........||||                     ||||")
    print("         !.........||||      Jackson's      ||||")
    print("         !.........||||                     ||||")
    print("         !.........||||          CLI        ||||")
    print("         !.........||||                     ||||")
    print("         !.........||||         Games       ||||")
    print("         `.........||||,                    ||||")
    print("          .;.......||||               _.-!!|||||")
    print("   .,uodWBBBBb.....||||        _.-!!|||||||||!:'")
    print("!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....")
    print("!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.")
    print("!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.")
    print("!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^:`;:::       .")
    print("!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.")
    print("`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.")
    print("  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'")
    print("    `........::::::::::::::::;iof688888888888888888888b.     `")
    print("      `......:::::::::;iof688888888888888888888888888888b.")
    print("        `....:::;iof688888888888888888888888888888888899fT!")
    print("          `..::!8888888888888888888888888888888899fT|!^*'")
    print("            `' !!988888888888888888888888899fT|!^*'")
    print("                `!!8888888888888888899fT|!^*'")
    print("                  `!988888888899fT|!^*'")
    print("                    `!9899fT|!^*'")
    print("                      `!^*'")
    # ? Geme Generation
    # * Creating the Game.


levelBoss = False
clear()
splash()
time.sleep(2)
clear()
gameTitle()
print()
print()
print('Press any key to start the game. Enter "Exit" to exit.', end="\n \n")
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


def createClass():
    a = input("ARE YOU A(1) OR B(2)?...")
    while a != "1" and a != "2":
        print("Invalid Selection")
        a = input("ARE YOU A(1) OR B(2)?...")

    if a == "1":
        heroAttack = 50
        heroDefence = 100

    elif a == "2":
        heroAttack = 100
        heroDefence = 50

    b = input("Roll the Dice")
    time.sleep(0.2)
    print("rolling dice...")
    heroLuck = random.randint(0, 10)
    print("Your hero has", heroLuck, "luck out of 10")

    c = input("are You C(3) Or D(4)")
    while c != "3" and c != "4":
        print("Invalid Selection")
        c = input("are You C(3) Or D(4)")
    if c == "3":
        heroRanged = 100
        heroMagic = 50
    elif c == "4":
        heroRanged = 50
        heroMagic = 100

    heroName = input("What is your name?")
    print("Welcome", heroName, "!")
    return(heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName)


class_data = createClass()

character = hero(100, class_data[0], class_data[1],
                 class_data[2], class_data[3], class_data[4], class_data[5])
print(class_data)
pprint(vars(character))
