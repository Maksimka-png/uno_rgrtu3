import random
class unogame:
    def _init_(self,players):
        self.playes = players
        self.current_play = 0
        self.deck = ['0','1','2','3','4','5','6','7','8','9']
        self.hand = [[]for _ in range(len(players))]

    def deal_cards(self):
        random.shufle(self.deck)
        for player in self.hand:
            for _ in range(7):
                player.append(self.deck.pop())
    def play_card(self,card):
        if card in self.hand[self.current_player]:
            self