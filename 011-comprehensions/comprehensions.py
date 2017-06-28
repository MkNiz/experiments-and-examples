print("Creating a list where each number from 1 to 10 is multiplied by 12:")
my_list = [val * 12 for val in range(1,11)]
print(my_list)
print("---")

print("Creating a list where each number from 10 to 20 is doubled and added to itself:")
my_list_2 = [val + (val*2) for val in range(10,21)]
print(my_list_2)
