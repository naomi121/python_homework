def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        display_word = [
            char if char.lower() in guesses else "_" for char in secret_word
        ]
        print("".join(display_word))
        return all(char.lower() in guesses for char in secret_word)

    return hangman_closure


secret = input("Enter the secret word: ")
game = make_hangman(secret)

won = False
while not won:
    guess = input("Guess a letter: ")
    won = game(guess)

print("You guessed the word!")