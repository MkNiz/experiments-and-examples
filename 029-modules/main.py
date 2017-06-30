import game
from do_print import print_introduction as printro
from do_print import print_dog_greeting, print_help, print_disappointment, print_valediction

printro()

dog = game.generate_dog()
dog_name = dog['name'].title()

print_dog_greeting(dog_name)

running = True

while running:
    command = input("~> ")
    if command == 'help':
        print_help()
    elif command == 'status':
        game.dog_status(dog)
    elif command == 'pet':
        game.pet(dog)
        dog_state = game.check_agitation(dog)
        if dog_state == 'critical':
            break
    elif command == 'break':
        game.give_break(dog)
        dog_state = game.check_agitation(dog)
        if dog_state == 'critical':
            break
    elif command == 'quit':
        print("")
        running = False
    else:
        print_disappointment(dog_name)

print_valediction(dog_name)
