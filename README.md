This project implements a simple Flood Fill Game using Depth-First Search (DFS). The objective of the game is to change the color of the board such that all tiles become the same color using the fewest number of moves.

Algorithm Explanation

Initialization:

A board of size between 3 and 6 is generated with random colors.

Note on Libraries:
While our aim to use no external libraries for the core algorithm, i have included the random library purely for convenience. The random library is used only to simplify the generation of the board and the creation of test cases. It has no effect on the algorithm's logic or performance.

Flood Fill Algorithm:

The algorithm starts from the top-left corner and uses DFS to identify all connected tiles of the same color.
The identified tiles are then changed to the new color.
Choosing the Best Color:

For each possible color, simulate a flood fill operation.
Count the number of connected tiles for each simulated color.
Choose the color that results in the maximum number of connected tiles.

Game Loop:

The game continues until all tiles on the board are the same color.
The number of moves and the chosen colors for each move are recorded.
