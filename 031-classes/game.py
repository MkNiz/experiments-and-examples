import random
from adventurer import Adventurer

random.seed()

jobs = [
    {
        'name': 'Nomad',
        'reqs': {}
    },
    {
        'name': 'Warrior',
        'reqs': { 'str': 13, 'dex': 8, 'con': 12 }
    },
    {
        'name': 'Thief',
        'reqs': { 'str': 7, 'dex': 15 }
    },
    {
        'name': 'Mage',
        'reqs': { 'int': 16 }
    },
    {
        'name': 'Priest',
        'reqs': { 'int': 13, 'con': 13 }
    }
]

def welcome():
    """Introduces the player to the party builder"""
    print("Welcome to the CYBEReris party builder!")
    print("Please input your command. Input 'help' for a list of available commands.")
    print("")

def bye():
    """Says goodbye to the player"""
    print("Goodbye!")

def invalid(command):
    """Communicates that a command was invalid"""
    print("Invalid command: '" + command + "'")
    print("")

def help():
    """Prints the game's commands"""
    print("--Commands")
    print("help    - Brings up this command list or contextual help")
    print("add     - Add a new adventurer to the party")
    print("remove  - Remove an adventurer from the party")
    print("status  - View the party's statistics")
    print("details - View an individual party member's statistics")
    print("greet   - Greet a party member")
    print("quit    - Exits to console")
    print("")

def roll():
    """Rolls stats for an adventurer"""
    stats = {}
    while True:
        stats = {
            'str': random.randint(5, 20),
            'dex': random.randint(5, 20),
            'int': random.randint(5, 20),
            'con': random.randint(5, 20)
        }
        print("STR: " + str(stats['str']))
        print("DEX: " + str(stats['dex']))
        print("INT: " + str(stats['int']))
        print("CON: " + str(stats['con']))
        print("")
        confirm = input("Are these values alright? (y/n)\n~> ")
        if confirm == 'yes' or confirm == 'y':
            break
    return stats

def valid_jobs(stats):
    """Returns a list of valid jobs given the provided stats"""
    good_jobs = []
    for job in jobs:
        good = True
        for stat, req in job['reqs'].items():
            if stats[stat] < req:
                good = False
        if good:
            good_jobs.append(job['name'])
    return good_jobs

def choose_job(job_list):
    """Allows the player to choose a job provided the given list"""
    chosen_job = ''
    while True:
        print("Available Jobs:")
        print("")
        for idx, job in enumerate(job_list):
            print(str(idx+1) + ".) " + job)
        print("")

        selection = input("Please select a job by referencing it by number:\n~> ")
        if selection.isnumeric() and int(selection) <= len(job_list):
            chosen_job = job_list[int(selection) - 1]
            print("You have chosen the job of '" + chosen_job + "'.")
            print("")
            break
        else:
            print("Invalid selection, please try again")
    return chosen_job

def add(party):
    """Adds a party member"""
    while True:
        stats = roll()
        job = choose_job(valid_jobs(stats))
        name = input("What would you like this adventurer to be called?\n~> ")

        char = Adventurer(name, job, stats)
        char.print_status()
        confirm = input("Is this acceptable? (y/n)(cancel or quit to go back to main menu)\n~> ")
        if confirm == "y" or confirm == "yes":
            print(name + " was added to the party.")
            print("")
            party.append(char)
            break
        elif confirm == "cancel" or confirm == "quit":
            print("Cancelled")
            break

def party_status(party):
    """Displays the status of the party"""
    if len(party) == 0:
        print("There are no party members.")
        print("")
    else:
        for idx, member in enumerate(party):
            print(str(idx+1) + ".) " + member.one_line_summary())
        print("")

def select_member(party):
    """Returns the index of a member of the party the user selects"""
    member_index = None
    while True:
        party_status(party)
        selection = input("Select a member by referencing it by number(cancel or quit to go back):\n~> ")
        if selection.isnumeric() and int(selection) <= len(party):
            member_index = int(selection) - 1
            break
        elif selection == "cancel" or selection == "quit":
            print("Cancelled")
            print("")
            break
        else:
            print("Invalid selection, please try again")
    return member_index

def remove(party):
    """Allows the player to remove a party member"""
    selected_index = select_member(party)
    if selected_index is not None:
        print(party[selected_index].name + " was removed from the party.")
        print("")
        del party[selected_index]

def details(party):
    """Allows the player to view the details of different party members"""
    selected_index = select_member(party)
    if selected_index is not None:
        party[selected_index].print_status()

def greet(party):
    """Allows the player to select a party member to greet"""
    selected_index = select_member(party)
    if selected_index is not None:
        party[selected_index].greet()
