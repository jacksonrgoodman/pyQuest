import random, time, math
from pprint import pprint
from data.entities.actors import enemy, boss

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
    print(name.strip(), "strikes out!")
    hit = random.randint(0, 10)
    if hitChance >= hit:
        print("The "+ name.strip() + "'s attack lands!!!")
        loss = attackValue - defence
        print("You stagger, losing", str(loss)+ "HP.")
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
        print("The enemy dropped a", name+ ".")
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
        print("You are victorious!")
        input()
    else:
        print("You have died!")
        print("Better Luck Next Time!")
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
            print("Your deal "+ str(damage)+"HP"+ " in damage!")
            print(genEnemy.getName(), "now has "+ str(genEnemy.getHealth())+ "HP left.")
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
                      str(genCharacter.getHealth()) + "HP.")
                input()
        else:
            battle = False
            print("You have defeated "+ genEnemy.getName().strip()+ "!")
            input()
            print("You check "+ genEnemy.getName()+ " for any items.")

            loot(genCharacter.getLuck(), genCharacter)

            return True