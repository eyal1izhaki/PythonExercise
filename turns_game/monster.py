import random
from config import EasyConfig as Config


class Monster:

    proport_hp_level = Config.MONSTER_HP_PROPOR_TO_LEVEL
    proport_damage_level = Config.MONSTER_DAMAGE_PROPOR_TO_LEVEL

    def __init__(self, name, player_level):
        self.name = name

        level_range_bottom = player_level if player_level == 1 else player_level - 1
        self.level = random.randint(level_range_bottom, player_level + 1)

        self.damage = self.proport_damage_level*self.level
        self.hp = self.proport_hp_level * \
            (1+Config.HERO_INC_DAMAGE_PERCENTAGE)**(self.level-1)

    def attack(self, hero):
        hero.reduce_health(self)

    def reduce_health(self, hero):
        self.hp -= hero.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def __str__(self) -> str:
        return f"Name: {self.name}\nHP: {str(self.hp)}\nDamage: {str(self.damage)}\nLevel: {str(self.level)}"
