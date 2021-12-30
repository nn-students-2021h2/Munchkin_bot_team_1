from typing import Any

from src.Cards.BaseCard import BaseCard


class CurseCard(BaseCard):
    def __init__(
        self,
        name: str,
        description: str,
        deck_type: Any,
        play_time: Any,
        is_instant_curse: bool,
    ):
        super().__init__(name, description, deck_type, play_time)
        self.is_instant_curse = is_instant_curse

    def curse(self, player: Any):
        # do something with player
        pass
