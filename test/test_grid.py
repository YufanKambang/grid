import pytest

from ..grid import Grid, Cell

def test_fill():
    """
    Tests to see if it does fill a cell in the the grid.
    """

    g = Grid(4, 4)
    g.fill(1, 1)

    assert g.cell(1, 1).occupied()

    assert g.nFilled() == 1

def test_empty():
    """
    Tests to see if it does empty a cell in the the grid.
    """

    g = Grid(4, 4)
    g.fill(1, 1)

    assert g.cell(1, 1).occupied()

    assert g.nFilled() == 1

    g.empty(1, 1)

    assert not g.cell(1, 1).occupied()

    assert g.nFilled() == 0