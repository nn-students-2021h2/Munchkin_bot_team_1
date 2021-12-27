import sys
sys.path.append('../BaseCard')

from BaseCard import BaseCard

class CurseCard(BaseCard):
    def __init__(self, name, description, deck_type, play_time, instant_curse):
        super().__init__(name, description, deck_type, play_time)
        self.instant_curse = instant_curse
        
    def curse(self, player):
        #do something with player
        pass
    