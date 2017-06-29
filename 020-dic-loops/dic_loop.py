boy_status = {
    'zach': 'zesty',
    'clint': 'wild',
    'beavis': 'heh',
    'bort': 'wacky',
    'sam': 'trusty'
}

print('With the following dictionary:')
print(boy_status)
print("")

print("Loop through and describe the status of each boy:")
for boy, status in boy_status.items():
    print(boy.title() + " is feelin' " + status + "!!!")
print("")

print("Again, but this time sorted:")
for boy, status in sorted(boy_status.items()):
    print(boy.title() + " is feelin' " + status + "!!!")
print("")

print("Loop through each key without its value:")
for boy in boy_status.keys():
    print(boy.title() + " is our sweet boy")
print("")

print("Same, but without using .keys():")
for boy in boy_status:
    print(boy.title() + " is a fine upstanding boy")
print("")

print("Loop through each value without its key:")
for status in boy_status.values():
    print("There's a boy who is positively " + status + "!")
print("---")

good_boys = ['clint', 'bort']

print("Assuming this list of good boys:")
print(good_boys)
print("")

print("Determine which boys are good and which are nasty:")
for boy, status in boy_status.items():
    if boy in good_boys:
        print(boy.title() + " is a good, " + status + " fella")
    else:
        print(boy.title() + " is a NASTY " + status.upper() + " FILTHY BOY")
print("---")

print("If another boy is added who is also zesty:")
boy_status['danny'] = 'zesty'
print(boy_status)
print("")

print("Looping through each value will repeat 'zesty':")
for status in boy_status.values():
    print("At least one of your boys is " + status + "!")
print("")

print("If the list of values is converted to a set, however, only unique values are iterated:")
for status in set(boy_status.values()):
    print("At least one of your boys is " + status + "!")
print("")
