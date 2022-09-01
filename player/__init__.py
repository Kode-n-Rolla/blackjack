class Player(object):
    
    """Инициализия класса по имени и карт в руке"""
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        
    """Добавление карт в руку"""
    def add_card(self, card) -> None:
        self.cards.append(card)

    """Получение очков достоинства карт в рукt"""
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

    """Вывод достоинства карт в руке"""
    def __str__(self) -> str:
        text = ''
        for card in self.cards:
            text += str(card) + ' '
        text += 'Значения на руке: ' + str(self.get_value())
        return text
