import csv
from random import randrange

source_list = "vocab.csv" # csv file containing words to import
vocabulary = []
match_list = []
matches_index = []

with open(source_list) as file:
    reader = csv.reader(file)
    
    for row in reader:
        vocabulary.append({"Japanese": row[0], "English": row[1]})

for _ in range(8):
    n = randrange(len(vocabulary))

    # ensuring no repetition in match_list
    # if n is in matches_index, keep trying to find another random number
    
    while n in matches_index:
        n = randrange(len(vocabulary))
    
    matches_index.append(n)

    match_list.append(vocabulary[n])

print(match_list)
