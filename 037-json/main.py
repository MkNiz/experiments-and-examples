import game
import json

game.welcome()
party = []
save_slots = game.load_from_file()

while True:
    print("Command?")
    command = input("~> ")
    if command == "help":
        game.help()
    elif command == "add":
        if len(party) < 6:
            game.add(party)
        else:
            print("A party cannot consist of more than 6 members.\n")
    elif command == "remove":
        if len(party) != 0:
            game.remove(party)
        else:
            print("There are no party members to remove.\n")
    elif command == "details":
        if len(party) != 0:
            game.details(party)
        else:
            print("There are no party members to inspect.\n")
    elif command == "status":
        game.party_status(party)
    elif command == "greet":
        if len(party) != 0:
            game.greet(party)
        else:
            print("There are no party members to remove.\n")
    elif command == "new":
        party = []
        print("Party reset.\n")
    elif command == "save":
        if len(party) == 0:
            print("You have no party to save!\n")
        else:
            game.save_party(party, save_slots)
    elif command == "load":
        party = game.load_party(party, save_slots)
    elif command == "delete":
        game.delete_save(save_slots)
    elif command == "quit":
        game.bye()
        break
    else:
        game.invalid(command)
