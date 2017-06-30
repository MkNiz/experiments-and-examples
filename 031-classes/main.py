import game

game.welcome()
party = []

while True:
    print("Command?")
    command = input("~> ")
    if command == "help":
        game.help()
    elif command == "add":
        if len(party) < 6:
            game.add(party)
        else:
            print("A party cannot consist of more than 6 members.")
            print("")
    elif command == "remove":
        if len(party) != 0:
            game.remove(party)
        else:
            print("There are no party members to remove.")
            print("")
    elif command == "details":
        if len(party) != 0:
            game.details(party)
        else:
            print("There are no party members to inspect.")
            print("")
    elif command == "status":
        game.party_status(party)
    elif command == "greet":
        if len(party) != 0:
            game.greet(party)
        else:
            print("There are no party members to remove.")
            print("")
    elif command == "quit":
        game.bye()
        break
    else:
        game.invalid(command)
