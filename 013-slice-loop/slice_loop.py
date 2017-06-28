visitors = ['chuckles', 'beauregard', 'johnson', 'guts', 'chester', 'a horse']

print("Assuming the following list:")
print(visitors)
print("")

print("Slice the first 3 items of the list:")
for visitor in visitors[:3]:
    print(visitor.title())
print("")

print("Slice 2 items of the list starting from the second item:")
for visitor in visitors[1:3]:
    print(visitor.title())
print("")

print("Slice all items of the list after the third item:")
for visitor in visitors[2:]:
    print(visitor.title())
print("")

print("Slice the last four items of the list:")
for visitor in visitors[-4:]:
    print(visitor.title())
