print("Reading text file in directory:")
print("")

with open('a_text_file.txt') as text_file:
    print(text_file.read())

print("Reading text file in subdirectory:")
print("")

with open('a-subdirectory/another_text_file.txt') as another_text_file:
    print(another_text_file.read())

print("Reading text file line by line, interjecting with 'weff' after each line:")
print("")

path = 'a_text_file.txt'

with open(path) as text_file:
    for line in text_file:
        print(line.rstrip())
        print("weff!")

print("")
print("Converting lines to a list, and then modifying and displaying that list:")
print("")

with open(path) as text_file:
    lines = text_file.readlines()

for idx, line in enumerate(lines):
    lines[idx] = line.rstrip() + "...cough..."

print(lines)
