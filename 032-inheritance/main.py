from creatures import Animal, Cat, Dog, Spider, Human

annie = Animal("Annie", legs=1000)
annie.summarize()
annie.announce_cry()

nermyl = Cat("Nermyl")
nermyl.summarize()
nermyl.announce_cry()

zoe = Dog("Zoe")
zoe.summarize()
zoe.announce_cry()

chester = Dog("Chester", yips=False)
chester.summarize()
chester.announce_cry()

maren = Spider("Maren")
maren.summarize()
maren.announce_cry()

widow = Spider("Widow", poisonous=True)
widow.summarize()
widow.announce_cry()

bob = Human("Bob")
bob.summarize()
bob.announce_cry()

morgana = Human("Morgana", job="Witch")
morgana.summarize()
morgana.announce_cry()
