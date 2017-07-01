files = [
    "a_file.txt",
    "subdirectory/another_file.txt",
    "subdirectory/append_file.txt"
]

print("Writing to a file in the current directory...")
print("")

with open(files[0], 'w') as my_file:
    my_file.write("This is a file written to by Python")

print("Writing to a file in a subdirectory...")
print("")

with open(files[1], 'w') as my_file:
    my_file.write("This is a second file written to by Python")

print("Writing to an existing file in a subdirectory using append mode...")
print("")

with open(files[2], 'a') as my_file:
    my_file.write("This line was appended. There are as many duplicate lines as times this script has been run.\n")

print("---")
print("State of each file:")
print("")

for idx, a_file in enumerate(files):
    print(str(idx+1) + ".) " + a_file + ":")
    print("")
    with open(a_file) as my_file:
        print(my_file.read())
    print("")
