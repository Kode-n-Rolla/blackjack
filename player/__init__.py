class Player(object):
    
    """Initialized class with name and hands cards"""
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        
    """Add card to hands"""
    def add_card(self, card) -> None:
        self.cards.append(card)

    """Get points equal card value"""
    def get_value(self) -> int:
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == 'A':
                aces += 1
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    """Outpu card value"""
    def __str__(self) -> str:
        text = ''
        for card in self.cards:
            text += str(card) + ' '
        text += 'Cards value: ' + str(self.get_value())
        return text
