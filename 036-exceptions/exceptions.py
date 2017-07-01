print("Using try-except blocks to 'escape' code errors:\n")

try:
    impossible = "5" + 2
except TypeError:
    print("I tried to add a string and a number and couldn't.")

try:
    division_by_zero = 42 / 0
except ZeroDivisionError:
    print("I tried to divide by zero and couldn't.")

try:
    with open('nonexistent-file.fake') as fake_file:
        print(fake_file.read())
except FileNotFoundError:
    print("I tried to read a file that didn't exist and failed.\n")

print("The code immediately following this print fails silently.\n")

try:
    5 + a_number
except NameError:
    pass

print("Using try-except blocks to 'escape' user errors:\n")

while True:
    number = input("Please provide a number to be divided in half:\n~> ")
    try:
        print((float(number) / 2))
    except ValueError:
        print("That wasn't a number, was it? Pathetic.\n")
    else:
        break
