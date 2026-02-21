## Lab-report-01
Implementation of Iterative Deepening Depth-First Search (IDDFS) .

Name:Abu Hanif Khan <br>
ID: 232002053 <br>
Batch: 232_D7 <br>
Course: CSE 316 <br>

## OBJECTIVES: 
This laboratory experiment is to implement and Analyze the Iterative Deepening Depth-First Search (IDDFS) algorithm for solving a pathfinding problem in a two-dimensional maze environment.
•	To represent a maze as a two-dimensional grid where each cell denotes either a free space (0) or a wall (1).
•	To implement the Iterative Deepening Depth-First Search (IDDFS) algorithm using Python programming language.
•	To apply Depth-Limited Search (DLS) iteratively with increasing depth limits in order to determine whether a valid path exists between a given start cell and a target cell.
## How to Run 
```bash
Hanif.py
```
## Example:
# input
```bash
4 4
0 1 0 1
0 0 0 1
1 1 0 0
0 0 1 0
Start: 0 0
Target: 2 3

```
## Output 
```bash
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (1,2), (2,2), (2,3)]
```
## ANALYSIS AND DISCUSSION :

The IDDFS algorithm was used to find a path in a 2D maze, moving only through empty cells and visiting each cell once. It searches by increasing depth limits until the target is found or the maximum depth is reached. In Case #1, the path from start (0,0) to target (2,3) was found at depth 5, showing that IDDFS efficiently finds shallow solutions and backtracks correctly at dead ends. In Case #2, no path exists within the maximum depth, and the algorithm correctly reported failure. This demonstrates that IDDFS is both complete and memory-efficient for maze-solving tasks. 

