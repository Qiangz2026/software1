# Finnish learning and challenge game!

**Qiang Zhang**

## 1. Project description: This is a project for my Python programming course; the idea stems from my own experience learning Finnish.
## The game  is a simple command-line game designed to help players learn and practice Finnish vocabulary.
## At the beginning of the game, players can create a personal profile including their name, age, Finnish level, and interests. The game then provides different vocabulary challenges based on the player's Finnish level and interests.
## Players can also create their own Finnish vocabulary library and practice their custom words.
## When the game ends, the player's information is saved to a JSON file.

## 2. Project structure
```
project/
├── main.py (Starts the game, loads or creates the player, and controls the main program loop.)
├── game_introduction.txt (A simple introduction of the game.)
├── challenge_introduction.txt (A simple introduction of the challenge.)
├── finnish_word.py (Contains all kinds of Finnish vocabulary library.)
├── player_data.json (saved player information.)
├── readme.md
└── functions/
    ├── __init__.py
    ├── load_player.py(load old player, if there is.)
    ├── create_player.py(create new player)
    ├── menu.py(show the main menu)
    ├── game_introduction.py
    ├── player.py (player class, Initializes player information and includes functions for modifying player information, customizing the Finnish vocabulary library and practice vocabulary library.)
    ├── start_game.py (Provides the challenge selection menu.)
    ├── quick_challenge.py (quick_challenge)
    ├── level_challenge.py (level_challenge)
    ├── interest_challenge.py (interest_challenge)
    ├── learn_words.py
    ├── run_challenge.py
    └── save_exit_game.py (save player information and exit the game.)
```
## 3. How to run: Firstly make sure Python is installed on your computer. Because I wrote the game code in VS Code. Therefore, I recommend installing VS Code, then opening the project folder and locating and opening the `main.py` file. After that, click the icon shaped like a slanted triangle in the top-right corner of the page to run it.
