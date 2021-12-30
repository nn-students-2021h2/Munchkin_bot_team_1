from src.GameMaster.Turn import Turn

"""Represent battle stage of the game"""


class Battle(Turn):
    def __init__(self, player, taken_card):
        super().__init__(player, taken_card)
