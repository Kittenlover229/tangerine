# All the imports are to be at the top of a file, that makes it easy to search
# for all the external things.
from random import randint

dictionary = ["cow", "cat", "dog", "slice", "cake", "sale"]
attempt_count = 7


def makeup_a_word() -> str:
    word_index = randint(0, len(dictionary) - 1)
    return dictionary[word_index]


def find_many_letters_in_str(letter: str, in_str: str) -> list[int]:
    assert len(letter) == 1
    indices = []
    for i, letter_in_str in enumerate(in_str):
        if letter == letter_in_str:
            indices.append(i)
    return indices


def main():
    """
    The actual body of the program.
    It is usually separated to improve readability.
    """

    wins = 0
    losses = 0

    while True:
        attempts_left = attempt_count

        # start by inventing a new word to play with
        word = makeup_a_word()
        # This is the part of the word that will be revealed to the user
        revealed_word = "_" * len(word)

        while attempts_left > 0:
            print("Your word is:", revealed_word)
            print("You have", attempts_left, "left")
            guess = input("Guess a letter: ").strip()

            # Runs if guess is an empty string (falsy value)
            if not guess:
                # This will interrupt the outermost loop
                exit()

            if len(guess) != 1:
                # Ask for a guess again, kindly reminding the user that they are wrong
                print("You may only guess one letter at a time!")
                continue

            # This will improve user experience, since 'A' and 'a' are the same letter
            # we will treat them both as 'a'
            guess = guess.lower()

            indices = find_many_letters_in_str(guess, word)
            was_guessed_before = guess in revealed_word

            if indices:
                # This executes if indices is non-empty (guess is correct)
                print("You guessed", len(indices), "correct!")

                revealed_word = "".join(
                    map(
                        lambda ix: word[ix[0]]
                        if ix[0] in indices
                        else revealed_word[ix[0]],
                        enumerate(revealed_word),
                    )
                )

            elif was_guessed_before:
                # This executes when the guess was made before
                print("You are repeating yourself, try another letter")
            else:
                # Finally, this executes when the guess is incorrect
                print("Nope, wrong!")
                attempts_left -= 1

            if attempts_left == 0:
                print("You are out of attempts! The word was", word)
            elif revealed_word == word:  # All of the word was revealed:
                print(
                    "You won! It only took you",
                    attempt_count - attempts_left,
                    "wrong guesses!",
                    "The word was",
                    word,
                )
                break
            print(
                "\nYou won a total of ",
                wins,
                "times and lost",
                losses,
                "times",
            )
        print()  # Print an empty line to separate this game from the one about to start


main()
