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
            self.hand[self.current_player].remove(card)
            if self.check_win():
                print(f"Player{self.curent_player+1}wins!")
                return True #Игрок выиграл
            self.next_player()
        else:
            print("Ты не можешь разыграть эту карту.")
            return False #Игрок проиграл
    def draw_card(self):
           if len(self.deck)>0:
               self.hand[self.current_player].append(self.deck.pop())
    def check_win(self):
        return
    len(self.hand[self.current_player]) == 0
    def next_player(self):
           self.current_player=(self.current_player+1) % len(self.players)
