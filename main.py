import pygame
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


def drawGrid(w, rows, surface):
    gapSize = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + gapSize
        y = y + gapSize
        # Draw the lines                    Start Position    End Position
        pygame.draw.line(surface, functions.GREY, (x, 0), (x, w))
        pygame.draw.line(surface, functions.GREY, (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s, apple
    surface.fill(functions.BLACK)
    s.draw(surface)
    apple.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows, s, apple
    width = 500
    rows = 20
    displayWindow = pygame.display.set_mode((width, width))
    running = True
    clock = pygame.time.Clock()
    s = snake(functions.BLUE, (10, 10))
    apple = cell(randomFood(rows, s), color=(255, 0, 0))
    # Main Loop
    while running:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == apple.pos:
            s.addCell()
            apple = cell(randomFood(rows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

            redrawWindow(displayWindow)


main()
