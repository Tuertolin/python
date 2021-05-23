import json

def create_JSON_file(numbers, filename):
# Creates a JSON file with the numbers provided
    with open(filename, 'w') as f:
        json.dump(numbers, f)

def reads_JSON_file(filename):
# Reads a JSON file
    with open(filename) as f:
        numbers = json.load(f)
    print(numbers)


numbers = [1, 2, 3, 3.3, 4, 4.5]
filename = 'numbers_v2.json'

create_JSON_file(numbers, filename)
reads_JSON_file('numbers.json')
reads_JSON_file('numbers_v2.json')
