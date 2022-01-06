from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Any


class Sex(Enum):
    MALE: auto()
    FEMALE: auto()


class Race(Enum):
    HUMAN: auto()
    ELF: auto()
    DWARF: auto()
    HOBBIT: auto()


class ClassType(Enum):
    WARRIOR: auto()
    SHAMAN: auto()
    WIZARD: auto()
    THIEF: auto()


@dataclass
class Stats:
    level: int = 1
    power: int = 1
    max_cards_in_hand: int = 5
    max_big_items: int = 1
    max_two_handed_items = 1
    escape_bonus: int = 0


class Player:
    def __init__(self, name: str, sex: Sex):
        self.name = name
        self.sex = sex
        self.race = Race.HUMAN
        self.stats = Stats()
        self.cards_in_hand: List[Any] = []
        self.class_types: List[ClassType] = []

    def _calculate_power(self):
        ...
