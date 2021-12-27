from BaseCard import BaseCard

class MonsterEnchancerCard(BaseCard):
    def __init__(self, name, description, deck_type, play_time, ability):
        super().__init__(name, description, deck_type, play_time)
        self.ability = ability

    def enchance(self, monster):
        #do something with monster
        pass