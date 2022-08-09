from random import shuffle

class Cards:
    def __init__(self):
        self.cards = list(range(52))
        shuffle(self.cards)

    def shuffle(self):
        self.cards = list(range(52))
        shuffle(self.cards)

    def draw(self):
        c = ''
        card = self.cards.pop()

        if card % 13 < 9:
            c += str(card % 13 + 2)
        elif card % 13 == 9:
            c += 'J'
        elif card % 13 == 10:
            c += 'Q'
        elif card % 13 == 11:
            c += 'K'
        else:
            c += 'A'
        
        if card % 4 == 0:
            c += 'S'
        elif card % 4 == 1:
            c += 'C'
        elif card % 4 == 2:
            c += 'D'
        elif card % 4 == 3:
            c += 'H'

        return c