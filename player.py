class Player():
    #class which reperesents a player
    def __init__(self):
        self.hand = []
        self.balance = 1000
        self.bet = 0
        self.points = 0

    def draw(self, cards):
        #adds a card to players hand
        drown_card = cards.draw()
        self.hand.append(drown_card)
        self.add_points(drown_card)

    def add_points(self, card):
        if card[0] not in ['J', 'Q', 'K', 'A', '1']:
            self.points += int(card[0])
        elif card[0] == 'J':
            self.points += 2
        elif card[0] == 'Q':
            self.points += 3
        elif card[0] == 'K':
            self.points += 4
        elif card[0] == 'A':
            self.points += 11
        else:
            self.points += 10
