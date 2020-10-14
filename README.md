<p align="center">
<img src="example.gif" width="350">
</p>

# Table of content
1. [About](#About)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [To-do](#To-do)
4. [License](#License)
5. [Examples](#Examples)

# About

This programm aims to visualize how the Dijkstra and A* algorithms work to find the shortest path between two nodes in a graph.

## Dijkstra

> Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm)[4] is an algorithm for finding the shortest paths between nodes in a graph [...] ([Wikipedia: Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm))

The algorithm may be used either for finding the shortest path between a given source and destination in graph or for finding all shortest paths from one source to all other nodes. 
One popular application of this algorithm is the [OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) routing protocol used in networking as a interior gateway protocol by the routers of one network to determine the shortest path to all other routers.

## A*

> A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. ([Wikipedia: A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm))

# Installation

1. `git clone https://github.com/dvdvgt/shortest-path-visualizer.git`
2. `cd shortest-path-visualizer`
3. `pip install --user -r requirements.txt`
3. `python -m pathfinder.main`

## Dependencies
- [pygame](https://www.pygame.org)

# Usage

## Setting source, destination and barriers
- Press the **left mouse button** to set the start and barriers.
- Press the **middle mouse button** to set an optional destination node (mandatory for A* though).

## Reset
- Press the **right mouse button** to reset/delete a node.
- Press **ESC** to reset all nodes.
- Press **C** to reset all nodes except start, end and barriers.

## Starting an algorithm
- Press **A** to start the A* algorithm.
- Press **D** to start the Dijkstra algorithm.

## Generation a maze
- Press **M** to start generating a maze.

## Changing Destination

After the shortest path to the destination has been found you may reassign the destination to a different, already discovered (coloured grey or blue) node to show the shortest path to that node (as can be seen in the example GIF).

# To-do
* [X] Implement A* algorithm.
* [ ] Write tests.
* [X] Implement a maze generator.

# License

Copyright (C) 2020 David Voigt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
