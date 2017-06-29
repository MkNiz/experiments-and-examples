forbidden_numbers = [7, 13, 26]

current_number = 1
number_of_numbers = 0

print("These numbers are forbidden:")
print(forbidden_numbers)
print("")

while current_number <= 30:
    if current_number in forbidden_numbers:
        current_number = current_number + 1
        continue
    print(str(current_number) + " is one of the permitted numbers.")
    current_number = current_number + 1
    number_of_numbers = number_of_numbers + 1

print("")
print("In total, there are " + str(number_of_numbers) + " permitted numbers.")
