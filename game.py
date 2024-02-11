from player import HumanPlayer, RandomComputerPlayer, AIComputerPlayer
import time
from typing import List, Union


class TicTacToe:
    """
    Represents the Tic Tac Toe game.

    Attributes:
    - board: List containing the current state of the game board.
    - current_winner: Represents the current winner of the game.
    """

    def __init__(self) -> None:
        """Initializes the Tic Tac Toe game."""
        self.board: List[str] = [" " for _ in range(9)]
        self.current_winner: Union[str, None] = None

    def print_board(self) -> None:
        """Prints the current state of the game board."""
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums() -> None:
        """Prints the reference numbers for the game board positions."""
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self) -> List[int]:
        """Returns a list of available moves on the board."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self) -> bool:
        """Checks if there are empty squares left on the board."""
        return " " in self.board

    def no_of_empty_squares(self) -> int:
        """Counts the number of empty squares left on the board."""
        return self.board.count(" ")

    def make_move(self, square: int, letter: str) -> bool:
        """
        Makes a move on the board.

        Args:
        - square: The position on the board where the move is made.
        - letter: The player's letter ('X' or 'O').

        Returns:
        - bool: True if the move is valid and made successfully, False otherwise.
        """
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square: int, letter: str) -> bool:
        """
        Checks if the current move leads to a winning condition.

        Args:
        - square: The position on the board where the move is made.
        - letter: The player's letter ('X' or 'O').

        Returns:
        - bool: True if the move results in a win, False otherwise.
        """
        # check row
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        col = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # No winner
        return False


def play(game: TicTacToe, x_player: Union[HumanPlayer, RandomComputerPlayer, AIComputerPlayer],
         o_player: Union[HumanPlayer, RandomComputerPlayer, AIComputerPlayer], print_game: bool = True) -> str:
    """
    Plays a game of Tic Tac Toe.

    Args:
    - game: The Tic Tac Toe game object.
    - x_player: The player who plays 'X'.
    - o_player: The player who plays 'O'.
    - print_game: If True, prints the game progress.

    Returns:
    - str: The winner of the game ('X', 'O', or 'Tie').
    """
    if print_game:
        game.print_board_nums()

    letter = "X"

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to {square} \n")
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(letter + " Wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        if print_game:
            time.sleep(0.8)

    if print_game:
        print("It's a tie!")
    return "Tie"


if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0

    for _ in range(1000):
        o_player = AIComputerPlayer("O")
        x_player = HumanPlayer("X")
        # uncomment below code for ai vs random computer player
        # x_player = RandomComputerPlayer("X")
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)

    # uncomment the below code to see results of ai vs random computer player
    #     result = play(t, x_player, o_player, print_game=False)

    #     if result == 'X':
    #         x_wins += 1
    #     elif result == "O":
    #         o_wins += 1
    #     else:
    #         ties += 1

    # print(f"After 1000 iterations x wins {x_wins} times, o wins {
    #       o_wins} times and tied {ties} times")
