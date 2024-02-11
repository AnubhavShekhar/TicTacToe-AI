import random
import math
from typing import Union


class Player:
    """
    Represents a player in the Tic Tac Toe game.

    Attributes:
    - letter: The letter assigned to the player ('X' or 'O').
    """

    def __init__(self, letter: str) -> None:
        """Initializes a player with the given letter."""
        self.letter: str = letter

    def get_move(self, game) -> int:
        """
        Gets the move from the player.

        Args:
        - game: The Tic Tac Toe game object.

        Returns:
        - int: The position where the player wants to make a move.
        """
        pass


class RandomComputerPlayer(Player):
    """
    Represents a computer player that makes random moves.

    Attributes:
    Inherits from Player class.
    """

    def __init__(self, letter: str) -> None:
        """Initializes a random computer player with the given letter."""
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Gets a random move from the computer player.

        Args:
        - game: The Tic Tac Toe game object.

        Returns:
        - int: The position where the computer player wants to make a move.
        """
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """
    Represents a human player.

    Attributes:
    Inherits from Player class.
    """

    def __init__(self, letter: str) -> None:
        """Initializes a human player with the given letter."""
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Gets a move from the human player.

        Args:
        - game: The Tic Tac Toe game object.

        Returns:
        - int: The position where the human player wants to make a move.
        """
        valid_square = False
        val = None

        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move(0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square!! Please try again.")

        return val


class AIComputerPlayer(Player):
    """
    Represents an AI computer player using the minimax algorithm.

    Attributes:
    Inherits from Player class.
    """

    def __init__(self, letter: str) -> None:
        """Initializes an AI computer player with the given letter."""
        super().__init__(letter)

    def get_move(self, game) -> int:
        """
        Gets a move from the AI computer player using the minimax algorithm.

        Args:
        - game: The Tic Tac Toe game object.

        Returns:
        - int: The position where the AI computer player wants to make a move.
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player) -> dict:
        """
        Applies the minimax algorithm to find the best move.

        Args:
        - state: The current state of the game.
        - player: The player ('X' or 'O') for whom to find the best move.

        Returns:
        - dict: A dictionary containing the best move's position and score.
        """
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.no_of_empty_squares() + 1) if other_player == max_player else -1 * (state.no_of_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'positon': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = " "
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
