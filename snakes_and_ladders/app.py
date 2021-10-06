import os
import random


def clear_screen():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board(num_ladders, num_snakes):
    used_places = []

    board = [0]*100

    # Adds ladders to board
    for _ in range(num_ladders):
        start = random.randint(1, 98)
        end = random.randint(start+1, 99)

        while (start in used_places) or (end in used_places):
            start = random.randint(1, 98)
            end = random.randint(start+1, 99)
        used_places.append(start)
        used_places.append(end)

        board[start-1] = end - start

    # Adds snakes to board
    for _ in range(num_snakes):
        start = random.randint(1, 99)
        end = random.randint(0, start-1)

        while (start in used_places) or (end in used_places):
            start = random.randint(1, 98)
            end = random.randint(0, start-1)

        used_places.append(start)
        used_places.append(end)

        board[start-1] = end - start

    return board


def print_players(players, current):
    for i in range(len(players)):
        if i == current:
            print('--> Player ' + str(i+1), "\tLocation", players[i]+1)
        else:
            print('    Player ' + str(i+1), "\tLocation", players[i]+1)


def main():

    num_ladder = 6
    num_snakes = 8
    board = init_board(num_ladder, num_snakes)

    num_of_players = input("Enter number of players: ")
    while not num_of_players.isdigit():
        num_of_players = input("Enter number of players (numbers only): ")

    num_of_players=int(num_of_players)
    
    players = [0]*num_of_players

    current = 0

    while True:

        print_players(players, current)
        input("\nPress any key to roll the dice\n")
        clear_screen()
        
        steps = random.randint(1, 6)
        latest_location = players[current]
        players[current] += steps

        if players[current] < 99:
            players[current] += board[players[current]]

        elif players[current] == 99:
            clear_screen()
            print_players(players, current)

            print(f'Player {current+1} won the game!')
            break

        else:
            players[current] = 198 - latest_location - steps
            players[current] += board[players[current]]

        current += 1

        if current == num_of_players:
            current = 0




if __name__ == "__main__":
    main()
