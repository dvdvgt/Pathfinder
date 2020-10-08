from graph import Graph
from vertex import Vertex
from util.state import State


def dijkstra(grid: Graph, gui):
    # Containing pairs of vertix and distance to the starting vertix where
    # the vertix is the key and the distance the key.
    dist: dict = {}
    # Dictionary with pairs of (vertix: previous_vertix)
    prev: dict = {}
    # Containing all yet to visit nodes
    queue: list = []

    # Init dicts and queue
    dist[grid.start] = 0
    for row in grid.grid:
        for node in row:
            if node != grid.start:
                dist[node] = float('inf')
                prev[node] = None
            queue.append(node)
    # Sort queue so that node with lowest distance is at the lowest index
    queue.sort(key=lambda node: dist[node], reverse=True)

    while queue:
        crrnt: Vertex = queue.pop()
        
        # If the end is reached the shortest path has been found
        if crrnt == grid.end:
            break
        if crrnt != grid.start and crrnt != grid.end:
            crrnt.set_closed()

        for neighbor in crrnt.get_neighbors(grid).values():
            # Skip nodes that either cannot be visited or already have been visited
            if neighbor.state == State.CLOSED or neighbor.state == State.BARRIER:
                continue
            # Mark nodes as open
            if neighbor != grid.end and neighbor != grid.start:
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
    mark_path(prev, grid)


def mark_path(path: dict, grid: Graph):
    """

    """
    def marker(crrnt):
        if crrnt != grid.start:
            crrnt.set_path()
            marker(path[crrnt])
        else:
            return
    marker(path[grid.end])
