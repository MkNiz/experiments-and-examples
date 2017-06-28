print("Printing numbers in a range from 6 to 9:")
for val in range(6, 9):
    print(val)
print("---")

print("Creating a list from a range and displaying it:")
my_list = list(range(1,9))
print(my_list)
print("---")

print("Creating a list that skips every 4th number:")
my_list_2 = list(range(1,16,4))
print(my_list_2)
print("---")

print("Creating a list consisting of each number in a range multiplied by 12:")
my_list_3 = []
for val in range(1,11):
    my_list_3.append(val * 12)
print(my_list_3)
print("---")
