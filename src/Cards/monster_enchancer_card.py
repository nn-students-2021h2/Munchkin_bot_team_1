from typing import Any

from src.cards.base_card import BaseCard
from src.cards.monster_card import MonsterCard


class MonsterEnchancerCard(BaseCard):
    def __init__(
        self, name: str, description: str, deck_type: Any, play_time: Any, ability: Any
    ):
        super().__init__(name, description, deck_type, play_time)
        self.ability = ability

    def enchance(self, monster: MonsterCard):
        # do something with monster
        ...
