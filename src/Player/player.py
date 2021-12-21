"""Player class implementation and other usefull objects for that"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, List, Optional


class Race(Enum):
    """Represent race of the player"""

    HUMAN = auto()
    ELF = auto()
    DWARF = auto()
    HOBBIT = auto()


class ClassType(Enum):
    """Represent class type of the player"""

    WARRIOR = auto()
    WIZARD = auto()
    THIEF = auto()
    SHAMAN = auto()


class Sex(Enum):
    """Represent sex of the player"""

    MALE = auto()
    FEMALE = auto()


@dataclass
class Stats:
    """Store player stats"""

    level: int = 1
    power: int = 1
    race: Race = Race.HUMAN
    class_type: Optional[ClassType] = None


@dataclass
class Equipment:
    """
    Represent players equipment

    Weapons list must contain one two-handed weapon or two one-handed one
    """

    # TODO all theese fields should be Item class or None
    headgear: Any = None
    armor: Any = None
    footgear: Any = None
    weapons: List[Any] = field(default_factory=list)


class Player:
    """Store all player's stats and cards"""

    def __init__(self, name: str, sex: Sex) -> None:
        """
        Create new player with passed name and sex
        """

        # TODO Make valid annotations
        self.cards_in_hand: List[Any] = []
        self.cards_on_table: List[Any] = []
        self.equipment = Equipment()
        self.escape_bonus = 0
        self.max_big_items = 1
        self.max_cards_in_hand = 5
        self.name = name
        self.sex = sex
        self.stats = Stats()

    def _calculate_power(self) -> None:
        """
        Calculate and set player's power based on item cards change
        """

        ...

    # TODO Rename make_curse -> apply_curse
    # TODO Make valid annotation
    def make_curse(self, curse: Any) -> None:
        """
        Depending on the passed curse change player stats
        """

        ...
