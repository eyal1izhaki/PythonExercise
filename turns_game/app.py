import os
from hero import Hero, Actions
from monster import Monster
import random
import time


def clear_screen():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def print_game(hero, monster):
    clear_screen()
    print(f"""
##################
Hero
##################
{hero}

##################
Monster
##################
{monster}

__________________
Actions:                
    {str(Actions.ATTACK)}. Attack
    {str(Actions.DEFENCE)}. Defence
    {str(Actions.HEAL)}. Heal
    {str(Actions.LEVELUP)}. Level up

    """)


def random_name():
    names = ["Stenchface",
             "Stenchhand",
             "Mournbrute",
             "Dreamtooth",
             "The Bitter Mumbler",
             "The Enraged Demon",
             "The Ancient Dweller",
             "The Aquatic Raptor Bat",
             "The Black-Striped Killer Rhino",
             "The Screeching Doom Hog",
             "Mistflayer",
             "Chaosmutant",
             "Stoneghoul",
             "Voodoosoul",
             "The Wretched Bulge",
             "The Undead Mongrel",
             "The Lonely Face",
             "The Tusked Dread Yak",
             "The Brutal Berserker Lizard"
             "The Cold-Blooded Dire Leviathan"]

    return names[random.randint(0, len(names)-1)]


def main():
    clear_screen()
    hero_name = input("Enter hero name: ")
    hero = Hero(hero_name)
    monster_name = random_name()
    monster = Monster(monster_name, hero.level)

    while hero.hp > 0:

        print_game(hero, monster)
        action = input("Choose your action: ")
        while not (action.isdigit() and 0 < int(action) < 5):
            action = input("Not an action! Choose your action: ")
        action = int(action)

        if not hero.choose_action(action, monster):
            if action == Actions.LEVELUP:
                print('Not enough coins!')
                time.sleep(2)

        monster.attack(hero)

        if monster.hp == 0:
            print("You killed a monster! Ohh, there's another one coming!!")
            time.sleep(2)
            monster = Monster(random_name(), hero.level)

    clear_screen()
    print('You lost the game :(')


if __name__ == "__main__":
    main()
