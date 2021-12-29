from typing import Any


class BaseCard:
    def __init__(self, name: str, description: str, deck_type: Any, play_time: Any):
        self.name = name
        self.description = description
        self.deck_type = deck_type
        self.play_time = play_time
