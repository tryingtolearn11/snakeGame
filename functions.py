
import pygame
import sys
import random

# Colors
#       R  G  B
RED = (255, 0, 0,)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BGCOLOR = (40, 100, 255)


class cell(object):
    rows = 20
    w = 500

    def __init__(self, start, dirX=0, dirY=1, color=BLUE):
        self.pos = start
        self.dirX = 1
        self.dirY = 0
        self.color = color

    def move(self, dirX, dirY):
        self.dirX = dirX
        self.dirY = dirY
        self.pos = (self.pos[0] + self.dirX, self.pos[1] + self.dirY)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]  # x direction ROW
        j = self.pos[1]  # y direction COLUMN
        # draw cell
        # ---------------------- We draw cube but we want it be within the grid
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            radius = 3
            circleMid = (i*dis+center - radius, j*dis+8)
            circleMid2 = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, BLACK, circleMid, radius)
            pygame.draw.circle(surface, BLACK, circleMid2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cell(pos)
        self.body.append(self.head)
        # Keep track of direction we move in
        self.dirX = 0
        self.dirY = 1

    # Moving Function for the snake
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Gives list of keys pressed
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_a]:
                    self.dirX = -1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_d]:
                    self.dirX = 1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_w]:
                    self.dirX = 0
                    self.dirY = -1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_s]:
                    self.dirX = 0
                    self.dirY = 1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
        # Look thru list of Positions of the snake
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
        # Lets check if we have reached the edge of the screen
            else:
                if c.dirX == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirX == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirY == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirY == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirX, c.dirY)

    def reset(self, pos):
        self.head = cell(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCell(self):
        tail = self.body[-1]
        dx, dy = tail.dirX, tail.dirY

        if dx == 1 and dy == 0:
            self.body.append(cell((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cell((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cell((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cell((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirX = dx
        self.body[-1].dirY = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # Find the snake so we add eyes for the HEAD
                c.draw(surface, True)
            else:
                c.draw(surface)


def randomFood(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)
