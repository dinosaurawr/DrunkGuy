class Card(object):
    suits = ["черви", "крести", "буби", "пики"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(Card.values[self.value] +" "+ Card.suits[self.suit])

    def __lt__(self, other_card):

        if self.value < other_card.value:
            return True
        
        return False

    def __gt__(self, other_card):

        if self.value > other_card.value:
            return True

        return False

    def __eq__(self, other_card):

        if self.value == other_card.value:
            return True
        return False
        
