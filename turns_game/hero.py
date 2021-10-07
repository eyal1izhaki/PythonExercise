from config import EasyConfig as Config


class Actions:
    ATTACK = 1
    LEVELUP = 2
    HEAL = 3
    DEFENCE = 4


class Hero:

    heal_percent = Config.HERO_INC_HEAL_PERCENTAGE
    inc_hp_damage = Config.HERO_INC_DAMAGE_PERCENTAGE
    level_up_cost = Config.HERO_LEVEL_UP_COST
    defense_percentages = 0.8

    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        self.is_defended = False

    def heal(self):
        if self.hp+10*((1+self.inc_hp_damage)**(self.level-1))*self.heal_percent < 10*((1+self.inc_hp_damage)**(self.level-1)):
            self.hp += 10*((1+self.inc_hp_damage) **
                           (self.level-1))*self.heal_percent
        else:
            self.hp = 10*((1+self.inc_hp_damage)**(self.level-1))

    def level_up(self):

        if self.coins > self.level_up_cost*(self.level+1):
            self.level += 1
            self.damage += self.damage*self.inc_hp_damage
            self.hp = 10*((1+self.inc_hp_damage)**(self.level-1))
            return True
        return False

    def attack(self, monster):
        if monster.reduce_health(self) == 0:
            self.coins += monster.level

    def defend(self):
        self.is_defended = True

    def reduce_health(self, monster):

        if not self.is_defended:
            self.hp -= monster.damage
            self.is_defended = False
        else:
            self.hp -= monster.damage*self.defense_percentages

        if self.hp < 0:
            self.hp = 0

        return self.hp if self.hp > 0 else 0

    def choose_action(self, action, monster=None):

        if action == Actions.ATTACK and monster:
            self.attack(monster)
            return True

        elif action == Actions.DEFENCE:
            self.defend()
            return True

        elif action == Actions.HEAL:
            self.heal()
            return True

        elif action == Actions.LEVELUP:
            return self.level_up()

    def __str__(self) -> str:
        return f"Name: {self.name.capitalize()}\nHP: {str(self.hp)}\nDamage: {str(self.damage)}\nLevel: {str(self.level)}\nCoins: {str(self.coins)}"
