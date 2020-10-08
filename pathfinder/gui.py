#!/usr/bin/env python3
import pygame
from util.colour import Colour
from graph import Graph
from solver import dijkstra


class GUI:
    """
    Class containing all methods for creating and updating a GUI with pygame.

    Attributes
    ----------
    rows: int
        Total number of rows starting at 0.
    columns: int
        Total number of columns starting at 0.
    width: int
        Width of the window.
    cell_width: int
        Width of cell representing a node in a graph.
    graph: Graph
        Containing all nodes of graph plus methods for managing the graph.
    win
        Main window.
    """

    def __init__(self, rows: int, width: int):
        """
        Parameters
        ----------
        rows: int
            Total number of rows. Since the window is a square the number of rows
            equals the number of columns.
        width: int
            Width of the window used for calculating the width of the cells.
        """
        self.rows: int = rows
        self.columns: int = rows
        self.width: int = width
        self.vertix_width: int = width // rows
        self.graph: Graph = Graph(self.rows, self.vertix_width)

        self.win = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Pathfinding")

    def draw_grid(self):
        """
        Draws the grid lines.
        """
        for i in range(self.rows):
            pygame.draw.line(
                self.win,
                Colour.GREY,
                (0, i * self.vertix_width),
                (self.width, i * self.vertix_width)
            )
            for j in range(self.columns):
                pygame.draw.line(
                    self.win,
                    Colour.GREY,
                    (j * self.vertix_width, 0),
                    (j * self.vertix_width, self.width)
                )

    def draw(self):
        """
        Reponsible for drawing the cells and calling the draw_grid function
        which draws the grid.
        """
        self.win.fill(Colour.WHITE)
        # Draw cells
        for row in self.graph.grid:
            for cell in row:
                pygame.draw.rect(
                    self.win,
                    cell.colour,
                    (cell.x, cell.y, self.vertix_width, self.vertix_width)
                )
        self.draw_grid()

        pygame.display.update()

    def event_handler(self) -> bool:
        """
        Responsible for handling all mouse and key events and calling
        the appropiate functions.
        """
        for event in pygame.event.get():
            # Stop loop if window closed
            if event.type == pygame.QUIT:
                return False

            # Left click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = self.get_click_pos(pos)
                node = self.graph.grid[row][col]

                if not self.graph.start and node != self.graph.end:
                    self.graph.set_start(node)
                elif not self.graph.end and node != self.graph.start:
                    self.graph.set_end(node)
                elif node != self.graph.end and node != self.graph.start:
                    node.set_barrier()

            # Right click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = self.get_click_pos(pos)
                node = self.graph.grid[row][col]

                node.reset()
                if node == self.graph.start:
                    self.graph.start = None
                elif node == self.graph.end:
                    self.graph.end = None

            # Reset with ESC
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.graph.reset()
                elif self.graph.start and self.graph.end and event.key == pygame.K_SPACE:
                    dijkstra(self.graph, self)

        return True

    def loop(self):
        """
        Main loop of the window.
        """
        while self.event_handler():
            self.draw()
        pygame.quit()

    def get_click_pos(self, pos: tuple) -> tuple:
        """
        Determines which cell was clicked.

        Parameters
        ----------
        pos: tuple
            tuple containing the x and y coordinates.

        Returns
        -------
        tuple
            containing the row and column of the selected cell.
        """
        x, y = pos
        row = y // self.vertix_width
        col = x // self.vertix_width
        return (row, col)


if __name__ == "__main__":
    window = GUI(40, 800)
    window.loop()