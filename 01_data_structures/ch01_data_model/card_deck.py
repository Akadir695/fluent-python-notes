# this example explains the power of implementing just two special methods __getitem and __len__
# a deck as sequence of playing cards
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
"""we use collections.namedtuple to construct a simple class to represent individual cards """
beer_card = Card(7, "dionmonds")
deck = FrenchDeck()
# print(len(deck)) # 52
# reading special cards from a deck the first or last is easy 
print(deck[0]) # Card(rank='2', suit='spades')
print(deck[-1]) # Card(rank='A', suit='hearts')
from random import choice
print(choice(deck))
# also __get__delegates to the [] operator of self_cards our automatically supports slicing 
print(deck[:3])
# we can iterate 
for card in deck:
  print(card)
# we can also iterate over in reverse
for card in reversed(deck):
  print(card)
  
# this function that sorts the cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
