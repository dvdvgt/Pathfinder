import pytest
import random
from pathfinder.vertex import Vertex
from pathfinder.graph import Graph
from pathfinder.util.colour import Colour
from pathfinder.util.state import State

def test_init_grid():
    g: Graph = Graph(10, 10)
    assert type(g.grid) == list
    assert len(g.grid) == g.rows == g.columns == 10
    assert len(g.grid[0]) == g.columns == g.rows == 10

def test_set_start():
    g: Graph = Graph(10, 10)
    v: Vertex = g.grid[0][5]

    g.set_start(v)
    assert g.start == v
    assert v.state == State.START
    assert v.colour == Colour.RED

def test_set_end():
    g: Graph = Graph(10, 10)
    v: Vertex = g.grid[5][5]

    g.set_end(v)
    assert g.end == v
    assert v.state == State.END
    assert v.colour == Colour.BLUE

def test_reset():
    g: Graph = Graph(10, 10)
    g.set_start(g.grid[0][0])
    g.set_end(g.grid[3][9])
    g.reset()

    assert g.start == g.end == None
    for rows in g.grid:
        for node in rows:
            assert node.state == State.EMPTY
            assert node.colour == Colour.WHITE
    assert g.paths == {}

def random_graph(rows: int, percent_barriers: float):
    g: Graph = Graph(rows, 10)
    g.set_start(
        g.grid[random.randint(0, rows-1)][random.randint(0, rows-1)]
    )
    g.set_end(
        g.grid[random.randint(0, rows-1)][random.randint(0, rows-1)]
    )
    num_barriers: int = (rows ** 2) * percent_barriers

    for i in range(num_barriers - 1):
        while True:
            rand_row: int = random.randint(0, rows)
            rand_col: int = random.randint(0, rows)
            rand_v: Vertex = g.grid[rand_row][rand_col]

            if rand_v not in [g.start, g.end]:
                break
        rand_v.set_barrier()