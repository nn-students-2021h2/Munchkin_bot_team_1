from src.Cards.BaseCard import BaseCard


class Item(BaseCard):
    def __init__(
        self,
        name,
        description,
        deck_type,
        play_time,
        cost,
        ability,
        gear_type,
        bonus,
        is_two_hand,
        is_big,
        who_can_use,
        is_disposable,
    ):
        super().__init__(name, description, deck_type, play_time)
        self.cost = cost
        self.ability = ability
        self.gear_type = gear_type
        self.bonus = bonus
        self.is_two_hand = is_two_hand
        self.is_big = is_big
        self.who_can_use = who_can_use
        self.is_disposable = is_disposable
