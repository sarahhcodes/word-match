import csv
import pygame
from random import randrange

# TO DO:
# implement pygame loop
# finish card class w/temp graphics
# create cards
# test drawing on screen
# add matching function
# function for each round (ensure the cards are not picked more than once)
# game start
# game end
# timer -> how fast did you match the cards?
# accuracy rating -> how many cards did you guess correctly?

# required functions:
# 1) start & reset game -> start new game
# 2) card matching -> behaviour if card is
#    correct (remove from draw list, increase points, accuracy rating)
#    or incorrect (adjust accuracy rating)
# 3) new round -> redraw the screen, reset the cards & make sure they're
#    not picked more than once, carry points over to the new round
# 4) end game -> show score

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

class Card: # class to create each card -> make as sprite
    def __init__(self, japanese, english):
        self.japanese = japanese
        self.english = english
        self.solved = False # has the player matched the card?
        self.image_front = "card_front.png"
        self.image_back = "card_back.png"

def main():
    cards = Cards("vocab.csv")

    print(cards.match_list)


if __name__ == "__main__":
    main()