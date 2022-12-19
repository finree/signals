import random
valid = []
invalid = []
for i in range(10):
    number = random.randint(1,99)
    character = chr(number)
    print(character)
    answer = input("is this a valid character? (y/n)")
    if answer == "y":
        valid.append(character)
    else:
        invalid.append(character)
print(valid)

FILENAME = 'character.txt'
with open(FILENAME, 'a') as myfile:
    for i in valid:
        myfile.write(i)