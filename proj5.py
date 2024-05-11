def read_sudoku(file_path):
    """Reads a Sudoku grid from a file and returns it as a list of lists of integers."""
    try:
        with open(file_path, 'r') as file:
            grid = [[int(num) for num in line.strip().split()] for line in file if line.strip()]
        return grid
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric values or is not formatted correctly.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def print_sudoku(grid):
    """Prints the Sudoku grid in a more readable form with '.' representing '0'."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(grid):
    """Finds the first empty cell in the grid, marked by '0', and returns its position as a tuple (row, col)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j  # row, col
    return None

def is_valid(grid, num, pos):
    """Checks if placing the number 'num' at position 'pos' is valid according to Sudoku rules."""
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking. Returns True if the puzzle is solved, else False."""
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False  # Trigger backtracking

def main():
    print("Welcome to the Sudoku Solver Program")
    print("Please input the path to your Sudoku file. The file should contain the grid where '0' represents empty cells, and numbers are separated by spaces.")
    print("------------")
    
    file_path = input("Enter the path to your Sudoku file: ")
    sudoku_grid = read_sudoku(file_path)
    if sudoku_grid is None:
        print("Failed to read the Sudoku grid from the file.")
        return

    print("Initial Sudoku Grid:")
    print_sudoku(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_sudoku(sudoku_grid)
    else:
        print("\nNo solution exists for the provided Sudoku puzzle.")

if __name__ == "__main__":
    main()
