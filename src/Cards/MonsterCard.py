from src.Cards.BaseCard import BaseCard


class MonsterCard(BaseCard):
    def __init__(
        self, name, description, deck_type, play_time, level, ability, action, treasures
    ):
        super().__init__(name, description, deck_type, play_time)
        self.level = level
        self.ability = ability
        self.action = action
        self.treasures = treasures

    def _action(self, player):
        # do something with player
        pass
