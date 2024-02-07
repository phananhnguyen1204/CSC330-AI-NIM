import random

# move: is the number of sticks taken
# num_sticks: the total of sticks in the game
# this function return True if the move is valid, else False
def check_valid_move(move,num_sticks):
  return 1 <= move and move <= 4 and move <= num_sticks

# Start the game
def start_game():
  num_sticks = 0
  #turn: 1-Computer's turn 2-Your turn
  turn = 1

  is_game_ended = False

  num_sticks = int(input("Enter the number of sticks to start the game: "))
  print("==========================================================")


  stick_taken = 0

  while is_game_ended == False:
    while(True):
      if turn == 1:
        print("-------------------- Computer's turn --------------------")
        stick_taken = random.randint(1, 4)
      else:
        print("-------------------- Your turn --------------------")
        stick_taken = int(input("""
You can only take 1, 2, 3 or 4 sticks at a time. 
The number of stick you want to take: 
"""))
      if check_valid_move(stick_taken,num_sticks) == True:
        break;
      else:
        print("Invalid move!")
    print("==========================================================")
    if turn == 1:
      print("Computer took " +str(stick_taken))
    else:
      print("You took " + str(stick_taken))
    
    num_sticks -= stick_taken
    print("Total number of sticks remaining: " + str(num_sticks))
    if num_sticks == 0:
      is_game_ended = True
      print("==========================================================")
      print("Computer won. Good luck next time!!!" if turn == 1 else "You won 🚀!!! Congratulations!")
    turn = 1 if turn == 2 else 2

start_game()
