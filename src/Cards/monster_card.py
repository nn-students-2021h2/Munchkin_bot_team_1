from typing import Any

from src.cards.base_card import BaseCard


class MonsterCard(BaseCard):
    def __init__(
        self,
        name: str,
        description: str,
        deck_type: Any,
        play_time: Any,
        level: int,
        ability: Any,
        action: Any,
        treasures: int,
    ):
        super().__init__(name, description, deck_type, play_time)
        self.level = level
        self.ability = ability
        self.action = action
        self.treasures = treasures

    def _action(self, player: Any):
        # do something with player
        pass
