# hangman-application
This repository contains 2 py files. The first one contains the Hangman game that can be played on the terminal, and the second one contains the GUI version of the game, to make the experience better for the user.

# Hangman Game

A graphical Hangman game implemented in Python using the Tkinter library for the GUI and PIL for image handling.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Features
- Graphical user interface with Tkinter.
- Randomly chosen words from a predefined list.
- Image updates based on incorrect guesses.
- Displays remaining attempts.
- Simple and intuitive design.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/hangman-game.git
    cd hangman-game
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Prepare the images:**
    - Place your hangman images in the `images/` directory with filenames `img0.jpg` to `img7.jpg`.

## Usage
1. **Run the Hangman game:**
    ```sh
    python hangman_game.py
    ```

2. **Gameplay Instructions:**
    - A random word will be selected from the list.
    - Guess the word by entering one letter at a time.
    - Each incorrect guess will reveal part of the hangman image.
    - The game ends when you either guess the word correctly or run out of attempts.

## Code Explanation
### `center_window` Function
This function centers the application window on the screen. It takes in the window instance and optional width and height parameters, and calculates the position to place the window in the center of the screen.

### `HangManGame` Class
Manages the Hangman game logic and GUI.

#### Attributes:
- `word_list`: List of possible words for the game.
- `attempts_label`, `message_label`, `submit_button`, `letter_entry`, `word_label`, `image_label`: Various Tkinter widgets.
- `master`: The main Tkinter window.
- `image_folder`, `image_files`, `images`, `current_image_index`: Image handling attributes.
- `secret_word`: The word to guess.
- `display_secret_word`: Current state of the guessed word.
- `attempts`: Remaining attempts.

#### Methods:
- `__init__(self, master)`: Initializes the game. It sets up the initial state, loads images, chooses a random word, and calls `setup_gui` to set up the GUI components.
- `setup_gui(self)`: Sets up the GUI components, including the frame, labels, entry, and button, and centers the window.
- `check_letter(self)`: Checks the guessed letter, updates the game state, and displays messages based on whether the guess was correct or incorrect. It also updates the hangman image and remaining attempts.
- `end_game(self, result)`: Ends the game and displays a message indicating whether the player won or lost. It also disables the entry and button.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

