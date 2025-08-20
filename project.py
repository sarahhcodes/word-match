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
        self.matches_index = []
        self.number_of_cards = 8

        self.convert_list() # converts csv to list
        self.random_list() # generates subsection of list for matching
    
    def convert_list(self):
        # opens source file
        with open(self.source_list) as file:
            reader = csv.reader(file)
    
            for row in reader:
                self.vocab_list.append({"Japanese": row[0], "English": row[1]})
                
    def random_list(self):
        # randomly generates list
        
        for _ in range(self.number_of_cards):
            n = randrange(len(self.vocab_list))

            # ensuring no repetition in match_list
            # if n is in matches_index, keep trying to find another random number
    
            while n in self.matches_index:
                n = randrange(len(self.vocab_list))
    
            self.matches_index.append(n)

            self.match_list.append(self.vocab_list[n])
    
    def reset_list(self):
        self.matches_index = [] # reset list

class Card: # class to create each card -> make as sprite
    def __init__(self, japanese, english):
        self.japanese = japanese
        self.english = english
        self.solved = False # has the player matched the card?
        self.image_front = "card_front.png"
        self.image_back = "card_back.png"

def main():
    ########## TEMP GAME LOOP
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255,233,0))
        
        # game goes here
        pygame.draw.rect(screen, (255, 255, 255), (250, 250, 500, 100))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

    cards = Cards("vocab.csv")

    print(cards.match_list)


if __name__ == "__main__":
    main()