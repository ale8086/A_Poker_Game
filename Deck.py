import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    ]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
        
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.create_deck()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __init__(self):
        self.__cards = []

    def create_deck(self):
        for suit in self.suit:
            for rank in self.rank:
                new_card = (rank, suit)
                self.__cards.append(new_card)

                how to commit changes to the repository