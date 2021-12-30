from src.GameMaster.Battle import Battle


class Turn:
    """A class that describes the behavior of the game during combat"""

    def __init__(self, player, taken_card):
        self._player = player
        self._taken_card = taken_card

    def turn(self):
        if self._taken_card.type == "monster":
            # init Fight class
            battle = Battle(..., ...)

        elif self._taken_card.type == "curse":
            # apply a curse on the current player
            self._player.make_curse()  # method in Players class
