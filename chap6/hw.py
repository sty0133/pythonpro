def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word

def hangman(secret_word):
    guessed_letters = []
    attempts = len(list(secret_word))

    print("\tWelcome to Hangman!\n\n")

    while True:
        print("You've used the following letters: \n", guessed_letters)
        print()
        print("So far, the word is: \n", display_word(secret_word, guessed_letters))
        print()

        if "-" not in display_word(secret_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word)
            break

        if attempts == 0:
            print("You're out of attempts. The word was:", secret_word)
            break

        guess = input("Enter your guess: ").upper()
        print()

        if guess in guessed_letters:
            print("You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print(f"No! {guess} is not in the word!\n")
            attempts -= 1
        else:
            print(f"Yes! {guess} is in the word!\n")

if __name__ == "__main__":
    secret_word = "PYTHON" 
    hangman(secret_word)