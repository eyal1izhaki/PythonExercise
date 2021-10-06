import random
import os


def get_word_after_hit(word: str, guessed_word: list, guessed_letter: str):
    for i in range(len(word)):
        if word[i] == guessed_letter:
            guessed_word[i] = word[i]

    return guessed_word


def is_valid_input(input: str):
    if not (input.isalpha() and len(input) == 1):
        return False
    return True


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_the_game(guessed_word :str, life :int, wrong_guesses: set):
    clear_screen()
    print(
        "Life:", life,
        "\nWrong guesses:", wrong_guesses or '{}',
        "\n"+"".join(guessed_word),
        "\n"
    )

def print_win_lose(win :bool):
    clear_screen()
    print("You won the game!" if win else "You lose the game!")


def main():
    wordlist = ('apple', 'orang', 'car', 'cat', 'inactive',
                'geometry', 'python', 'exercise', 'family')
    life = 8
    word = wordlist[random.randint(0, len(wordlist)-1)]
    guessed_word = ["_"]*len(word)
    wrong_guesses = set([])

    while not (life == 0 or ''.join(guessed_word) == word):

        print_the_game(guessed_word, life, wrong_guesses)

        letter = input().lower()

        while not is_valid_input(letter):
            print_the_game(guessed_word, life, wrong_guesses)
            letter = input("Please enter one letter:\n").lower()

        if letter not in word:
            life -= 1
            wrong_guesses.add(letter)
        else:
            guessed_word = get_word_after_hit(word, guessed_word, letter)

    print_win_lose(life)
        


if __name__ == "__main__":
    main()
