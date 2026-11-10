import random


WORDS = {
    "apple": "A crunchy fruit that can be red or green.",
    "tiger": "A large striped wild cat.",
    "chair": "You sit on it.",
    "water": "You drink it to stay hydrated.",
    "planet": "Earth is one of these.",
    "rocket": "It can travel into space.",
    "rainbow": "You may see one in the sky after rain.",
    "elephant": "A very large animal with a trunk.",
    "butterfly": "An insect with colorful wings.",
    "chocolate": "A sweet treat made from cocoa.",
    "keyboard": "You use it to type on a computer.",
    "mountain": "A very high natural area of land.",
    "library": "A place where you can borrow books.",
    "sandwich": "Food often made with bread and a filling.",
    "sunflower": "A tall yellow flower that faces the sun.",
}


def choose_word():
    """Choose a random word and its matching hint."""
    return random.choice(list(WORDS.items()))


def show_word(secret_word, guessed_letters):
    """Display guessed letters and underscores for hidden letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    """Play one round of the mystery word game."""
    secret_word, hint = choose_word()
    guessed_letters = set()
    attempts_left = 7

    print("\nWelcome to Mystery Word Game!")
    print(f"The word has {len(secret_word)} letters.")

    while attempts_left > 0:
        print(f"\nWord: {show_word(secret_word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter from A to Z.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")

            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nYou win! The word was '{secret_word}'.")
                return
        else:
            attempts_left -= 1
            print("That letter is not in the word.")
            print(f"Hint: {hint}")

    print(f"\nGame over! The word was '{secret_word}'.")


def main():
    """Run games until the player chooses to quit."""
    while True:
        play_game()

        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
