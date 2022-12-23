import random

def draw_board(board):
  # This function prints the current state of the board
  print(" %c | %c | %c " % (board[0], board[1], board[2]))
  print("---+---+---")
  print(" %c | %c | %c " % (board[3], board[4], board[5]))
  print("---+---+---")
  print(" %c | %c | %c " % (board[6], board[7], board[8]))

def get_move(board, symbol):
  # This function allows the player to enter their move
  while True:
    move = input("Enter your move (1-9): ")
    try:
      move = int(move) - 1
      if move in range(0, 9) and board[move] == " ":
        board[move] = symbol
        return
      else:
        print("Invalid move, try again.")
    except ValueError:
      print("Invalid input, try again.")

def get_ai_move(board, symbol, difficulty):
  # This function allows the artificial opponent to make a move
  # At difficulty 1, the AI simply chooses a random empty cell
  if difficulty == 1:
    while True:
      move = random.randint(0, 8)
      if board[move] == " ":
        board[move] = symbol
        return

  # At difficulty 2, the AI tries to block the player from getting three in a row if possible
  if difficulty == 2:
    # Check if the player can win in the next move, and block them if possible
    for i in range(0, 9):
      if board[i] == " ":
        board[i] = "X"
        if check_win(board, "X"):
          board[i] = "O"
          return
        else:
          board[i] = " "

    # If the player can't win in the next move, choose a random empty cell
    while True:
      move = random.randint(0, 8)
      if board[move] == " ":
        board[move] = symbol
        return

  # At difficulty 3, the AI tries to get three in a row themselves if possible
  if difficulty == 3:
    # Check if the AI can win in the next move, and play the winning move if possible
    for i in range(0, 9):
      if board[i] == " ":
        board[i] = "O"
        if check_win(board, "O"):
          return
        else:
          board[i] = " "

    # If the AI can't win in the next move, try to block the player if possible
    for i in range(0, 9):
      if board[i] == " ":
        board[i] = "X"
        if check_win(board, "X"):
          board[i] = "O"
          return
        else:
          board[i] = " "

    # If the AI can't win and the player can't win in the next move, choose a random empty cell
    while True:
      move = random.randint(0, 8)
      if board[move] == " ":
        board[move] = symbol
        return

def check_win(board, symbol):
  # This function checks if a player has won the game
  for i in range(0, 3):
    # Check rows
    if board[i * 3] == symbol and board[i * 3 + 1] == symbol and board[i * 3 + 2] == symbol:
      return True
    # Check columns
    if board[i] == symbol and board[i + 3] == symbol and board[i + 6] == symbol:
      return True
  # Check diagonals
  if board[0] == symbol and board[4] == symbol and board[8] == symbol:
    return True
  if board[2] == symbol and board[4] == symbol and board[6] == symbol:
    return True
  return False

def main():
  # Main function to play the game
  board = [" " for i in range(0, 9)]
  difficulty = int(input("Enter difficulty (1-3): "))
  draw_board(board)
  while True:
    get_move(board, "X")
    draw_board(board)
    if check_win(board, "X"):
      print("You win!")
      break
    elif not " " in board:
      print("Draw.")
      break
    get_ai_move(board, "O", difficulty)
    draw_board(board)
    if check_win(board, "O"):
      print("AI wins!")
      break
    elif not " " in board:
      print("Draw.")
      break

# Run the game
main()
