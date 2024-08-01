import unittest
import random


def generate_random_board():
    """
    Generate a random board with size between 3 and 6 filled with random colors.

    Returns:
        list: A 2D list representing the board.
    """
    size = random.randint(3, 6)  # Random board size between 3 and 6
    colors = ['R', 'G', 'B', 'Y', 'O']  # List of possible colors
    board = [[random.choice(colors) for _ in range(size)] for _ in range(size)]
    return board


class FloodFillGameDFS:
    """
    Class to implement the Flood Fill Game using Depth-First Search (DFS).
    """

    def __init__(self, board):
        """
        Initialize the game with the given board.

        Args:
            board (list): 2D list representing the initial state of the board.
        """
        self.board = board  # Store the board
        self.n = len(board)  # Get the size of the board
        self.moves = []  # List to keep track of moves
        print("Initial Board:")
        self.print_board()  # Print the initial board

    def get_neighbors(self, x, y):
        """
        Get the neighboring tiles of a given tile.

        Args:
            x (int): X-coordinate of the tile.
            y (int): Y-coordinate of the tile.

        Returns:
            list: List of tuples representing the neighboring tiles.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # North, South, West, East directions
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                neighbors.append((nx, ny))
        return neighbors

    def flood_fill(self, x, y, target_color, replacement_color):
        """
        Perform flood fill using DFS to change the color of connected tiles.

        Args:
            x (int): X-coordinate of the starting tile.
            y (int): Y-coordinate of the starting tile.
            target_color (str): The color to be replaced.
            replacement_color (str): The new color.
        """
        if target_color == replacement_color:
            return  # If target color is the same as replacement color, do nothing
        stack = [(x, y)]  # Initialize stack with the starting tile
        while stack:
            cx, cy = stack.pop()  # Pop a tile from the stack
            if self.board[cx][cy] == target_color:
                self.board[cx][cy] = replacement_color  # Change the color of the tile
                for nx, ny in self.get_neighbors(cx, cy):  # Check neighbors
                    if self.board[nx][ny] == target_color:  # If neighbor tile is of target color
                        stack.append((nx, ny))  # Add it to the stack

    def count_connected_tiles(self, x, y, target_color):
        """
        Count the number of tiles connected to the origin with the same color.

        Args:
            x (int): X-coordinate of the starting tile.
            y (int): Y-coordinate of the starting tile.
            target_color (str): The color to count.

        Returns:
            int: Number of connected tiles of the target color.
        """
        visited = set()  # To keep track of visited tiles
        stack = [(x, y)]  # Start from the origin
        count = 0  # Initialize count of connected tiles
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited or self.board[cx][cy] != target_color:
                continue  # Skip if already visited or not the target color
            visited.add((cx, cy))
            count += 1  # Increase the count
            for nx, ny in self.get_neighbors(cx, cy):
                if (nx, ny) not in visited:
                    stack.append((nx, ny))  # Add unvisited neighbors to the stack
        return count

    def choose_best_color(self):
        """
        Choose the best color to maximize the number of connected tiles.

        Returns:
            str: The best color to choose.
        """
        current_color = self.board[0][0]
        color_count = {}
        for color in set(tile for row in self.board for tile in row if tile != current_color):
            original_board = [row[:] for row in self.board]  # Make a copy of the board
            self.flood_fill(0, 0, current_color, color)  # Simulate flood fill with this color
            count = self.count_connected_tiles(0, 0, color)
            color_count[color] = count
            self.board = original_board  # Restore the board

        if not color_count:
            return current_color  # If color count is empty, return the current color

        best_color = max(color_count, key=color_count.get)  # Choose the color with the most connected tiles
        return best_color

    def play_game(self):
        """
        Play the game until all tiles are the same color.
        """
        step = 1
        while True:
            best_color = self.choose_best_color()  # Choose the best color
            if best_color == self.board[0][0]:
                break  # If no better color is found, game is over
            self.moves.append(best_color)  # Record the move
            print(f"Step {step}: Chosen color - {best_color}")  # Print the chosen color for each step
            self.flood_fill(0, 0, self.board[0][0], best_color)  # Perform the flood fill
            print(f"Board after step {step}:")
            self.print_board()  # Print the board after each move
            step += 1

        print("Game finished.")
        print("Total number of steps:", step - 1)
        print("Moves taken:", self.moves)

    def print_board(self):
        """
        Print the current state of the board.
        """
        for row in self.board:
            print(' '.join(row))  # Print each row of the board
        print()


class TestFloodFillGameDFS(unittest.TestCase):
    """
    Unit test class for FloodFillGameDFS.
    """

    def run_game_and_assert(self, board):
        """
        Helper function to run the game and assert the final state.

        Args:
            board (list): The initial board state.
        """
        game = FloodFillGameDFS(board)
        game.play_game()
        self.assertTrue(all(tile == game.board[0][0] for row in game.board for tile in row))
        print("Moves taken:", game.moves)

    def test_random_game(self):
        """
        Test the game with multiple random boards.
        """
        for _ in range(5):  # Run multiple random tests
            board = generate_random_board()
            self.run_game_and_assert(board)


if __name__ == '__main__':
    unittest.main()
