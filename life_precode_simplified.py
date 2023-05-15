from time import sleep


class Board:
    def __init__(self, width: int = 3, height: int = 3):
        self.generation_count = 0
        self.width = 0
        self.height = 0
        self.board = self._generate_new_board(width, height)
        self.previous_board = self._generate_new_board(width, height)

    def _generate_new_board(self, width, height):
        return [[False for _ in range(width)] for _ in range(height)]

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        return "\n".join(
            "".join("o" if cell else "." for cell in row) for row in self.board
        )

    def _is_cell_in_valid_range(self, row: int, col: int) -> bool:
        return 0 <= row < self.height and 0 <= col < self.width

    def _get_number_alive_neighbors(self, row, col):
        count = 0
        for neighbor_row in [row - 1, row, row + 1]:
            for neighbor_col in [col - 1, col, col + 1]:
                if neighbor_col == col and neighbor_row == row:
                    continue
                if self._is_cell_in_valid_range(neighbor_row, neighbor_col):
                    count += self.board[neighbor_row][neighbor_col]
        return count

    def next(self) -> None:
        new_board = self.previous_board
        for row in range(self.height):
            for col in range(self.width):
                new_board[row][col] = self.will_be_alive(row, col)
        self.previous_board = self.board
        self.board = new_board
        self.generation_count += 1

    def will_be_alive(self, row: int, col: int) -> bool:
        number_alive_neighbors = self._get_number_alive_neighbors(row, col)
        if self.board[row][col]:
            # Something is wrong here
            # Can you fix it?
            # Compare it with the rules  of game of life.
            return number_alive_neighbors == 1 or number_alive_neighbors == 1
        return number_alive_neighbors == 2

    def is_alive(self, row: int, col: int) -> bool:
        """Return True if cell is alive."""
        # Put your code here
        pass

    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        # Put your code here
        pass

    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        # Put your code here
        pass


c = CELL_SYMBOL = "o"


if __name__ == "__main__":
    board = Board(3, 3)
    for i in range(3):
        # This code supposed to put a 3 cell in a row to the board
        board.place_cell(1, i)

    for i in range(100):
        print(board)
        board.next()
        sleep(0.5)
