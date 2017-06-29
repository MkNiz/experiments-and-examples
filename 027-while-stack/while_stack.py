queue = [
    { 'name': "Billy", 'password': "I don't know" },
    { 'name': "Bort", 'password': "swordfish" },
    { 'name': "Leia", 'password': "SWORDFISH" },
    { 'name': "Tabitha", 'password': "squishy baby" },
    { 'name': "Mr. Snrub", 'password': "smithers" },
]

club_members = []

print("It's a party at the club!")

while queue:
    queue_leader = queue.pop()
    print(queue_leader['name'] + " attempts to get past the bouncer...")
    print("")
    print("BOUNCER: What's the password?")
    print(queue_leader['name'].upper() + ": " + queue_leader['password'] + "!")
    if queue_leader['password'].lower() == 'swordfish':
        print("BOUNCER: Alright, you can pass. Next!")
        club_members.append(queue_leader)
    else:
        print("BOUNCER: Get outta here. Next!")
    print("")

print("The queue of aspiring club members has dispersed.")
print("")
print("In the end, " + str(len(club_members)) + " party animals made it in:")
for member in club_members:
    print(member['name'])
