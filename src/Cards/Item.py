from src.cards.base_card import BaseCard


class Item(BaseCard):
    def __init__(
        self,
        name,
        description,
        deck_type,
        play_time,
        cost,
        ability,
        type,
        bonus,
        two_hand,
        big,
        who_can_use,
        disposable,
    ):
        super().__init__(name, description, deck_type, play_time)
        self.cost = cost
        self.ability = ability
        self.type = type
        self.bonus = bonus
        self.two_hand = two_hand
        self.big = big
        self.who_can_use = who_can_use
        self.disposable = disposable
