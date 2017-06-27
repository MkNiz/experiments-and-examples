animals = ["zebra", "coyote", "aardvark", "pig"]

print("Initial list state:")
print(animals)
print("---")

print("Permanently sorted alphabetically:")
animals.sort()
print(animals)
print("---")

print("Permanently sorted alphabetically(reverse order):")
animals.sort(reverse = True)
print(animals)
print("---")

people = ["Tim", "Jake", "Abaddon", "Dr. Ivo Robotnik"]

print("Second initial list state:")
print(people)
print("---")

print("Temporarily sorted alphabetically:")
print(sorted(people))
print("---")

print("Temporarily sorted alphabetically(reverse order):")
print(sorted(people, reverse = True))
print("---")

print("Maintained state of list:")
print(people)
print("---")

print("Reversed list order:")
people.reverse()
print(people)
print("---")

print("Length of list:")
print(len(people))
