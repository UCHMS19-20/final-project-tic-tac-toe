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

pygame.init()
# initialize pygame

# Set the HEIGHT and WIDTH of the screen
window_size = [255, 255]
screen = pygame.display.set_mode(window_size)





