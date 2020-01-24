import pygame

# naming the pieces as variables
XO = "X"
# keep track of turns and X goes first
grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]

winner = None

# setting supporting functions

def init_board(abc):
    # representing the gameboard as initials
    #abc : pygame display variable

    #setting gameboard size/color
    background = pygame.Surface (abc.get_size())
    background = background.convert()
    background.fill ((0,200,250))
    
    #creating the grid
    #drawing the vertical lines
    pygame.draw.line(background, (250,250,250), (100,0), (100,300), 2)
    pygame.draw.line(background, (250,250,250), (200,0), (200,300), 2)
    
    # drawing horizontal lines
    pygame.draw.line(background, (250,250,250), (0,100), (300,100), 2)
    pygame.draw.line(background, (250,250,250), (0,200), (300,200), 2)
    
    return background
    # returns a drawn board ^^

def show_board (abc, board):
    abc.blit (board, (0, 0))
    pygame.display.flip()


def board_postion (mouseX, mouseY):
        """the mouse gives coordinates to figure out
         the space on the board (row, column) the user clicked
         x_click = x coordinate & y_click = y coordinate  """
        if (mouseY < 100):
                row = 0
        elif (mouseY < 200):
                row = 1
        else:
                row = 2
# shows the row clicked by the player ^^
        if (mouseX < 100):
                column = 0
        elif (mouseX < 200):
                column = 1
        else:
                column = 2
# shows the column clicked by the player ^^
        return (row, col)

def draw_move(board, boardrow, boardcol, piece):
        """ board = surface of game,
         boardrow & boardcol = row and column to draw the piece, 
         piece = X or O"""

        middle_X = ((boardcol) * 100) + 50
        middle_Y = ((boardrow) * 100) + 50
# shows center of the square board ^^

        if (piece == 'O'):
                pygame.draw.circle (board, (250,250,250), (middle_X, middle_Y), 44, 2)
        else:
                pygame.draw.line (board, (250,250,250), (middle_X - 22, middle_Y - 22),
                        (middle_X + 22, middle_Y + 22), 2)
                pygame.draw.line (board, (0,0,0), (middle_X + 22, middle_Y - 22), 
                        (middle_X - 22, middle_Y + 22), 2)
# draws pieces X or O

        grid[boardrow][boardcol] = piece
# marks space as used

def click_Board(board):
   """determine where the user clicked and if the
    space is not already occupied, draw the appropriate
     piece there (X or O); board = game board surface"""
  
   global grid, XO
  
   (mouseX, mouseY) = pygame.mouse.get_pos()
   (row, col) = board_position(mouseX, mouseY)
 
   # makes sure no used the space
   if ((grid[row][col] == "X") or (grid[row][col] == "O")):
       # the space has been used
       return
 
   # draw an X or O
   draw_move (board, row, col, XO)
 
   # toggle X1 to the other player's move
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
           pygame.draw.line (board, (153,0,153), (0, (row + 1)*100 - 50), \
                             (300, (row + 1)*100 - 50), 2)
           break
 
   # check for winning columns
   for col in range (0, 3):
       if (grid[0][col] == grid[1][col] == grid[2][col]) and \
          (grid[0][col] is not None):
           # this column won
           winner = grid[0][col]
           pygame.draw.line (board, (153,0,153), ((col + 1)* 100 - 50, 0), \
                             ((col + 1)* 100 - 50, 300), 2)
           break
 
   # check for diagonal winners
   if (grid[0][0] == grid[1][1] == grid[2][2]) and \
      (grid[0][0] is not None):
       # game won diagonally left to right
       winner = grid[0][0]
       pygame.draw.line (board, (153,0,153), (50, 50), (250, 250), 2)
 
   if (grid[0][2] == grid[1][1] == grid[2][0]) and \
      (grid[0][2] is not None):
       # game won diagonally right to left
       winner = grid[0][2]
       pygame.draw.line (board, (153,0,153), (250, 50), (50, 250), 2)
 
# initialize pygame and our window
pygame.init()
abc = pygame.display.set_mode ((300, 325))

 
# create the game board
board = init_board(abc)
 
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
