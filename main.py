import pygame
import functions
import random
import math
import tkinter as tk
from tkinter import messagebox
from functions import snake
pygame.init()


def drawGrid(w, rows, surface):
    gapSize = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + gapSize
        y = y + gapSize
        # Draw the lines                    Start Position    End Position
        pygame.draw.line(surface, functions.WHITE, (x, 0), (x, w))
        pygame.draw.line(surface, functions.WHITE, (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s
    surface.fill(functions.BLACK)
    s.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows, s
    width = 500
    rows = 20
    displayWindow = pygame.display.set_mode((width, width))
    running = True
    clock = pygame.time.Clock()
    s = snake(functions.RED, (10, 10))
    # Main Loop
    while running:
        # Speed
        pygame.time.delay(50)  # Lower = faster
        clock.tick(10)  # Lower = slower
        s.move()
        redrawWindow(displayWindow)


main()
