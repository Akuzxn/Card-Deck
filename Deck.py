import random
# card numbers
cardType = ["A", "2", "3", "4", "5", "6","7", "8", "9", "10", "J", "Q", "K"]
# card types
cardSorts = ["K", "S", "H", "R"]



class Deck:
    """ Class that creates a deck with 52 cards """

    def __init__(self):
        """ Creating the cards in the deck as a list of cards """
        self.deck = [] #var for the class where the deck is stored in a list

        for sort in cardSorts:
            for card in cardType:
                self.deck.append(sort+card)
        #combines sort and card


    shuffle = lambda self: random.shuffle(self.deck)
    # lambda function that shuffles the cards in the deck

    def hand(self, numberOfCards):
        """
            Deals out n cards from the deck
        """

        # to deal the cards
        dealed_cards = []

        # add the cards to the dealed cards
        # at the same time, remove those cards from the deck

        if not self.deck:
            return []
        #if no cards, return empty list

        for cards in range(numberOfCards):
            poped = self.deck.pop()
            dealed_cards.append(poped)
        #takes cards from the deck and creates a list based on the cards that have been taken out

        return dealed_cards
        #returns the dealed cards

    def del_ut(self, p, cp):
        """
            Dealing p(layers) number of hands with n number of cards in each hand
        """

        # first check if there are enough cards in the deck to deal
        if p * cp > len(self.deck):

            # if not, print the error and return
            print("Error! There are no enough cards in the deck")
            return

        # otherwise deals p(layer) number of cards

        # to store the hands in the list
        hands = []

        # store p number of hands in the list
        for _ in range(p):
            card = self.hand(cp)
            hands.append(card)

        # return hands
        return hands

    __str__ = lambda self: str(self.deck)
    #makes the deck into a string

deck = Deck()
print(deck)

#prints the deck