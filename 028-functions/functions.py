def print_hello():
    """Prints Hello to the console"""
    print("Hello")

def print_with_affectation(msg):
    """Prints the passed message 'msg' with an affectation at the end"""
    print(msg + ", my friend!")

def print_multiplied(num1, num2):
    """Prints the product of 'num1' and 'num2'"""
    print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2))

def print_salutation(name='Stranger'):
    """Prints a salutation for the passed name ('Stranger' by default)"""
    print("Howdy, " + name + "!")

def return_hello():
    """Returns the string 'Hello'"""
    return "Hello"

def return_name(first, last, middle=''):
    """Returns a name string constructed from passed arguments"""
    if middle:
        return (first + " " + middle + " " + last).title()
    else:
        return (first + " " + last).title()

def return_profile(name, bio=False, age=False):
    """Returns a dictionary with the provided name and bio"""
    profile = {'name': name}
    if bio:
        profile['bio'] = bio
    if age:
        profile['age'] = age
    return profile

def shout_outs(names):
    """Prints all the names in the list 'names'"""
    for name in names:
        print("Awh yeah, it's " + name + "!")

def serve(customers):
    """Takes the last item in a list and prints out 'Now serving x'"""
    serving = customers.pop()
    print("Now serving: " + serving)
    print("Remaining customers:")
    for customer in customers:
        print(customer)
    print("")

def return_sum(*nums):
    """Returns the sum of all nums"""
    num_sum = 0
    for num in nums:
        num_sum = num_sum + num
    return num_sum

def favorite_books(name, *books):
    """Returns a dictionary with the name and their favorite books"""
    entry = {'name': name, 'favorite books': []}
    for book in books:
        entry['favorite books'].append(book)
    return entry

def user_account(name, role, **info):
    """Returns a dictionary that represents a user account"""
    account = {'name': name, 'role': role}
    for key, value in info.items():
        account[key] = value
    return account

print("Calling a basic function that says hello:")
print_hello()
print("")

print("Calling a function that takes a single argument:")
print_with_affectation("Eels")
print("")

print("Calling a function that takes multiple arguments:")
print_multiplied(5, 3)
print("")

print("Calling the same function but with keyword arguments to swap parameters:")
print_multiplied(num2=5, num1=3)
print("")

print("Calling a function that has a default parameter value with and without an argument:")
print_salutation("Billy")
print_salutation()
print("")

print("Calling a function that returns hello:")
print(return_hello())
print("")

print("Calling a function that returns a full name, with and without a middle name:")
print(return_name("miles", "prower", "'tails'"))
print(return_name("scoobert", "doobert"))
print("")

print("Calling a function that returns a dictionary of the passed arguments:")
print(return_profile("Jim"))
print(return_profile("Curly Pete", "I like to have fun, and chew gum"))
print(return_profile("Lemon", "Hello, it's Lemon", 26))
print("")

print("Calling a function that iterates through a list:")
shout_outs(["Corey", "Sara", "Chelsea", "Wheatlord"])
print("")

print("Calling a function that pops through a list as a queue multiple times:")
customers = ["Jo", "Joey", "Jolyne", "Giorno", "Joseph"]
serve(customers)
serve(customers)
serve(customers)

print("Calling a function that can receive an arbitrary number of arguments:")
print("Sum of 1: " + str(return_sum(1)))
print("Sum of 1, 3, 5: " + str(return_sum(1, 3, 5)))
print("Sum of 9000, 900, 90, 9: " + str(return_sum(9000, 900, 90, 9)))
print("")

print("Calling a function that takes both required and arbitrary arguments:")
print(favorite_books("Timothy", "The Little Engine that Could", "Shrek"))
print(favorite_books("Sally"))
print(favorite_books("Greg", "The Book Thief", "The Thief Book", "Thief: The Book"))
print("")

print("Calling a function that takes an arbitrary number of keyword arguments:")
print(user_account("Steven", "Admin", strength=16))
print(user_account("Pauline", "User"))
print(user_account("Marmaduke", "Moderator", ratings=16, home="Hell"))
