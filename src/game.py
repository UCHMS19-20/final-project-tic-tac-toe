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


