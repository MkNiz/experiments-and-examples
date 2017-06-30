class Animal():
    """A generic animal"""
    def __init__(self, name, legs=4):
        self.species = "creature"
        self.name = name
        self.legs = legs

    def cry(self):
        print("Aaaaaaaaaaa")

    def announce_cry(self):
        print("Hear my cry:")
        self.cry()
        print("")

    def summarize(self):
        print(self.name.upper() + ": I am a " + self.species + " with " + str(self.legs) + " legs.")

class Cat(Animal):
    """A kitty cat"""
    def __init__(self, name):
        super().__init__(name, legs=4)
        self.species = "cat"
        self.lives = 9

    def cry(self):
        print("Mew~")

    def summarize(self):
        super().summarize()
        print("I have " + str(self.lives) + " lives." )

class Dog(Animal):
    """A powerful pupper"""
    def __init__(self, name, yips=True):
        super().__init__(name, legs=4)
        self.species = "dog"
        self.yips = yips

    def cry(self):
        if self.yips:
            print("Yip yip!")
        else:
            print("Weff!")

class Spider(Animal):
    """A spoopy spider"""
    def __init__(self, name, poisonous=False):
        super().__init__(name, legs=8)
        self.species = "spider"
        self.poisonous = poisonous

    def summarize(self):
        super().summarize()
        if self.poisonous:
            print("Look out! I'm poisonous.")

class Human(Animal):
    """A hooman bean"""
    def __init__(self, name, job="Unemployed"):
        super().__init__(name, legs=2)
        self.species = "human"
        self.job = job

    def cry(self):
        super().cry()
        print("MY NAME IS " + self.name.upper() + "!!!!!")
        super().cry()

    def summarize(self):
        super().summarize()
        print("My job is: " + self.job)
