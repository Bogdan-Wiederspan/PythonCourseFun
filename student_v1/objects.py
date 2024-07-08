import pygame
import random

ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class BaseObject:

    def __init__(
        self,
        x: int,
        y: int,
        color: tuple[int, int, int],
        *,
        width: int,
        height: int,
        screen: pygame.Surface
    ):
        """
            A base class for objects in a breakout game.

            This class provides the basic attributes and initialization for game objects,
            including position, size, color, and an optional screen for rendering.
            But also the basic draw method.

        Attributes:
            screen (pygame.Surface): Game screen on which the object is rendered. Default is None.
            x (int): The x-coordinate of the object's position.
            y (int): The y-coordinate of the object's position.
            width (int): The width of the object.
            height (int): The height of the object.
            color (tuple): The color of the object, defined as an RGB tuple.
            rect (pygame.Rect): The rectangle representing the object's shape and position.

        Parameters:
            x (int): The initial x-coordinate of the object.
            y (int): The initial y-coordinate of the object.
            color (tuple): The color of the object, defined as an RGB tuple.
            width (int): The width of the object.
            height (int): The height of the object.
            screen (pygame.Surface): Game screen on which the object is rendered. Defaults to None.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        """
        Draw the object to the current screen using the object's color and rectangle.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)


class Paddle(BaseObject):
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple[int, int, int],
        screen: pygame.Surface,
        *,
        width: int = 50,
        height: int = 20,
        speed: int = 10,

    ) -> None:
        """
        Initializes a paddle object for the breakout game, inheriting from BaseObject.

        The paddle can move horizontally across the screen within the screen boundaries.
        Movement is controlled by the left and right arrow keys.

        Attributes:
            speed (int): The speed at which the paddle moves.

        Parameters:
            x (int): The initial x-coordinate of the paddle.
            y (int): The initial y-coordinate of the paddle.
            color (tuple[int, int, int]): The color of the paddle, defined as an RGB tuple.
            width (int, optional): The width of the paddle. Defaults to 50.
            height (int, optional): The height of the paddle. Defaults to 20.
            speed (int, optional): The speed at which the paddle moves. Defaults to 5.
        """
        pass

    def move(self) -> None:
        """
        Handles the movement of the paddle based on user input.

        The paddle moves left or right when the left or right arrow keys are pressed,
        respectively. It does not move beyond the screen's boundaries.

        Parameters:
            screen (pygame.Surface): The game screen to which the paddle's movement is relative.
        """
        # get the pressed keys

        # movement with bound checks


class Ball(BaseObject):
    def __init__(self, x, y, color, screen, *, radius=10, speed=5, direction_x=1, direction_y=1):
        super().__init__(x, y, color, width=radius, height=radius, screen=screen)
        # balls are squares, so width and height are the same
        self.radius = radius
        self.start_speed = speed
        self.speed = speed

        # > 0 (right, down), < 0 (left, up)
        self.direction_x = direction_x
        self.direction_y = direction_y

        self.reset()

    def reset(self):
        # random start position and direction
        width_half = self.screen.get_width() // 2
        height_half = self.screen.get_height() // 2
        self.x = random.randint(width_half - 150, width_half + 150)
        self.y = random.randint(height_half - 50, height_half + 50)

        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

        self.speed = self.start_speed

    def move(self):
        # move the ball

        # check if the ball hits the wall
        # lower wall is not checked, because the game is lost if it hits the lower wall
        pass

    def collide(self, collision_object) -> bool:
        # returns True if the ball collides with the object
        return self.rect.colliderect(collision_object)


def grid(screen):
    # create a starting grid of bricks
    bricks = []
    # 1 row of orange bricks, 2 rows of green bricks, 3 rows of red bricks
    for column in range(20):
        # create a row of bricks

    return bricks

class Brick(BaseObject):
    PIXEL_BUFFER = 2

    def __init__(self, column, row, color, score, screen, *, width=20, height=20):
        super().__init__(column * width, row * height, color, width=width, height=height, screen=screen)
        # reduce actual widht and height by PIXEL_BUFFER to avoid overlap
        self.width = width - self.PIXEL_BUFFER
        self.height = height - self.PIXEL_BUFFER

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # score of the brick
        self.score = score


class EmptyBrick(Brick):
    def __init__(self, column, row, screen):
        # no score, no color
        pass


class RedBrick(Brick):
    def __init__(self, column, row, screen):
        # score 1, red color
        pass


class GreenBrick(Brick):
    def __init__(self, column, row, screen):
        # score 2, green color
        pass


class OrangeBrick(Brick):
    def __init__(self, column, row, screen):
        # score 3, orange color
        pass
