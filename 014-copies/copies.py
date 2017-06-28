my_list = ["good", "bad", "ugly"]

print("Assuming the following list:")
print(my_list)
print("")

print("A copy has been made, and starts out identical:")
my_list_2 = my_list[:]
print(my_list_2)
print("")

print("If 'gross as heck' is appended to the second list:")
my_list_2.append('gross as heck')
print(my_list_2)
print("")

print("The state of the first list is not changed:")
print(my_list)
