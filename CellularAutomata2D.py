import random

from Ruleset import Ruleset2D


class CellularAutomata2D(object):
    """
    A class to represent a 2d cellular automata
    """
    size: tuple[int, int]
    do_wrap: bool
    ruleset: Ruleset2D
    field: list[list]

    def __init__(self, size: tuple[int, int], do_wrap: bool,
                 ruleset: Ruleset2D, density: float) -> None:
        """
        Create a new cellular automata with a random field.
        :param size: Size of the cellular automata field.
        :param do_wrap: Determines whether cells on the edge of the
        field are affected by the cells on the opposite edge, or copied
        from the previous state.
        :param ruleset: A set of rules for the automata.
        :param density: The probability of the cell being alive initially.
        """

        self.size = size
        self.do_wrap = do_wrap
        self.ruleset = ruleset

        field = []
        for i in range(size[1]):
            field.append([])
            for j in range(size[0]):
                field[i].append(1 if random.random() < density else 0)

        self.field = field

    def __init__(self, size: tuple[int, int], do_wrap: bool,
                 ruleset: Ruleset2D, field: list[list]) -> None:
        """
        Create a new cellular automata with a predetermined initial state
        :param size: Size of the cellular automata field.
        :param do_wrap: Determines whether cells on the edge of the
        field are affected by the cells on the opposite edge, or copied
        from the previous state.
        :param ruleset: A set of rules for the automata.
        :param field: Initial state of the cellular automata.
        """

        self.do_wrap = do_wrap
        self.ruleset = ruleset
        self.field = field
        self.size = size

    def get_new_cell_state(self, row: int, col: int) -> int:
        """
        Get a new cell state given its coordinates.
        :param row: Row of the cell.
        :param col: Column of the cell.
        :return: New cell state
        """
        if self.do_wrap:
            chunk = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cell = self.field[(row + i) % self.size[1]] \
                    [(col + j) % self.size[0]]
                    chunk.append(cell)
            return self.ruleset.get_new_state(chunk)

        if ((row == 0) or (row == self.size[0]-1) or
                (col == 0) or (col == self.size[1]-1)):
            return self.field[row][col]

        chunk = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                cell = self.field[row + i][col + j]
                chunk.append(cell)
        return self.ruleset.get_new_state(chunk)

    def step(self):
        """
        Update all the cells in the field
        :return: None
        """
        new_field = []
        for i in range(self.size[1]):
            new_field.append([])
            for j in range(self.size[0]):
                new_field[i].append(self.get_new_cell_state(i, j))

        self.field = new_field

    def display(self):
        print('╔' + '═' * self.size[0] + '╗')
        for row in self.field.copy():
            cells = '║' + ''.join([
                '█' if cell else ' ' for cell in row
            ]) + '║'
            print(cells)
        print('╚' + '═' * self.size[0] + '╝')
