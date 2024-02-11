# Tic Tac Toe Game

This project contains Python code for playing Tic Tac Toe, including implementations for human players, random computer players, and AI computer players using the minimax algorithm.

## Code Overview

### `game.py`

This file contains the implementation of the Tic Tac Toe game (`TicTacToe` class) along with the `play` function for playing the game. It also includes three types of players:

- `HumanPlayer`: Represents a human player who inputs moves via the command line.
- `RandomComputerPlayer`: Represents a computer player who makes random moves.
- `AIComputerPlayer`: Represents an AI computer player using the minimax algorithm to make optimal moves.

### `player.py`

This file contains the definitions of the `Player` class and its subclasses (`RandomComputerPlayer`, `HumanPlayer`, `AIComputerPlayer`). Each player has a `get_move` method to make moves in the game.

## How to Use

1. Run the `game.py` file to play Tic Tac Toe.
2. Choose the type of players you want to play against (human or computer).
3. Follow the prompts to input moves or watch the computer make moves.
4. Enjoy the game and try to win!

## Dependencies

- Python 3.x
