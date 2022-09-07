class Card:
    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # Returns the suit of the card.
    def suit(self):
        return self.suit
    
    # Returns the value of the card.
    def value(self):
        return self.value
      
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self):
        return self.suit + ' of ' + self.value
