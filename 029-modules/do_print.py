def dont_import_me():
    """This function will not be imported"""
    return "It's illegal to import me!!"

def print_introduction():
    """Prints the game introduction"""
    print("|== Dog Petter 3000 ==|")
    print("|== Version: dog.12 ==|")
    print("|==   by CYBEReris  ==|")
    print("")

def print_dog_greeting(name):
    """Affirms the dog's name and welcomes the user"""
    print("Lovely dog '" + name + "' has been initialized.")
    print("")
    print("Type 'help' for commands. Enjoy petting the dog!")

def print_help():
    """Prints the commands available to the player"""
    print("--- Commands:")
    print('help   - Displays this list of commands')
    print('status - Displays the status of your dog')
    print('pet    - Pets your dog')
    print('break  - Takes a break from petting your dog, giving them time to calm down')
    print('quit   - Exits to console')
    print("")

def print_disappointment(name):
    """Prints the dog's disappointment at not understanding your command."""
    print("Command could not be understood. " + name + " is very disappointed.")
    print("")

def print_valediction(name):
    """Prints that the dog was destroyed"""
    print(name + " has been destroyed. Bye " + name + "!")
