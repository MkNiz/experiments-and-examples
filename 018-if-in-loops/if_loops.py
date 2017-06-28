inventory = ["sword", "sword", "sword", "spear", "halcyon cube", "space-time", "fake sword"]

print("State of inventory:")
print(inventory)
print("---")

print("The equipment power of your current inventory is:")
power = 0
for item in inventory:
    if item == "sword":
        power = power + 1
    elif item == "spear":
        power = power + 2
print(power)
print("---")

print("Finding the indices of all 'sword' items:")
for index, item in enumerate(inventory):
    index = str(index+1)
    if item == "sword":
        print("sword found in inventory slot " + index + "!")
    elif item == "fake sword":
        print("a fake sword is taking up space in inventory slot " + index + "!")
    else:
        print("no sword in inventory slot " + index + "!")
print("---")
