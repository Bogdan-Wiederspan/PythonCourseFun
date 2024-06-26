import pygame

ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PIXEL_BUFFER = 2

def grid(screen):
    # create a starting grid
    width = screen.get_width()
    height = screen.get_height()

    bricks = []

    for column in range(20):
        column_bricks = []
        for row in range(6):
            if row < 1:
                column_bricks.append(OrangeBrick(column, row))
            elif row < 3:
                column_bricks.append(GreenBrick(column, row))
            elif row < 6:
                column_bricks.append(RedBrick(column, row))
        bricks.append(column_bricks)
    num_of_bricks = len(bricks) * len(bricks[0])
    return bricks, num_of_bricks

class Brick:
    def __init__(self, column, row, color, score, *, width=20, height=20):
        self.x = column * width
        self.y = row * height
        # reduce actual widht and height by PIXEL_BUFFER to avoid overlap
        self.width = width - PIXEL_BUFFER
        self.height = height - PIXEL_BUFFER
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # score of the brick
        self.score = score

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class EmptyBrick(Brick):
    def __init__(self, column, row):
        super().__init__(column, row, (0, 0, 0), 0)

class RedBrick(Brick):
    def __init__(self, column, row):
        super().__init__(column, row, RED, 1)

class GreenBrick(Brick):
    def __init__(self, column, row):
        super().__init__(column, row, GREEN, 2)

class OrangeBrick(Brick):
    def __init__(self, column, row):
        super().__init__(column, row, ORANGE, 3)
