import pygame

class Ball:
    def __init__(self, x, y, color, *, radius=10, speed=5):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.rect = pygame.Rect(x, y, radius, radius)
        # > 0 means right, < 0 means left
        self.direction_x = 1
        # > 0 means down, < 0 means up
        self.direction_y = 1


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, screen):
        # move the ball
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y
        # update the rect
        self.rect.topleft = (self.x, self.y)
        # check if the ball hits the wall
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.direction_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.direction_y *= -1

    def collide(self, collision_object) -> bool:
        # returns True if the ball collides with the object
        return self.rect.colliderect(collision_object)
