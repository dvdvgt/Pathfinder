#!/usr/bin/env python3
from pathfinder.util.colour import Colour
from pathfinder.util.state import State

class Vertex:
    """
    Class representing a vertex in graph/grid.

    Attributes
    ----------
    row: int
        Row the vertex is in.
    column: int
        Column the vertex is in.
    x: int
        x coordinate.
    y: int
        y coordinate.
    width: int
        Width of the square which represents a vertex.
    colour: Colour
        Colour of the vertex depending on its state.
    state: State
        State of the vertex. Check the State class for more
        information.
    """

    def __init__(self, row: int, column: int, width: int):
        """
        Parameters
        ----------
        row: int
            Row of the vertex.
        column: int
            Column of the vertex.
        width: int
            Width of the cell which represents a vertex.
        """
        self.row: int = row
        self.column: int = column
        self.x: int = column * width
        self.y: int = row * width
        self.width: int = width

        self.colour: Colour = Colour.WHITE
        self.state: State = State.EMPTY

    def set_start(self):
        """Marks the vertex as the starting point by colouring it red."""
        self.colour = Colour.RED
        self.state = State.START

    def set_end(self):
        """Marks the vertex as the destination point by colouring it blue."""
        self.colour = Colour.BLUE
        self.state = State.END

    def set_barrier(self):
        """Marks the vertex as barrier which cannot be visited by colouring it black."""
        self.colour = Colour.BLACK
        self.state = State.BARRIER

    def set_path(self):
        """Marks the vertex as one of the vertices of the shortest path."""
        self.colour = Colour.GREEN
        self.state = State.PATH

    def set_open(self):
        """Marks the vertex as discovered but not yet visited by colouring in light blue."""
        self.colour = Colour.LIGHT_BLUE
        self.state = State.OPEN

    def set_closed(self):
        """Marks the vertex visited by colouring it light grey."""
        self.colour = Colour.LIGHT_GREY
        self.state = State.CLOSED

    def reset(self):
        """Marks the vertex as empty by colouring it white."""
        self.colour = Colour.WHITE
        self.state = State.EMPTY

    def get_neighbors(self, graph) -> dict:
        """
        Returns all neighbors of the current vertex.

        Parameters
        ----------
        graph: Graph
            Graph of which the current vertex is part of to determine
            its neighbors.

        Returns
        -------
        dict
            Neighbors of the current vertex.
        """
        neighbors: dict = {}
        if self.row - 1 >= 0:
            neighbors["upper"] = graph.grid[self.row - 1][self.column]
        if self.row + 1 < graph.rows:
            neighbors["lower"] = graph.grid[self.row + 1][self.column]
        if self.column - 1 >= 0:
            neighbors["left"] = graph.grid[self.row][self.column - 1]
        if self.column + 1 < graph.columns:
            neighbors["right"] = graph.grid[self.row][self.column + 1]

        return neighbors

    def get_position(self) -> tuple:
        """Returns the row and column the vertex is in"""
        return (self.row, self.column)

    def __str__(self):
        return str(self.get_position())
