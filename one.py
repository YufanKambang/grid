from grid import Grid

grid = Grid(10, 10)
grid.fill(0, 0)
assert grid.nFilled() == 1

grid.fill(3, 7)
assert grid.nFilled() == 2

grid.empty(0, 0)
assert grid.nFilled() == 1

assert grid.cell(3, 7).occupied()
assert not grid.cell(0, 0).occupied()