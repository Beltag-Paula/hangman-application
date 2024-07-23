import tkinter as tk  # Importing the Tkinter library for GUI components
from PIL import Image, ImageTk  # Importing PIL for image handling
import random  # Importing random for selecting a random word


def center_window(some_window, width=800, height=600):
    """
    Center the application window on the screen.

    Parameters:
    some_window (Tk): The Tkinter window instance.
    width (int): Width of the window. Default is 800.
    height (int): Height of the window. Default is 600.
    """
    some_window.geometry(f"{width}x{height}")
    screen_width = some_window.winfo_screenwidth()
    screen_height = some_window.winfo_screenheight()
    position_x = int((screen_width / 2) - (width / 2))
    position_y = int((screen_height / 2) - (height / 2))
    some_window.geometry(f"{width}x{height}+{position_x}+{position_y}")


class HangManGame:
    # List of words for the game
    word_list = ['vaporeon', 'jolteon', 'flareon', 'sylveon', 'leafeon', 'umbreon', 'glaceon']

    def __init__(self, master):
        """
        Initialize the HangManGame class.

        Parameters:
        master (Tk): The main Tkinter window.
        """
        self.attempts_label = None
        self.message_label = None
        self.submit_button = None
        self.letter_entry = None
        self.word_label = None
        self.image_label = None
        self.master = master
        self.master.title("Hangman Game")

        # Load images for the hangman game
        self.image_folder = "images/"
        self.image_files = [f"{self.image_folder}img{i}.jpg" for i in range(8)]
        self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.image_files]
        self.current_image_index = 0

        # Choose a random word and set initial display
        self.secret_word = random.choice(HangManGame.word_list)
        self.display_secret_word = ['*' for _ in self.secret_word]
        self.attempts = 8

        # Set up the GUI components
        self.setup_gui()

    def setup_gui(self):
        """Set up the GUI components."""
        frame = tk.Frame(self.master, width=800, height=600)
        frame.grid_propagate(False)
        frame.grid(row=0, column=0)

        # Image label for hangman images
        self.image_label = tk.Label(frame, image=self.images[self.current_image_index])
        self.image_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="w")

        # Label to display the secret word
        self.word_label = tk.Label(frame, text=' '.join(self.display_secret_word), font=("Helvetica", 24),
                                   wraplength=300)
        self.word_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Entry for guessing a letter
        self.letter_entry = tk.Entry(frame, font=("Helvetica", 18))
        self.letter_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Button to submit the guessed letter
        self.submit_button = tk.Button(frame, text="Submit", command=self.check_letter)
        self.submit_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Label to display messages
        self.message_label = tk.Label(frame, text="", font=("Helvetica", 14), wraplength=300)
        self.message_label.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        # Label to display the remaining attempts
        self.attempts_label = tk.Label(frame, text=f"Attempts remaining: {self.attempts}", font=("Helvetica", 14))
        self.attempts_label.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        # Center the application window
        center_window(self.master)

    def check_letter(self):
        """Check the guessed letter and update the game state."""
        guess = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.secret_word:
            for index, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.display_secret_word[index] = guess
            self.message_label.config(text="Good guess!")
        else:
            self.attempts -= 1
            if self.current_image_index < len(self.images) - 1:
                self.current_image_index += 1
            self.image_label.config(image=self.images[self.current_image_index])
            self.message_label.config(text="Incorrect guess.")
            self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")

        self.word_label.config(text=' '.join(self.display_secret_word))

        if '*' not in self.display_secret_word:
            self.message_label.config(text="Congratulations! You guessed the word.")
            self.end_game("win")
        elif self.attempts == 0:
            self.message_label.config(text=f"Out of attempts! The word was: {self.secret_word}")
            self.end_game("lose")

    def end_game(self, result):
        """End the game and display the result."""
        if result == "win":
            self.message_label.config(text=f"Congratulations! The word was: {self.secret_word}")
        else:
            self.message_label.config(text=f"Out of attempts! The word was: {self.secret_word}")
        self.submit_button.config(state="disabled")
        self.letter_entry.config(state="disabled")


if __name__ == '__main__':
    root = tk.Tk()
    game = HangManGame(root)
    root.mainloop()
