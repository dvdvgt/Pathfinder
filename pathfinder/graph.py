#!/usr/bin/env python3
import pygame
from vertex import Vertex
from util.state import State


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

    def __init__(self, rows: int, vertex_width: int):
        """
        Parameters
        ----------
        rows: int
            Total number of rows. Since the window is square the number
            of rows also equals the number of columns.
        vertex_width: int
            Width of the square representing a vertix in graph.
        """
        self.rows: int = rows
        self.columns: int = rows
        self.vertex_width: int = vertex_width

        self.start: Vertex = None
        self.end: Vertex = None
        self.paths: dict = {}

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
        self.paths = {}
        self.grid = self.init_grid()

    def dijkstra(self, gui) -> dict:
        # Containing pairs of vertix and distance to the starting vertix where
        # the vertix is the key and the distance the key.
        dist: dict = {}
        # Dictionary with pairs of (vertix: previous_vertix)
        prev: dict = {}
        # Containing all yet to visit nodes
        queue: list = []

        # Init dicts and queue
        dist[self.start] = 0
        for row in self.grid:
            for node in row:
                if node != self.start:
                    dist[node] = float('inf')
                    prev[node] = None
                queue.append(node)
                
        # Sort queue so that node with lowest distance is at the lowest index
        queue.sort(key=lambda node: dist[node], reverse=True)

        while queue:
            crrnt: Vertex = queue.pop()

            # If the end is reached the shortest path has been found
            if crrnt == self.end:
                break
            
            if crrnt != self.start and crrnt != self.end:
                crrnt.set_closed()

            for neighbor in crrnt.get_neighbors(self).values():
                # Skip nodes that either cannot be visited or already have been visited
                if neighbor not in queue or neighbor.state == State.BARRIER:
                    continue
                # Mark nodes as open
                if neighbor != self.end and neighbor != self.start:
                    neighbor.set_open()
                # Check whether there's a faster path by comparing known
                # to newly discovered distances
                alt_dist = dist[crrnt] + 1
                if alt_dist < dist[neighbor]:
                    dist[neighbor] = alt_dist
                    prev[neighbor] = crrnt
            # Redraw the grid
            gui.draw()
            # Sort the queue again to account for changes in distances
            queue.sort(key=lambda node: dist[node], reverse=True)

        self.paths = prev

    def mark_path(self, delete: bool):
        """
        Parameters
        ----------
        path: dict
            Dictionary containing the shortest path to each cell.
        graph: Graph
            Graph object of the current graph.
        """
        def marker(current: Vertex):
            if current != self.start:
                if delete:
                    current.set_closed()
                else:
                    current.set_path()
                marker(self.paths[current])
        marker(self.paths[self.end])
