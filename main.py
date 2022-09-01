from card import *
from player import *

"""Главная игровая функция"""
def black_jack():
    this_deck = Deck()
    player = Player('Френки')
    dealer = Player('Дилер')
    player.add_card(this_deck.deal_card())
    player.add_card(this_deck.deal_card())
    dealer.add_card(this_deck.deal_card())
    print('Карты дилера: ', dealer)
    print(f'Карты {player.name}: ', player)

    status_game = True

    while player.get_value() < 21:
        choice = input('Взять карту или нет? (y/n): ').lower()
        if choice == 'y':
            player.add_card(this_deck.deal_card())
            print(f'Карты {player.name}: ', player)
            if player.get_value() > 21:
                print(f'{player.name} проиграл')
                status_game = False
        else:
            print(f'{player.name} не берет карты')
            break

    if status_game:
        while dealer.get_value() < 17:
            dealer.add_card(this_deck.deal_card())
            print('Карты дилера: ', dealer)
            if dealer.get_value() > 21:
                print('Дилер проиграл')
                status_game = False
    if status_game:
        if player.get_value() > dealer.get_value():
            print(f'{player.name} выиграл')
        else:
            print('Дилер выиграл')

black_jack()
