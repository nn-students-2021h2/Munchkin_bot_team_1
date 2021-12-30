from src.GameMaster.Turn import Turn


class Player:
    pass


class GameMaster:
    def __init__(self, number_of_players):
        """Class to control game proccess"""

        # Create default list of players
        self._players = [Player() for _ in range(number_of_players)]

        # Create dungeon and treasure card deck with random shuffle
        self._dungeon_cards_deck = []  # List of dicts
        self._treasure_cards_deck = []  # List of dicts

        # Variable to track whose turn is now
        self._whose_turn = 0

        pass

    def get_players(self, name=None):
        """Return List of Players or player with selected name"""

        if id is None:
            for player in self._players:
                print(dict(player))
        else:
            return filter(lambda player: player["name"] == name, self._players)

    def _take_dungeon_card(self):
        """Take card from dungeon cards deck"""

        taken_card = self._dungeon_cards_deck[-1]
        self._dungeon_cards_deck.pop(len(self._dungeon_cards_deck) - 1)

        return taken_card

    def start_game(self):
        """Start game method"""

        is_game_end = False  # Game end trigger

        while is_game_end:
            self._turn()

            if self._whose_turn == len(self._players) - 1:
                self._whose_turn = 0
            else:
                self._whose_turn += 1

            is_game_end = True

    def _turn(self):
        """Turn init"""

        taken_card = self._take_dungeon_card()
        turn = Turn(..., ...)
        turn.turn()  # create Turn instance to manipulate game during turn stage
