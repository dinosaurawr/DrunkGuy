from random import shuffle
from Card import Card

class Deck(object):

    def __init__(self):

        self.cards = []

        for suite in range(4):
            for value in range(2, 15):
                
                self.cards.append(Card(suite, value))
            
        shuffle(self.cards)


