import random  # Importing the random module to select a random word


class HangMan:
    # List of words for the game
    word_list = ['vaporeon', 'jolteon', 'flareon', 'sylveon', 'leafeon', 'umbreon', 'glaceon']

    def __init__(self):
        """Initialize the HangMan class."""
        # Select a random word from the word list
        self.secret_word = random.choice(HangMan.word_list)
        # Create a list to display the secret word with asterisks
        self.display_secret_word = ['*' for letter in self.secret_word]
        # Set the number of attempts
        self.attempts = 8

    def playGame(self):
        """Start and manage the Hangman game."""
        # Welcome message and initial game state
        print("Welcome to Hangman")
        print("You have", self.attempts, "attempts to guess the word.")
        print("Current word:", ''.join(self.display_secret_word))

        # Main game loop
        while self.attempts > 0 and '*' in self.display_secret_word:
            # Prompt the player to enter a letter
            guess = input("Enter a letter: ").lower()
            # Validate the input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            # Check if the guessed letter is in the secret word
            if guess in self.secret_word:
                # Update the display word with the correct guess
                for index, letter in enumerate(self.secret_word):
                    if letter == guess:
                        self.display_secret_word[index] = guess
                print("Good guess!")
            else:
                # Decrease the number of attempts for incorrect guess
                self.attempts -= 1
                print("Incorrect guess. Attempts remaining:", self.attempts)

            # Display the current state of the word
            print("Current word:", ''.join(self.display_secret_word))

        # End of game messages
        if '*' not in self.display_secret_word:
            print("Congratulations! You guessed the word:", self.secret_word)
        else:
            print("Out of attempts! The word was:", self.secret_word)


# If this script is run directly, create an instance of HangMan and start the game
if __name__ == '__main__':
    game = HangMan()
    game.playGame()
