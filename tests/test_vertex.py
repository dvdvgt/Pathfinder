import pytest
from pathfinder.vertex import Vertex
from pathfinder.graph import Graph
from pathfinder.util.colour import Colour
from pathfinder.util.state import State


def test_init():
    v: Vertex = Vertex(10, 5, 10)

    assert v.x == 5 * 10
    assert v.y == 10 * 10
    assert v.colour == Colour.WHITE
    assert v.state == State.EMPTY

def test_get_position():
    v: Vertex = Vertex(10, 5, 10)
    v_pos: tuple = v.get_position()

    assert v_pos == (10, 5)
    assert type(v_pos) == tuple

def test_get_neighbors():
    g: Graph = Graph(10, 10)
    # Pick top left node
    v: Vertex = g.grid[0][0]
    v_neighbors: dict = v.get_neighbors(g)
    
    assert type(v_neighbors) == dict
    assert list(v_neighbors.keys()) == ["lower", "right"]

    # Pick bottm right node
    v_1: Vertex = g.grid[9][9]
    v_1_neighbors: dict = v_1.get_neighbors(g)

    assert list(v_1_neighbors.keys()) == ["upper", "left"]

def test_setter():
    v: Vertex = Vertex(12, 5, 8)
    v.set_start()
    v.set_barrier()
    v.set_closed()
    v.set_open()
    
    assert v.state == State.OPEN
    assert v.colour == Colour.LIGHT_BLUE