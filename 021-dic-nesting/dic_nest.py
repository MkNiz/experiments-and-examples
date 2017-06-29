boys = [
    { 'name': 'bort', 'status': 'powerful'},
    { 'name': 'sam', 'status': 'deadly'},
    { 'name': 'sassafrass', 'status': 'overwhelmingly strong'}
]

print("Assuming the list of boys:")
print(boys)
print("")

print("Iterate through the list of dictionaries:")
for boy in boys:
    print(boy['name'].title() + " is " + boy['status'].upper() + "!!")
print("---")

main_character = {
    'name': 'quackenbush',
    'stats': {
        'strength'    : 16,
        'dexterity'   : 12,
        'intelligence': 19,
        'constitution': 8
    },
    'inventory': [
        'bucket', 'rope', 'pearl hellsword'
    ]
}

print("Assuming the main character:")
print(main_character)
print("")

print("Assess their inventory:")
for item in main_character['inventory']:
    print(main_character['name'].title() + " has a " + item.title() + ".")
print("")

print("Describe their statistics:")
print(main_character['name'].upper() + ":")
for stat, value in main_character['stats'].items():
    print(stat.title() + ": " + str(value))
print("")

print("Character needs to pass an inventory check to continue:")
print("")
print("An empty elevator shaft is in front of you. If you have a rope, you may proceed.")
if 'rope' in main_character['inventory']:
    print(main_character['name'].title() + " ties and lowers a rope, then climbs down the shaft.")
else:
    print("You cannot proceed without a rope.")
print("")

print("Character needs to pass a stat check to continue:")
print("")
print("A heavy boulder is in your path. With enough strength, you could move it.")
if main_character['stats']['strength'] >= 20:
    print(main_character['name'].title() + " punches the boulder, grinding it into a fine powder.")
else:
    print(main_character['name'].title() + " punches the boulder, grinding their knuckles into a fine powder. Take 5 damage.")
