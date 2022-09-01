import random

"""Класс Card инициализируется мастью и достоинством карты"""
class Card(object):

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def card_value(self) -> int:
        if self.rank in 'TJQK':
            return 10
        else:
            return ' A23456789'.index(self.rank)

    def get_rank(self) -> int:
        return self.rank

    def __str__(self) -> str:
        return '%s%s' % (self.rank, self.suit)

"""Класс Deck для инициализации карт на 'игровом поле'"""
class Deck(object):

    def __init__(self):
        ranks = '23456789TJQKA'
        suits = ('♥', '♣', '♠', '♦')
        self.cards = [Card(r, s) for r in ranks for s in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
