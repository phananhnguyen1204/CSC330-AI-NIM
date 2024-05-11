def min_value(sticks_left, max_pick, alpha, beta):
    if sticks_left <= 0:
        return 1  # Max (computer) wins because Min (human) cannot move.
    value = float('inf')
    for i in range(1, min(max_pick, sticks_left) + 1):
        score = max_value(sticks_left - i, max_pick, alpha, beta)
        value = min(value, score)
        beta = min(beta, score)
        if alpha >= beta:
            break  # Alpha cut-off
    return value

def max_value(sticks_left, max_pick, alpha, beta):
    if sticks_left <= 0:
        return -1  # Min (human) wins because Max (computer) cannot move.
    value = float('-inf')
    for i in range(1, min(max_pick, sticks_left) + 1):
        score = min_value(sticks_left - i, max_pick, alpha, beta)
        value = max(value, score)
        alpha = max(alpha, score)
        if alpha >= beta:
            break  # Beta cut-off
    return value

def alpha_beta(sticks_left, max_pick):
    alpha = float('-inf')
    beta = float('inf')
    best_move = 1  # Initialize with a default move in case all moves have equal value.
    value = float('-inf')
    for i in range(1, min(max_pick, sticks_left) + 1):
        move_value = min_value(sticks_left - i, max_pick, alpha, beta)
        if move_value > value:
            value = move_value
            best_move = i
        alpha = max(alpha, move_value)
        if alpha >= beta:
            break  # Beta cut-off
    return value, best_move  # Return the value for completeness, even though bestMove is what we're after.

def main():
    print("Let's play NIM with me\n")
    print("Game will start now\n")

    sticks = int(input("Enter the initial number of sticks in the pile: "))
    max_pick = int(input("Enter the maximum number of sticks you can pick up: "))

    while sticks <= 0 or max_pick <= 0:
        print("Invalid number of sticks or max pick. Please enter valid values.")
        sticks = int(input("Initial sticks in the pile: "))
        max_pick = int(input("Maximum number of sticks you can pick up: "))

    print(f"Each player takes turns picking up 1 to {max_pick} sticks")
    print("The player who picks up the last stick wins\n")
    print("Good luck and have fun!\n")
    print("The computer will start first\n")

    while sticks > 0:
        _, best_move = alpha_beta(sticks, max_pick)
        sticks -= best_move
        print(f"Computer turn. {best_move} sticks were picked.")
        print(f"There are {sticks} sticks left\n")
        if sticks <= 0:
            print("The computer wins!\n")
            break
        print("********************************\n")

        print("Now. Your turn")
        user = int(input(f"Choose number of sticks you want to pick (1-{max_pick}): "))
        while user > max_pick or user < 1 or user > sticks:
            user = int(input(f"Invalid input. Please enter a number between 1 and {min(max_pick, sticks)}: "))
        print(f"You chose {user} sticks.")
        sticks -= user
        print(f"There are {sticks} sticks left\n")
        print("********************************\n")
        if sticks <= 0:
            print("You win!\n")
            break

if __name__ == "__main__":
    main()
