import random
import time


color = ('Red', 'Green', 'Blue', 'Yellow')
rank = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
ctype = {'0':'number','1':'number','2':'number','3':'number','4':'number','5':'number','6':'number','7':'number','8':'number','9':'number'}

class Card:
    def _init_(self,color,rank):
        self.rank = rank
        if ctype[rank] =='number':
            self.color = color
            self.cardtype ='number'
        else:
            self.color = None
            self.cardtype='action_noclor'

        def _str_(self):
            if self.color is None:
                return self.rank
            else:
                return self.color+" "+ self.rank

class deck:
    def _init_(self):
        self.deck =[]
        for clr in color:
            for ran in rank:
                if ctype[ran]!='action_nocolor':
                    self.deck.append(Card(clr,ran))
                    self.deck.append(Card(clr,ran))




