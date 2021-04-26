#file_path = '~/Documents/text_file.txt'
filename = 'text_file.txt'

with open('text_file.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

"""Reading the file line by line """
with open('text_file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print("############")

"""Saving the lines in a variable """
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

print("\n############")

"""Working with files"""

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))