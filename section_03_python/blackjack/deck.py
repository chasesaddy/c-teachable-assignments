class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit, value):
    
    # Returns the suit of the card.
    def suit(self):
    
    # Returns the value of the card.
    def value(self):
      
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self):

class Deck:    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
      SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
      VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

      for suit in SUITS:
          for value in VALUES:
              self.deck.append( [ value, suit ] )
      
    
    # Returns the number of Cards in the Deck
    def size(self):
    
    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self):
    
    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self):
    
    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
    
    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
    
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
      
    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self):
