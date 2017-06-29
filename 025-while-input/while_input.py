print("|== Dog Petter 3000 ==|")
print("|== Version: dog.12 ==|")
print("|==   by CYBEReris  ==|")
print("")

dog_name = input("To start with, please name your dog:\n~> ")
print("")
dog = {
    'name'      : dog_name,
    'pets'      : 0,
    'agitation' : 0,
    'condition' : 'fine'
}
print("Lovely dog '" + dog['name'].title() + "' has been initialized.")
print("")
print("Type 'help' for commands. Enjoy petting the dog!")

running = True

while running:
    name = dog['name'].title()
    command = input("~> ")
    if command == 'help':
        print("--- Commands:")
        print('help   - Displays this list of commands')
        print('status - Displays the status of your dog')
        print('pet    - Pets your dog')
        print('break  - Takes a break from petting your dog, giving them time to calm down')
        print('quit   - Exits to console')
        print("")
    elif command == 'status':
        print(dog['name'].upper() + ":")
        print("Has been pet " + str(dog['pets']) + " times.")
        print("Is feeling " + dog['condition'] + ".")
        print("")
    elif command == 'pet':
        print("You give " + name + " a nice pet!")
        print("")
        dog['pets'] = dog['pets'] + 1
        dog['agitation'] = dog['agitation'] + 1
        if dog['agitation'] >= 30:
            print("Unfortunately, " + name + " was decimated by your affections.")
            print("")
            running = False
        elif dog['agitation'] > 20:
            print(dog['name'].title() + " looks dangerously agitated.")
            print("")
            dog['condition'] = 'exasperated'
        elif dog['agitation'] > 10:
            print(dog['name'].title() + " is visibly upset.")
            print("")
            dog['condition'] = 'upset'
        elif dog['agitation'] >= 5:
            print(dog['name'].title() + " seems a bit anxious.")
            print("")
            dog['condition'] = 'anxious'
    elif command == 'break':
        print("You give " + name + " a break from pets.")
        print("")
        dog['agitation'] = dog['agitation'] - 5
        if dog['agitation'] < -5:
            dog['agitation'] = -5

        if dog['agitation'] < 0:
            print(name + "'s fur is shiny and they seem very happy!")
            print("")
            dog['condition'] = 'excellent'
        elif dog['agitation'] < 5:
            dog['condition'] = 'fine'
        elif dog['agitation'] <= 10:
            dog['condition'] = 'anxious'
        elif dog['agitation'] <= 20:
            dog['condition'] = 'upset'
        elif dog['agitation'] < 30:
            dog['condition'] = 'exasperated'

    elif command == 'quit':
        print("")
        running = False
    else:
        print("Command could not be understood. " + name + " is very disappointed.")
        print("")

print(dog['name'].title() + " has been destroyed. Bye " + dog['name'].title() + "!")
