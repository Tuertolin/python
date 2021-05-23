
def count_words(filename):
 # Count the approx number of words in the file.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the filename {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about ~{num_words} words!")

filename = ['alice_wonderland.txt','Moby_Dick.txt','FightClub.txt']
for file in filename:
    count_words(file)