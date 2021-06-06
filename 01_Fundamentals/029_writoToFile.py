filename = 'proogramming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Hello world!")

#Reads the file
with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())
