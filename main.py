from card import *
from player import *

"""Main funcion"""
def black_jack():
    this_deck = Deck()
    player = Player('Frencky')
    dealer = Player('Dealer')
    player.add_card(this_deck.deal_card())
    player.add_card(this_deck.deal_card())
    dealer.add_card(this_deck.deal_card())
    print('Dealer`s cards: ', dealer)
    print(f'{player.name}`s cards: ', player)

    status_game = True

    while player.get_value() < 21:
        choice = input('Take card or not? (y/n): ').lower()
        if choice == 'y':
            player.add_card(this_deck.deal_card())
            print(f'{player.name}`s cards: ', player)
            if player.get_value() > 21:
                print(f'{player.name} lose')
                status_game = False
        else:
            print(f'{player.name} don`t take card')
            break

    if status_game:
        while dealer.get_value() < 17:
            dealer.add_card(this_deck.deal_card())
            print('Dealer`s cards: ', dealer)
            if dealer.get_value() > 21:
                print('Dealer lose')
                status_game = False
    if status_game:
        if player.get_value() > dealer.get_value():
            print(f'{player.name} win')
        else:
            print('Dealer win')

black_jack()
