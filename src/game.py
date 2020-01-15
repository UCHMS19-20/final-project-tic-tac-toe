import pygame
<<<<<<< HEAD
import sys

width, height = 600, 600
cell_count = 3
cell_size = width/cell_count

grid = []

class Cell:

    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.sz = sz
        self.filled = False
        self.rectangle = pygame.Rect(self.x * sz, self.y * sz, sz, sz)

    def show(self):
        pygame.draw.rect(screen, pygame.Color("pink"), self.rectangle, 2)
        if self.filled:
            pygame.draw.rect(screen, pygame.Color("pink"), self.rectangle)

pygame.init()

screen = pygame.display.set_mode((width, height))

for y in range(cell_count):
    for x in range(cell_count):
        grid.append(Cell(x, y, cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
=======

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
    background = pygame.surface(abc.get_size())
    background = background.convert()
    background.fill = ((153,0,153))
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
>>>>>>> 29d00cdd30c7f3d85abff0164e5e0abc38612b56

    # pygame.draw.rect(screen, pygame.Color("red"), (0,0,50,50))
    for cell in grid:
        if cell.rectangle.collidepoint(pygame.mouse.get_pos()):
            cell.filled = True
        cell.show()


    pygame.display.flip() 