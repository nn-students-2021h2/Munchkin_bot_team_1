from src.GameMaster.Turn import Turn


class Battle(Turn):
    """Represent battle stage of the game"""

    def __init__(self, player, taken_card):
        super().__init__(player, taken_card)
