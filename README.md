<p align="center">
<img src="dijkstra.gif" width="350">
</p>

# Table of content
1. [About](#About)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [License](#License)

# About

This programm aims to visualize how the Dijkstra and A* algorithms work to find the shortest path between two nodes in a graph.

## Dijkstra

> Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm)[4] is an algorithm for finding the shortest paths between nodes in a graph [...] ([Wikipedia: Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm))

The algorithm may be used either for finding the shortest path between a given source and destination in graph or for finding all shortest paths from one source to all other nodes. 
One popular application of this algorithm is the [OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) routing protocol used in networking as a interior gateway protocol by the routers of one network to determine the shortest path to all other routers.

## A*

Yet to be implemented.

# Installation

1. `git clone https://github.com/dvdvgt/shortest-path-visualizer.git`
2. `cd shortest-path-visualizer`
3. `pip install --user -r requirements.txt`
3. `python -m pathfinder.main`

## Dependencies
- [pygame](https://www.pygame.org)

# Usage

## Basics

- Press the **left mouse button** to set the start and barriers.
- Press the **middle mouse button** to set a optional destination node.
- Press the **right mouse button** to reset a node.
- Press **ESC** to reset all nodes.
- Press the **spacebar** to start the algorithm (so far only the dijkstra algorithm has been implemented).

## Displaying SP to different destination

After the shortest path to the destination has been found you may reassign the destination to a different, already discovered (coloured grey) node to show the shortest path to that node as can be seen in the example GIF.

# To-do
* [ ] Implement A* algorithm
* [ ] Write tests

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