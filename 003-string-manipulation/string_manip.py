my_string = "squishy baby"

print("With each word capitalized using .title():")
print(my_string.title())
print("---")

print("With all letters uppercase:")
print(my_string.upper())
print("---")

print("With all letters lowercase:")
print(my_string.lower())
print("---")

my_string_2 = "rub a tummy!"

print("Concatenated with a second string variable:")
print(my_string.title() + ", " + my_string_2.title())
print("---")

print("Concatenated with a second string variable, with a tab and newline:")
print(my_string.title() + ": \n\t" + my_string_2.title())
print("---")

my_string_3 = "   " + my_string.title() + ", " + my_string_2.title() + "   "

print("Variable has right-most whitespace stripped:")
print(my_string_3.rstrip())
print("---")

print("Variable has left-most whitespace stripped:")
print(my_string_3.lstrip())
print("---")

print("Variable has whitespace on both sides stripped:")
print(my_string_3.strip())
