from typing import Any

from src.GameMaster.Turn import Turn


class Battle(Turn):
    """Represent battle stage of the game"""

    def __init__(self, player: Any, taken_card: Any):
        super().__init__(player, taken_card)
