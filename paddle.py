import pygame

class Paddle:
    def __init__(self, x, y, color, *, width=50, height=20,speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        # rectangles are easy to draw in pygame
        # just need the screen, color and rect object
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, screen):
        # get the pressed keys
        keys = pygame.key.get_pressed()
        # check which key is pressed AND
        # make sure the paddle does not go out of bounds
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            # when at the left edge, the x coordinate is 0 return back by speed
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen.get_width():
            self.rect.x += self.speed

    def collide(self, ball):
        return self.rect.colliderect(ball.rect)

