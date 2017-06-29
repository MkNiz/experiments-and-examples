jewels = input("How many jewels do you have?\n~> ")
jewels = int(jewels)
if jewels < 3:
    print("You have less than 3 jewels? Begone.")
else:
    print(str(jewels) + " jewels? Please, go right through.")
