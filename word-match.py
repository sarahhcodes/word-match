import csv
from random import randrange

class Cards: # creates and generates random list of cards from csv file
    def __init__(self, source):
        self.source_list = source
        self.vocab_list = []
        self.match_list = []
        self.number_of_cards = 8

        self.convert_list() # generates list of cards for matching
    
    def convert_list(self):
        matches_index = []

        # opens source file
        with open(self.source_list) as file:
            reader = csv.reader(file)
    
            for row in reader:
                self.vocab_list.append({"Japanese": row[0], "English": row[1]})
        
        # randomly generates list
        for _ in range(self.number_of_cards):
            n = randrange(len(self.vocab_list))

            # ensuring no repetition in match_list
            # if n is in matches_index, keep trying to find another random number
    
            while n in matches_index:
                n = randrange(len(self.vocab_list))
    
            matches_index.append(n)

            self.match_list.append(self.vocab_list[n])


def main():
    cards = Cards("vocab.csv")

    print(cards.match_list)


if __name__ == "__main__":
    main()