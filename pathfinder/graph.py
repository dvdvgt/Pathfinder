#!/usr/bin/env python3
import pygame
from vertex import Vertex


class Graph:
    """
    Class representing a graph with methods for managing it. However all
    vertices are apart by the same distance therefore this is more of a grid
    than a graph.

    Attributes
    ----------
    rows: int
        Total number of rows
    columns: int
        Total number of rows
    vertex_width: int
        Width of square representing a vertex.
    start: Vertex
        The starting vertex in the graph from which the shortest
        path the destination is to be found.
    end: Vertex
        The destination vertex to which to shortest path is to be
        found.
    grid: list
        A list representing the graph/grid.
    """

    def __init__(self, rows: int, vertix_width: int):
        """
        Parameters
        ----------
        rows: int
            Total number of rows. Since the window is square the number
            of rows also equals the number of columns.
        vertix_width: int
            Width of the square representing a vertix in graph.
        """
        self.rows: int = rows
        self.columns: int = rows
        self.vertex_width: int = vertix_width

        self.start: Vertex = None
        self.end: Vertex = None

        self.grid: list = self.init_grid()

    def init_grid(self) -> list:
        """
        Initialize the graph by creating a 2d list where the first dimension
        represents a row and the second dimension represents a columns.

        Returns
        -------
        list
            2d list representing a graph. 
        """
        xs: list = []
        ys: list = []

        for row in range(self.rows):
            for col in range(self.columns):
                node = Vertex(row, col, self.vertex_width)
                ys.append(node)
            xs.append(ys)
            ys = []

        return xs

    def set_start(self, v: Vertex):
        """
        Sets a given vertex as the starting point in graph.

        Parameters
        ----------
        v: Vertex
            Starting point.
        """
        v.set_start()
        self.start = v

    def set_end(self, v: Vertex):
        """
        Sets a given vertex as destination in graph.

        Parameters
        ----------
        v: Vertex
            Destination point.
        """
        v.set_end()
        self.end = v

    def reset(self):
        """
        Resets the graph by reseting start, destination and all vertex objects.
        """
        self.start = None
        self.end = None
        self.grid = self.init_grid()
