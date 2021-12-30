from src.GameMaster.Turn import Turn

"""Represet battle gme battle stage"""


class Battle(Turn):
    def __init__(self, player, taken_card):
        super().__init__(player, taken_card)
