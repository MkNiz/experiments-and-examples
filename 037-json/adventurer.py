import math

class Adventurer():
    """The class for a noble adventurer"""

    def __init__(self, name, job, stats):
        """Initialize the adventurer's base statistics"""
        self.name = name
        self.job = job
        self.str = stats['str']
        self.dex = stats['dex']
        self.int = stats['int']
        self.con = stats['con']
        self.level = 1
        self.max_hp = self.set_hp_max()
        self.hp = self.max_hp
        self.max_mp = self.set_mp_max()
        self.mp = self.max_mp

    def set_hp_max(self):
        """Uses a formula to determine an adventurer's max HP total"""
        hp_max = math.ceil(5 + ((self.con + self.level) / 1.75))
        if self.job == 'Warrior':
            hp_max = hp_max + (self.level * 2) + 8
        return hp_max

    def set_mp_max(self):
        """Uses a formula to determine an adventurer's max MP total"""
        mp_max = math.ceil(5 + ((self.int + self.level) / 1.75))
        if self.job == 'Mage':
            mp_max = mp_max + (self.level * 2) + 5
        return mp_max

    def print_status(self):
        """Prints the adventurer's current status"""
        print("---")
        print("NAME : " + self.name)
        print("JOB  : " + self.job)
        print("LEVEL: " + str(self.level))
        print("---")
        print("HP   : " + str(self.hp) + " / " + str(self.max_hp))
        print("MP   : " + str(self.mp) + " / " + str(self.max_mp))
        print(" STR : " + str(self.str))
        print(" DEX : " + str(self.dex))
        print(" INT : " + str(self.int))
        print(" CON : " + str(self.con))
        print("---")

    def one_line_summary(self):
        """Returns a string representing a one-line summary of this adventurer"""
        return self.name + " - Lv. " + str(self.level) + " " + self.job

    def greet(self):
        """Hails the player with a different string depending on own class"""
        greeting = self.name.upper() + ": "
        if self.job == 'Nomad':
            greeting = greeting + "H...hi..."
        elif self.job == 'Warrior':
            greeting = greeting + "Hail!"
        elif self.job == 'Thief':
            greeting = greeting + "What's cracking, guvna?"
        elif self.job == 'Mage':
            greeting = greeting + "Greetings, mortal."
        elif self.job == 'Priest':
            greeting = greeting + "Blessings be unto you, my child."
        print(greeting)
        print("")
