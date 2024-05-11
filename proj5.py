def load_sudoku_grid(file_path):
    """Reads a Sudoku grid from a file and returns it as a list of lists of integers."""
    try:
        with open(file_path, 'r') as file:
            sudoku_matrix = [[int(number) for number in line.strip().split()] for line in file if line.strip()]
        return sudoku_matrix
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric values or is not formatted correctly.")
        return None
    except Exception as exc:
        print(f"An error occurred: {exc}")
        return None


def display_sudoku(matrix):
    """Prints the Sudoku grid in a more readable form with '.' representing '0'."""
    for row in matrix:
        print(" ".join(str(elem) if elem != 0 else '.' for elem in row))

def locate_empty_cell(matrix):
    """Finds the first empty cell in the grid, marked by '0', and returns its position as a tuple (row_index, col_index)."""
    for row_index in range(9):
        for col_index in range(9):
            if matrix[row_index][col_index] == 0:
                return row_index, col_index  # row, column
    return None

def check_validity(matrix, number, position):
    """Checks if placing the number 'number' at position 'position' is valid according to Sudoku rules."""
    # Check row
    for idx in range(9):
        if matrix[position[0]][idx] == number and position[1] != idx:
            return False

    # Check column
    for idx in range(9):
        if matrix[idx][position[1]] == number and position[0] != idx:
            return False

    # Check box
    box_x_start = position[1] // 3 * 3
    box_y_start = position[0] // 3 * 3
    for row in range(box_y_start, box_y_start + 3):
        for col in range(box_x_start, box_x_start + 3):
            if matrix[row][col] == number and (row, col) != position:
                return False

    return True

def backtrack_solve(matrix):
    """Solves the Sudoku puzzle using backtracking. Returns True if the puzzle is solved, else False."""
    empty_cell = locate_empty_cell(matrix)
    if not empty_cell:
        return True  # Puzzle solved
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if check_validity(matrix, num, (row, col)):
            matrix[row][col] = num

            if backtrack_solve(matrix):
                return True

            matrix[row][col] = 0

    return False  # Trigger backtracking

def main():
    print("Welcome to the Sudoku Solver Program")
    print("Please input the path to your Sudoku file. The file should contain the grid where '0' represents empty cells, and numbers are separated by spaces.")
    print("------------")
    
    path_to_file = input("Enter the path to your Sudoku file: ")
    sudoku_grid = load_sudoku_grid(path_to_file)
    if sudoku_grid is None:
        print("Failed to read the Sudoku grid from the file.")
        return

    print("Initial Sudoku Grid:")
    display_sudoku(sudoku_grid)

    if backtrack_solve(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        display_sudoku(sudoku_grid)
    else:
        print("\nNo solution exists for the provided Sudoku puzzle.")

if __name__ == "__main__":
    main()
