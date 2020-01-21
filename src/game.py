import pygame

X1 = "x"
# tells the turn; X1 means "x" goes first
grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]
winner = None
# declares supporting functions

def __init__board(abc):
    """init = initialize ; board is initialized and turned into a variable; 
    "abc" is the pygame display variable"""
    background = pygame.Surface(abc.get_size())
    background = background.convert()
    background.fill = ((250,250,250))
    # sets the background of the game a light purple color

    pygame.draw.line(background, (0,0,0), (100,0), (100,300), 2)
    pygame.draw.line(background, (0,0,0), (100,0), (200,300), 2)
    # drawing vertical lines for the grid
    pygame.draw.line(background, (0,0,0), (0,100), (300,100), 2)
    pygame.draw.line(background, (0,0,0), (0,100), (300,200), 2)
    # drawing horizontal lines for the grid
    return background
    # returns a drawn board

    def board_postion(x_click, y_click):
        """the mouse gives coordinates to figure out
         the space on the board (row, column) the user clicked
         x_click = x coordinate & y_click = y coordinate  """
        if (y_click < 100):
                row = 0
        elif (y_click < 200):
                row = 1
        else:
                row = 2
# shows the row clicked by the player
        if (x_click < 100):
                column = 0
        elif (x_click < 200):
                column = 1
        else:
                column = 2
# shows the column clicked by the player

def draw_move(board, b_row, b_col, piece):
        """ board = surface of game,
         b_row & b_col = row and column to draw the piece, 
         piece = X or O"""

        middle_X = ((b_col) * 100) + 50
        middle_Y = ((b_row) * 100) + 50
# shows center of the square board

        if (piece == 'O'):
                pygame.draw.circle (board, (0,0,0), (middle_X, middle_Y), 44, 2)
        else:
                pygame.draw.line (board, (0,0,0), (middle_X - 22, middle_Y - 22),
                        (middle_X + 22, middle_Y + 22), 2)
                pygame.draw.line (board, (0,0,0), (middle_X + 22, middle_Y - 22), 
                        (middle_X - 22, middle_Y + 22), 2)
# draws pieces X or O

        grid[b_row][b_col] = piece
# marks space as used

def click_Board(board):
   """determine where the user clicked and if the
    space is not already occupied, draw the appropriate
     piece there (X or O); board = game board surface"""
  
   global grid, XO
  
   (x_click, y_click) = pygame.mouse.get_pos()
   (row, col) = board_position(x_click, y_click)
 
   # makes sure no used the space
   if ((grid[row][col] == "X") or (grid[row][col] == "O")):
       # the space has been used
       return
 
   # draw an X or O
   draw_move (board, row, col, XO)
 
   # toggle XO to the other player's move
   if (XO == "X"):
       XO = "O"
   else:
       XO = "X"
  
def game_won(board):
   """determine if anyone has won the game;
    board = the game board surface"""
  
   global grid, winner
 
   # check for winning rows
   for row in range (0, 3):
       if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
          (grid [row][0] is not None)):
           # this row won
           winner = grid[row][0]
           pygame.draw.line (board, (250,0,0), (0, (row + 1)*100 - 50), \
                             (300, (row + 1)*100 - 50), 2)
           break
 
   # check for winning columns
   for col in range (0, 3):
       if (grid[0][col] == grid[1][col] == grid[2][col]) and \
          (grid[0][col] is not None):
           # this column won
           winner = grid[0][col]
           pygame.draw.line (board, (250,0,0), ((col + 1)* 100 - 50, 0), \
                             ((col + 1)* 100 - 50, 300), 2)
           break
 
   # check for diagonal winners
   if (grid[0][0] == grid[1][1] == grid[2][2]) and \
      (grid[0][0] is not None):
       # game won diagonally left to right
       winner = grid[0][0]
       pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)
 
   if (grid[0][2] == grid[1][1] == grid[2][0]) and \
      (grid[0][2] is not None):
       # game won diagonally right to left
       winner = grid[0][2]
       pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)
 
# initialize pygame and our window
pygame.init()
abc = pygame.display.set_mode ((300, 325))
pygame.display.set_caption ('TicTacToe')
 
# create the game board
board = __init__board(abc)
 
# main event loop
running = 1
 
while (running == 1):
   for event in pygame.event.get():
       if event.type is quit:
           running = 0
       elif event.type is mousebuttondown:
           # the user clicked; place an X or O
           click_Board(board)
 
       # check for a winner
       game_won (board)
 
       # update the display
       show_board(abc, board)
