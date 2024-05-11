class PuzzleState:
    def __init__(self, puzzle, parent=None, action=None, depth=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        self.depth = depth

    def generate_possible_moves(self):
        possible_moves = []
        zero_position = self.puzzle.index(0)
        if zero_position % 3 != 0: 
            possible_moves.append('Left ')
        if zero_position % 3 != 2:  
            possible_moves.append('Right ')
        if zero_position > 2:  
            possible_moves.append('Up ')
        if zero_position < 6:  
            possible_moves.append('Down ')
        return possible_moves

    def perform_move(self, move):
        zero_position = self.puzzle.index(0)
        puzzle_copy = list(self.puzzle)
        if move == 'Left ':
            swap_position = zero_position - 1
        elif move == 'Right ':
            swap_position = zero_position + 1
        elif move == 'Up ':
            swap_position = zero_position - 3
        elif move == 'Down ':
            swap_position = zero_position + 3
        puzzle_copy[zero_position], puzzle_copy[swap_position] = puzzle_copy[swap_position], puzzle_copy[zero_position]
        return PuzzleState(puzzle_copy, self, move, self.depth + 1)

    def calculate_manhattan_distance(self):
        manhattan_distance = 0
        for idx in range(9):
            if self.puzzle[idx] == 0: continue  
            x, y = divmod(idx, 3)
            goal_x, goal_y = divmod(self.puzzle[idx] - 1, 3)
            manhattan_distance += abs(x - goal_x) + abs(y - goal_y)
        return manhattan_distance

    def is_solved(self):
        return self.puzzle == [1, 2, 3, 8, 0, 4, 7, 6, 5]

import heapq

def solve_with_astar(initial_state):
    initial = PuzzleState(initial_state)
    priority_queue = []
    state_counter = 0  
    heapq.heappush(priority_queue, (initial.calculate_manhattan_distance(), state_counter, initial))
    visited_states = set()
    expanded_nodes_count = 0

    while priority_queue:
        _, _, current_state = heapq.heappop(priority_queue)
        if tuple(current_state.puzzle) in visited_states:
            continue
        visited_states.add(tuple(current_state.puzzle))
        expanded_nodes_count += 1

        if current_state.is_solved():
            return current_state, current_state.depth, expanded_nodes_count

        for move in current_state.generate_possible_moves():
            new_state = current_state.perform_move(move)
            if tuple(new_state.puzzle) in visited_states:
                continue
            state_counter += 1
            heapq.heappush(priority_queue, (new_state.depth + new_state.calculate_manhattan_distance(), state_counter, new_state))

    return None, None, expanded_nodes_count

from collections import deque

def solve_with_bfs(initial_state):
    initial = PuzzleState(initial_state)
    if initial.is_solved():
        return initial, 0, 0

    queue = deque([initial])
    visited_states = set()
    expanded_nodes_count = 0

    while queue:
        current_state = queue.popleft()
        visited_states.add(tuple(current_state.puzzle))
        expanded_nodes_count += 1

        for move in current_state.generate_possible_moves():
            new_state = current_state.perform_move(move)
            if tuple(new_state.puzzle) in visited_states:
                continue
            if new_state.is_solved():
                return new_state, new_state.depth, expanded_nodes_count
            queue.append(new_state)

    return None, None, expanded_nodes_count

def retrieve_solution_path(final_state):
    path = []
    current = final_state
    while current.parent:
        path.append(current.action)
        current = current.parent
    path.reverse()
    return path

def load_puzzle_from_file(filename):
    try:
        with open(filename, 'r') as file:
            loaded_puzzle = [list(map(int, line.split())) for line in file]
        return loaded_puzzle
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return None

def display_puzzle_state(puzzle):
    if puzzle:
        print("Initial state of the puzzle:")
        for row in puzzle:
            print(' '.join(map(str, row)))    

def main():
    print("Welcome to the Eight-Puzzle Solver!")
    file_name = input("Enter the filename of the puzzle you want to solve: ")
    puzzle = load_puzzle_from_file(file_name)

    if puzzle is None:
        return  

    flat_puzzle = [tile for row in puzzle for tile in row]
    display_puzzle_state(puzzle)

    algorithm_choice = input("Algorithm selection: BFS(1) A*(2): ")
    if algorithm_choice == '1':
        final_state, depth_of_solution, nodes_expanded = solve_with_bfs(flat_puzzle)
    elif algorithm_choice == '2':
        final_state, depth_of_solution, nodes_expanded = solve_with_astar(flat_puzzle)
    else:
        print("Invalid choice.")
        return

    if final_state:
        solution_path = retrieve_solution_path(final_state)
        print("Solution path:", ''.join(solution_path))
        print("Number of moves:", depth_of_solution)
        print("Total nodes expanded:", nodes_expanded)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
