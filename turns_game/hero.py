from config import EasyConfig as Config


class Actions:
    ATTACK = 1
    DEFENCE = 2
    HEAL = 3
    LEVELUP = 4


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
        max_hp = 10*((1+self.inc_hp_damage)**(self.level-1))

        # if hero hp will be less then max_hp after heal, then add hp as should.
        if self.hp + max_hp * self.heal_percent < max_hp:
            self.hp += max_hp * self.heal_percent

        else:  # hero hp more then max_hp
            self.hp = max_hp

    def level_up(self):

        if self.coins >= self.level_up_cost*(self.level+1):
            self.level += 1
            self.damage += self.damage*self.inc_hp_damage
            self.hp = 10*((1+self.inc_hp_damage)**(self.level-1))
            self.coins = 0
            return True
        return False

    def attack(self, monster):
        if monster.reduce_health(self) == 0:
            self.coins += monster.level

    def defend(self):
        self.is_defended = True

    def reduce_health(self, monster):

        # Calculating the damage that the monster can case to the hero
        damage = monster.damage * \
            (1 - (self.defense_percentages*int(self.is_defended)))

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return self.hp

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
