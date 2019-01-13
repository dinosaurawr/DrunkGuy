from Deck import Deck

class Player(object):

    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def get_upper_card(self):
        card = self.deck.cards[0]
        del self.deck.cards[0]
        return card
    
    def get_last_card(self):
        return self.deck.cards.pop()
    
    def take_cards(self, *cards):
        for card in cards:
            self.deck.cards.append(card)
