print("Welcome to our game of Tic Tac Toe")

import pygame
import sys

Black = (0, 0, 0)
White = (255, 255, 255)
Pink = (240, 128, 128)
DPink = (205, 92, 92)

width = 3
height = 3

margin = 0.1

grid = []
for row in range(3):
    # Added an empty array to hold each cell
    # in this row
    grid.append([])
    for column in range(3):
        grid[row].append(0)  # Append a cell

grid = [[0 for x in range(3)] for y in range(3)]

pygame.init()
# initialize pygame

# Set the HEIGHT and WIDTH of the screen
window_size = [255, 255]
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("TIC TAC TOE")
# Makes title for the game



screen.fill(White)
#set screen with a white background

for row in range(3):
    for column in range(3):
        color = Black
        if grid [row][column] == 1:
            color = Pink
        pygame.draw.rect(screen,
                         color,
                         [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])
#drawing the grid

     # update the screen with what we've drawn
    pygame.display.flip()




