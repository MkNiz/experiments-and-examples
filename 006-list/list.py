my_list = ['first item', 'second item', 'third item', 'last item']

print("Full printout of list:")
print(my_list)
print("---")

print("First list item:")
print(my_list[0])
print("---")

print("Second list item:")
print(my_list[1])
print("---")

print("Third list item:")
print(my_list[2])
print("---")

print("Last list item, using -1 index:")
print(my_list[-1])
print("---")

print("Before changing the first item to Bepis:")
print(my_list)
print("After changing the first item to Bepis:")
my_list[0] = 'Bepis'
print(my_list)
print("---")

print("Before appending a new item to the list:")
print(my_list)
print("After appending a new item to the list:")
my_list.append('TRUE last item')
print(my_list)
print("---")

print("Before inserting a new item to the list:")
print(my_list)
print("After inserting a new item to the list:")
my_list.insert(3, 'fourth item')
print(my_list)
print("---")

print("Before removing the fourth item in the list:")
print(my_list)
print("After removing the fourth item in the list:")
del my_list[3]
print(my_list)
print("---")

print("Before popping the last item out of the list:")
print(my_list)
print("After popping the last item out of the list:")
my_popped_item = my_list.pop()
print(my_list)
print("Item popped from the list:")
print(my_popped_item)
print("---")

print("Before removing the second item by its value:")
print(my_list)
print("After removing the second item by its value:")
my_list.remove('second item')
print(my_list)
