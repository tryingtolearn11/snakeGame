import pygame
import sys
import functions
import tkinter as tk
from tkinter import messagebox
from functions import snake
from functions import cell, randomFood


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def drawGrid(w, rows, surface, displayGRID):
    gapSize = 500 // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + gapSize
        y = y + gapSize
        if displayGRID:
            # Draw the lines                    Start Position    End Position
            pygame.draw.line(surface, functions.GREY, (x, 0), (x, 500))
            pygame.draw.line(surface, functions.GREY, (0, y), (500, y))


def redrawWindow(surface):
    displayGRID = True
    global rows, width, s, apple
    surface.fill(functions.BLACK)
    # Drawing Visible Grid Option Button
    gridbox = pygame.Rect(20, 520, 90, 20)
    pygame.draw.rect(surface, functions.WHITE, gridbox)
    # Drawing Text to screen
    font = pygame.font.SysFont('didot.ttc', 20)
    img = font.render('Toggle Grid', True, functions.BLACK)
    testRectObj = img.get_rect()
    testRectObj.center = (30, 524)
    grid = surface.blit(img, testRectObj.center)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if grid.collidepoint(pos) and pressed1:
        displayGRID = False
    # LETS MAKE A TITLE Text
    # Drawing Text to screen
    font2 = pygame.font.SysFont('chalkduster.ttc', 60)
    img2 = font2.render('SNAKE', True, functions.GREEN)
    testRectObj2 = img2.get_rect()
    testRectObj2.center = (200, 520)
    surface.blit(img2, testRectObj2.center)
    # Draw rest of the Game
    s.draw(surface)
    apple.draw(surface)
    drawGrid(width, rows, surface, displayGRID)
    pygame.display.update()


def main():
    pygame.init()
    global width, rows, s, apple
    width = 570
    rows = 20
    displayWindow = pygame.display.set_mode((515, width))
    pygame.display.set_caption("Snake Game")
    running = True
    clock = pygame.time.Clock()
    s = snake(functions.BLUE, (10, 10))
    apple = cell(randomFood(rows, s), color=functions.RED)
    # Main Loop
    while running:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == apple.pos:
            s.addCell()
            apple = cell(randomFood(rows, s), color=functions.RED)

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('Play Again? Your Score was: ', len(s.body))
                s.reset((10, 10))
                break

            redrawWindow(displayWindow)


main()
