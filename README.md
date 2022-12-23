# Tic-Tac-Toe

This is a simple game of tic-tac-toe in which a player can play against an artificial intelligence (AI) opponent. The game is played on a 3x3 board, with the player taking turns to place their symbol ('X' or 'O') on an empty cell. The game ends when a player gets three in a row, or when there are no more empty cells on the board.
The game consists of several functions:

## How to Play

1. Clone this repository and navigate to the directory containing the code.
2. Run the game by entering python tic-tac-toe.py in the command line.
3. The game will prompt you to enter the difficulty level (1, 2, or 3). At difficulty 1, the AI simply chooses a random empty cell. At difficulty 2, the AI tries to block you from getting three in a row if possible. At difficulty 3, the AI tries to get three in a row themselves if possible.
4. The game will then alternate between you and the AI making moves until the game is won or there are no more empty cells on the board.
5. The game will display the current state of the board after each move.

## Function Descriptions

- **draw_board()** takes a board as input and prints the current state of the board to the console
- **get_move()** prompts the player to enter their move and updates the board with the player's symbol
- **get_ai_move()** allows the AI to make a move based on the difficulty level specified by the player (1, 2, or 3). At difficulty 1, the AI simply chooses a random empty cell. At difficulty 2, the AI tries to block the player from getting three in a row if possible. At difficulty 3, the AI tries to get three in a row themselves if possible. If the AI can't win and the player can't win in the next move, the AI chooses a random empty cell.
- **check_win()** checks if a player has won the game by checking for three in a row on the board. It returns True if a player has won, and False otherwise.
- **main()** is the main function that plays the game. It initializes the board, prompts the player to specify the difficulty level, and then alternates between the player and the AI making moves until the game is won or there are no more empty cells on the board. The game ends in a draw if there are no more empty cells and no player has won.
