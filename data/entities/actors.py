
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