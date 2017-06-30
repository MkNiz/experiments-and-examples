def generate_dog():
    """Asks user for dog's name, and returns a dictionary representing the dog"""
    dog_name = input("To start with, please name your dog:\n~> ")
    print("")
    return {
        'name'      : dog_name,
        'pets'      : 0,
        'agitation' : 0,
        'condition' : 'fine'
    }

def dog_status(dog):
    """Displays the dog's status to the user"""
    print(dog['name'].upper() + ":")
    print("Has been pet " + str(dog['pets']) + " times.")
    print("Is feeling " + dog['condition'] + ".")
    print("")

def pet(dog):
    """Pets a dog, raising both the number of pets and agitation"""
    print("You give " + dog['name'].title() + " a nice pet!")
    print("")
    dog['pets'] = dog['pets'] + 1
    dog['agitation'] = dog['agitation'] + 1

def check_agitation(dog):
    """Checks the level of agitation of the dog. Returns 'critical' if dog is dying."""
    if dog['agitation'] >= 30:
        print("Unfortunately, " + dog['name'].title() + " was decimated by your affections.")
        print("")
        return 'critical'
    elif dog['agitation'] > 20:
        print(dog['name'].title() + " looks dangerously agitated.")
        print("")
        dog['condition'] = 'exasperated'
        return False
    elif dog['agitation'] > 10:
        print(dog['name'].title() + " is visibly upset.")
        print("")
        dog['condition'] = 'upset'
        return False
    elif dog['agitation'] >= 5:
        print(dog['name'].title() + " seems a bit anxious.")
        print("")
        dog['condition'] = 'anxious'
        return False
    elif dog['agitation'] >= 0:
        dog['condition'] = 'fine'
        return False
    else:
        print(dog['name'].title() + "'s fur is shiny and they seem very happy!")
        print("")
        dog['condition'] = 'excellent'
        return False

def give_break(dog):
    """Gives the dog a break, lowering their agitation level."""
    print("You give " + dog['name'].title() + " a break from pets.")
    print("")
    dog['agitation'] = dog['agitation'] - 5
    if dog['agitation'] < -5:
        dog['agitation'] = -5
