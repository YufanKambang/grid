"""
This module provides a set of classes for generating and manipulating
a two-dimensional grid of square cells.

Author - Lester Hedges
"""


class Cell:
    """
    The class contains functionality for a unit-square cell.
    """

    def __init__(self, x, y, w, h):
        """
        Construct a specific cell in the grid.

            x -- The x position in the grid.
            y -- The y position in the grid.
            w -- The width of the grid (number of cells).
            h -- The height of the grid (number of cells).
        """

        if not type(x) is int:
            raise TypeError("The x position must be of type 'int'!")

        if not type(y) is int:
            raise TypeError("The y position must be of type 'int'!")

        if not type(w) is int:
            raise TypeError("The grid width must be of type 'int'!")

        if not type(h) is int:
            raise TypeError("The grid height must be of type 'int'!")

        if w <= 0:
            raise ValueError("The grid width must be greater than zero!")

        if h <= 0:
            raise ValueError("The grid height must be greater than zero!")

        if x < 0 or x >= w:
            raise ValueError("The x position must be between 0 and %s!" % (w - 1))

        if y < 0 or y >= h:
            raise ValueError("The y position must be between 0 and %s!" % (h - 1))

        # Set the position of the cell in the grid.
        self._x = x
        self._y = y

        # Flag that the cell is empty.
        self._is_occupied = False

        # Set the neighbour list.
        self._initialiseNeighbours(w, h)

    def position(self):
        """
        Return the coordinates of the cell as a tuple (x, y).
        """
        return (self._x, self._y)

    def left(self):
        """
        Return the coordinates of the cell to the left as a tuple (x, y).
        """
        if self._neighbour_list[0] is None:
            return None
        else:
            return (self._neighbour_list[0], self._y)

    def right(self):
        """
        Return the coordinates of the cell to right as a tuple (x, y).
        """
        if self._neighbour_list[1] is None:
            return None
        else:
            return (self._neighbour_list[1], self._y)

    def down(self):
        """
        Return the coordinates of the cell below as a tuple (x, y).
        """
        if self._neighbour_list[2] is None:
            return None
        else:
            return (self._x, self._neighbour_list[2])

    def up(self):
        """
        Return the coordinates of the cell above as a tuple (x, y).
        """
        if self._neighbour_list[3] is None:
            return None
        else:
            return (self._x, self._neighbour_list[3])

    def neighbours(self):
        """
        Return the number of neighbouring cells.
        """
        return self._neighbours

    def occupied(self):
        """
        Return whether this cell is occupied.
        """
        return self._is_occupied

    def fill(self):
        """
        Fill the cell.
        """

        self._is_occupied = True

    def empty(self):
        """
        Empty the cell.
        """

        self._is_occupied = False

    def _initialiseNeighbours(self, w, h):
        """
        Initialise the neighbour list.

            w -- The width of the grid (number of cells).
            h -- The height of the grid (number of cells).
        """

        # Initialise the list of neighbouring cells.
        self._neighbour_list = [None] * 4

        # Initialise the number of neighbouring cells.
        self._neighbours = 0

        # Cell isn't on left edge.
        if self._x > 0:
            self._neighbour_list[0] = self._x - 1
            self._neighbours += 1

        # Cell isn't on right edge.
        if self._x < w - 1:
            self._neighbour_list[1] = self._x + 1
            self._neighbours += 1

        # Cell isn't on bottom edge.
        if self._y > 0:
            self._neighbour_list[2] = self._y - 1
            self._neighbours += 1

        # Cell isn't on top edge.
        #this was "w" but changed to "h - 1"
        if self._y < h - 1:
            self._neighbour_list[3] = self._y + 1
            self._neighbours += 1


class Grid:
    """
    The class contains functionality for a two-dimensional grid of
    unit-square cells.
    """

    def __init__(self, w, h):
        """
        Construct a two-dimensional grid.

            w -- The width of the grid (number of cells).
            h -- The height of the grid (number of cells).
        """

        if not type(w) is int:
            raise TypeError("The grid width must be of type 'int'!")

        if not type(h) is int:
            raise TypeError("The grid height must be of type 'int'!")

        if w < 0:
            raise ValueError("The width must be positive!")

        if h < 0:
            raise ValueError("The height must be positive!")

        # Set the width of the grid.
        self._w = w

        # Set the height of the grid.
        self._h = h

        # Generate a two-dimensional list of cells.
        self._cells = [[Cell(x, y, w, h) for y in range(h)] for x in range(w)]

        # Initialise an empty list of filled cells.
        self._filled = []

    def width(self):
        """
        Return the width of the grid.
        """

        return self._w

    def height(self):
        """
        Return the height of the grid.
        """

        return self._h

    def nCells(self):
        """
        Return the number of cells in the grid.
        """

        return self._w * self._w

    def cell(self, x, y):
        """
        Get a specific cell from the grid.

            x -- The x position of the cell.
            y -- The y position of the cell.
        """

        return self._cells[x][y]

    def nFilled(self):
        """
        Return the number of filled cells.
        """

        return len(self._filled)

    def fill(self, x, y, debug=False):
        """
        Fill a cell in the the grid.

            x -- The x position of the cell.
            y -- The y position of the cell.
        """

        # Fill the cell.
        self._cells[x][y].fill()

        # Add the cell to the 'filled' list.
        self._filled.append((x, y))

    def empty(self, x, y, debug=False):
        """
        Empty a cell in the the grid.

            x -- The x position of the cell.
            y -- The y position of the cell.
        """

        # Make sure the cell is filled.
        if self._cells[x][y].occupied():

            # Empty the cell.
            self._cells[x][y].empty()

            # Remove the cell from the filled list.
            self._filled.remove((x, y))
