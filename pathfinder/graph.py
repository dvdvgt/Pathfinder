#!/usr/bin/env python3
import pygame
from pathfinder.util.priority_queue import PriorityQueue
from queue import LifoQueue
import time
import math
import random
from pathfinder.vertex import Vertex
from pathfinder.util.state import State


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

    def __get_discovered(self):
        nodes: list = []
        for rows in self.grid:
            for node in rows:
                if node.state in [State.OPEN, State.CLOSED, State.PATH]:
                    nodes.append(node)
        return nodes

    def reset(self):
        """
        Resets the graph by reseting start, destination and all vertex objects.
        """
        self.start = None
        self.end = None
        self.paths = {}
        self.grid = self.init_grid()

    def reset_discovered(self):
        self.paths = {}
        for node in self.__get_discovered():
            node.reset()

    def dijkstra(self, gui) -> dict:
        """
        Finds the shortest path(s) to either one destination or to all other nodes
        starting at a source node.
        This implementation uses a priority queue for keeping track of yet to visit
        nodes. At first only the source node is in the queue. New nodes will be added
        after they have been discovered  (are neighbors of visited nodes).

        gui
            GUI object for accessing the drawing method to redraw the window.
        """

        # Containing pairs of vertix and distance to the starting vertix where
        # the vertix is the key and the distance the key.
        dist: dict = {}
        # Dictionary with pairs of (vertix: previous_vertix)
        prev: dict = {}
        # Containing all yet to visit nodes.
        queue: PriorityQueue = PriorityQueue()

        # Init dicts and queue
        dist[self.start] = 0
        for row in self.grid:
            for node in row:
                if node != self.start:
                    dist[node] = float('inf')
                    prev[node] = None
                
        # Add the starting node to the queue with the distance as metric. In case of
        # a tie the current time will be used as a tie breaker so that the least recently
        # added element wins.
        queue.put((dist[self.start], time.time(), self.start))

        while not queue.empty():
            # Get element with minimum distance from the queue.
            crrnt: Vertex = queue.get()[2]

            # Mark as visited
            if crrnt != self.start and crrnt != self.end:
                crrnt.set_closed()

            # If the end is reached the shortest path has been found
            if crrnt == self.end:
                break

            # Discover neighbors:
            for neighbor in crrnt.get_neighbors(self).values():

                # Skip nodes that either cannot be visited or already have been visited
                if neighbor.state == State.BARRIER or neighbor.state == State.CLOSED:
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
                    # Add newly discovered neighbor to the queue.
                    queue.put((dist[neighbor], time.time(), neighbor))

            # Redraw the grid
            gui.draw()

        self.paths = prev

    def a_star(self, gui):
        # Open priority queue
        open_queue: PriorityQueue = PriorityQueue()

        # Dict containing shortest path
        prev: dict = {}

        # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
        gScore: dict = {node: float('inf') for rows in self.grid for node in rows}
        gScore[self.start] = 0

        # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
        # how short a path from start to finish can be if it goes through n.
        fScore: dict = gScore.copy()
        fScore[self.start] = self.__manhattan_distance(self.start)

        # Add source node to the queue
        open_queue.put((fScore[self.start], time.time(), self.start))

        while not open_queue.empty():
            # Pop node with lowest f-score and explore its neighbors
            current: Vertex = open_queue.get()[2]
            # If the destination has been reached the shortest path has been found
            if current == self.end:
                break
            
            # Explore the current node's neighbors
            for neighbor in current.get_neighbors(self).values():
                # Barrierer nodes are not visitable and therefore cannot be considered
                # for the shortest path
                if neighbor.state == State.BARRIER:
                    continue
                # Since this is a grid like graph where all distances to neighbors are the
                # same 1 is chosen as distance between the current and neighbor node
                alt_dist = gScore[current] + 1

                # Update the g score if the distance via the neighbor is lower than previously known
                if alt_dist < gScore[neighbor]:
                    prev[neighbor] = current
                    gScore[neighbor] = alt_dist
                    fScore[neighbor] = gScore[neighbor] + self.__euclidean_distance(neighbor)

                    # If the node is not already in the queue add it for consideration in the
                    # following iterations
                    if not open_queue.is_element(neighbor, key=lambda x: x[2]):
                        open_queue.put((fScore[neighbor], time.time(), neighbor))
                        # Set the neighbor as open
                        if neighbor != self.end and neighbor != self.start:
                            neighbor.set_open()
            # Mark the current node as closed however it might be re-opened later on
            if current != self.start and current != self.end:
                current.set_closed()
                
            gui.draw()
        self.paths = prev

    def __euclidean_distance(self, node: Vertex) -> float:
        """
        Calculates the euclidean distance between a given node and the graph's destination.

        Parameters
        ----------
        node: Vertex

        Returns
        -------
        float
            Euclidean distance between given and destination node.
        """
        return math.sqrt(
            (node.x - self.end.x) ** 2 + (node.y - self.end.y) ** 2
        )

    def __manhattan_distance(self, node: Vertex) -> int:
        """
        Calculates the manhattan distance between a given node and the destination of
        the current graph.

        Parameters
        ----------
        node: Vertex

        Returns
        -------
        int
            Distance between given node and the graph's destination node.
        """
        return abs(node.x - self.end.x) + abs(node.y - self.end.y)

    def mark_path(self, delete: bool):
        """
        Parameters
        ----------
        path: dict
            Dictionary containing the shortest path to each cell.
        graph: Graph
            Graph object of the current graph.
        """
        current: Vertex = self.paths[self.end]
        while current != self.start:
            if delete:
                current.set_closed()
            else:
                current.set_path()
            current = self.paths[current]

    def __set_all_barriers(self):
        """Marks all nodes in the grid as a barrier."""
        for rows in self.grid:
            for node in rows:
                node.set_barrier()

    def generate_maze(self, gui):
        """
        Iterative maze generator utilizing a LIFO queue for all unvisited cells.

        Parameters
        ----------
        gui: GUI
            GUI object used for updating the grid while the maze is being made.
        """
        self.__set_all_barriers()
        # LIFO queue for mananging nodes with unvisited neighbors
        queue: LifoQueue = LifoQueue()
        # Select top left as start node
        start: Vertex = self.grid[0][0]
        queue.put(start)
        start.reset()
        gui.draw()
        # While there are still nodes in the queue with unvisited neighbors. 
        # This assures that all nodes will reachable.
        while not queue.empty():
            # Pop the last recently added node
            current: Vertex = queue.get()
            # List of all neighbors not yet visited
            neighbors = [node for node in current.get_neighbors(self, 2).values() if node.state == State.BARRIER] 
            # If there are still unvisited neighbors push current node into the queue again
            if neighbors:
                queue.put(current)
                # Select a random neighbor and remove wall between current and neighbor
                neighbor: Vertex = random.choice(neighbors)
                wall_pos = (
                    (current.row + neighbor.row) // 2, (current.column + neighbor.column) // 2
                )
                # Determine wall between current and neighbor to connect both by removing the wall.
                wall: Vertex = self.grid[wall_pos[0]][wall_pos[1]]
                wall.reset()
                # Mark neighbor as open and put it in the queue to discover its neighbors.
                neighbor.reset()
                queue.put(neighbor)
                # Redraw the grid
                gui.draw()