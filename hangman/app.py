import random
import os


def get_random_word(wordlist: tuple):
    word_index = random.randint(0, len(wordlist)-1)
    return wordlist[word_index]


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


def print_the_game(guessed_word, life, wrong_guesses):
    clear_screen()
    print(
        "Life:", life,
        "\nWrong guesses:", wrong_guesses,
        "\n"+"".join(guessed_word),
        "\n"
    )

def print_win_lose(win :bool):
    clear_screen()
    print("You won the game!" if win else "You lose the game!")

def is_wining(guessed_word, word):
    if ''.join(guessed_word) == word:
        return True



def main():
    wordlist = ('apple', 'orang', 'car', 'cat', 'inactive',
                'geometry', 'python', 'exercise', 'family')
    life = 8
    word = get_random_word(wordlist)
    guessed_word = ["_"]*len(word)
    wrong_guesses = []

    while True:

        print_the_game(guessed_word, life, wrong_guesses)

        letter = input()

        while not is_valid_input(letter):
            print_the_game(guessed_word, life, wrong_guesses)
            letter = input("Please enter one english letter:\n")

        if letter not in word:
            life -= 1
            if letter not in wrong_guesses:
                wrong_guesses.append(letter)
        else:
            guessed_word = get_word_after_hit(word, guessed_word, letter)


        if life == 0:
            print_win_lose(False)
            break

        if is_wining(guessed_word, word):
            print_win_lose(True)
            break
        


if __name__ == "__main__":
    main()
