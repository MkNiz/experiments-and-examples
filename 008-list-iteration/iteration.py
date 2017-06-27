dads = ["Brock", "Larry", "Jezza", "Daddyo"]

print("All Dads:")
for dad in dads:
    print(dad)
print("---")

print("State of Dads before granting last names:")
print(dads)
print("State of Dads after granting last names:")
for index, dad in enumerate(dads):
    dads[index] = dad + " " + dad + "son"
print(dads)
print("---")
