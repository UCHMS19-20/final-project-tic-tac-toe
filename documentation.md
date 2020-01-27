# What is our game?

The game that my partner Sophia and I chose to create is Tic Tac Toe. In Tic Tac Toe two players play against each other as X's and O.s. The game is played on a 3x3 grid and each player takes a turn placing their piece. Whoever is first to place three of their pieces in a row vertically, horizontally, or diagonally wins the game. 


### Code

import pygame
from pygame.locals import *
 
 #naming the variables
XO   = "X"   # keep track of turns and X goes first
grid = [ [ None, None, None ], \
        [ None, None, None ], \
        [ None, None, None ] ]
 
winner = None
 
 setting support functions
 
def initBoard(abc):
   #representing board as initials
   #abc : ized pyGame display variable
 
   #setting gameboard size/color
   background = pygame.Surface (abc.get_size())
   background = background.convert()
   background.fill ((0, 200, 250))
 
  #creating the grid
  #drawing vertical lines
   pygame.draw.line (background, (250,250,250), (100, 0), (100, 300), 2)
   pygame.draw.line (background, (250,250,250), (200, 0), (200, 300), 2)
 
   #drawing horizontal lines
   pygame.draw.line (background, (250,250,250), (0, 100), (300, 100), 2)
   pygame.draw.line (background, (250,250,250), (0, 200), (300, 200), 2)
 
   #return the board
   return background
 
 
 
def showBoard (abc, board):
   abc.blit (board, (0, 0))
   pygame.display.flip()
  
def boardPos (mouseX, mouseY):
   #determining where the mouse is clicked
 
   #determine the column the click is in
   if (mouseX < 100):
       col = 0
   elif (mouseX < 200):
       col = 1
   else:
       col = 2
 
   #determining the row the click is in
   if (mouseY < 100):
       row = 0
   elif (mouseY < 200):
       row = 1
   else:
       row = 2
 
 
 
   #return the row and column value
   return (row, col)
 
def drawMove (board, boardRow, boardCol, Piece):
 #identifying the center of the grid space
   centerX = ((boardCol) * 100) + 50
   centerY = ((boardRow) * 100) + 50
 
   #drawing x's or o's
   if (Piece == 'O'):
       pygame.draw.circle (board, (250,250,250), (centerX, centerY), 44, 2)
   else:
       pygame.draw.line (board, (250,250,250), (centerX - 22, centerY - 22), \
                        (centerX + 22, centerY + 22), 2)
       pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), \
                        (centerX - 22, centerY + 22), 2)
 
   #draw piece on space
   grid [boardRow][boardCol] = Piece
  
def clickBoard(board):
 
   global grid, XO
  
   (mouseX, mouseY) = pygame.mouse.get_pos()
   (row, col) = boardPos (mouseX, mouseY)
 
   #make sure no one's used this space
   if ((grid[row][col] == "X") or (grid[row][col] == "O")):
       # the current space is occupied
       return
 
   #draw an X or O
   drawMove (board, row, col, XO)
 
   #switching between x's and o's
   if (XO == "X"):
       XO = "O"
   else:
       XO = "X"
  
def gameWon(board):
 
   global grid, winner
 
   #checking for a winning column
   for col in range (0, 3):
       if (grid[0][col] == grid[1][col] == grid[2][col]) and \
          (grid[0][col] is not None):
           # this column won
           winner = grid[0][col]
           pygame.draw.line (board, (153,0,153), ((col + 1)* 100 - 50, 0), \
                             ((col + 1)* 100 - 50, 300), 2)
           break
 
   #checking for a wining row
   for row in range (0, 3):
       if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
          (grid [row][0] is not None)):
           # this row won
           winner = grid[row][0]
           pygame.draw.line (board, (153,0,153), (0, (row + 1)*100 - 50), \
                             (300, (row + 1)*100 - 50), 2)
           break
 
#check for a diagonal win
 
   if (grid[0][2] == grid[1][1] == grid[2][0]) and \
      (grid[0][2] is not None):
       # starting from right to left
       winner = grid[0][2]
       pygame.draw.line (board, (153,0,153), (250, 50), (50, 250), 2)
 
   #check for a diagonal win
   if (grid[0][0] == grid[1][1] == grid[2][2]) and \
      (grid[0][0] is not None):
       # starting from left to right
       winner = grid[0][0]
       pygame.draw.line (board, (153,0,153), (50, 50), (250, 250), 2)
 
 
 
pygame.init()
abc = pygame.display.set_mode ((300, 325))
 
 
#create the game board
board = initBoard (abc)
 
#main event loop
running = 1
 
while (running == 1):
   for event in pygame.event.get():
       if event.type is QUIT:
           running = 0
       elif event.type is MOUSEBUTTONDOWN:
           # the user clicked; place an X or O
           clickBoard(board)
 
       # check for a winner
       gameWon (board)
 
       # update the display
       showBoard (abc, board)

### Presentation

https://docs.google.com/presentation/d/1r1Q4du1eEUxJx_3BhNAu8EnqRP2WI31X6Wc30KhSUhE/edit#slide=id.p
