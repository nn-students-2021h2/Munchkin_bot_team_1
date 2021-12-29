from typing import Any

from src.cards.base_card import BaseCard


class Item(BaseCard):
    def __init__(
        self,
        name: str,
        description: str,
        deck_type: Any,
        play_time: Any,
        cost: int,
        ability: Any,
        gear_type: Any,
        bonus: Any,
        is_two_hand: bool,
        is_big: bool,
        who_can_use: Any,
        disposable: Any,
    ):
        super().__init__(name, description, deck_type, play_time)
        self.cost = cost
        self.ability = ability
        self.gear_type = gear_type
        self.bonus = bonus
        self.is_two_hand = is_two_hand
        self.is_big = is_big
        self.who_can_use = who_can_use
        self.disposable = disposable
