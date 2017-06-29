person = {'name': 'Jim', 'power': 70}

print("With the following person:")
print(person)
print("")

print("Their name is:")
print(person['name'])
print("")

print("Their power level is:")
print(person['power'])
print("---")

print("Adding the key 'devil buster' with the value 'True':")
person['devil buster'] = True
print(person)
print("")

print("Changing the value of 'power' to 69:")
person['power'] = 69
print(person)
print("")

print("Removing the key 'devil buster':")
del person['devil buster']
print(person)
print("---")

print("Is Jim's power level over 9000?")
if person['name'] == 'Jim' and person['power'] > 9000:
    print("Jim's power level is oVER NINE THOUSAAAAND")
elif person['name'] == 'Jim' and person['power'] <= 9000:
    print("Jim's power level is weak!!!")
else:
    print("Wait a minute, this isn't Jim!")
