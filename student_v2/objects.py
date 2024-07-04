import pygame
import random
from constants import ORANGE, GREEN, RED


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

    def move(self):
        # no code adjustment needed
        pass


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
        # ADD CODE HERE
        # super call to the parent class
        # set speed as an attribute
        pass

    def move(self) -> None:
        """
        Handles the movement of the paddle based on user input.

        The paddle moves left or right when the left or right arrow keys are pressed,
        respectively. It does not move beyond the screen's boundaries.

        Parameters:
            screen (pygame.Surface): The game screen to which the paddle's movement is relative.
        """
        # ADD CODE HERE
        # get the pressed keys

        # movement with bound checks
        # add bound checks for the left and right sides of the screen

        # adjust the paddle's x-coordinate based on the pressed keys and bound checks


class Ball(BaseObject):
    def __init__(self, x, y, color, screen, *, radius=10, speed=5, direction_x=1, direction_y=1, max_speed=10):
        super().__init__(x, y, color, width=radius, height=radius, screen=screen)
        # balls are squares, so width and height are the same
        self.radius = radius
        self.speed = speed
        self.initial_speed = speed
        self.max_speed = max_speed

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

        self.speed = self.initial_speed

    def move(self):
        # ADD CODE HERE
        # move the ball

        # check if the ball hits the wall
        left_wall = self.rect.left <= 0
        right_wall = self.rect.right >= self.screen.get_width()
        up_wall = self.rect.top <= 0

        # adjust the direction of the ball based on the wall hits

    def collide_with_paddle(self):
        """
        Modify ball direction when it hits the paddle
        """
        # ADD CODE HERE
        # add paddle collision logic
        # adjust speed, but try to keep it within the max_speed limit
        pass

    def collide_with_brick(self, side=None):
        """
        Modify ball direction and speed when it hits a brick.
        Depending on the side of the brick that the ball hits.

        side (str): The side of the brick that the ball hits.
        """
        # ADD CODE HERE
        # add brick collision logic
        # when hit lef or right side, change x direction
        # always change y

        # change speed


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

    def side_hit(self, x):
        side = None
        # ADD CODE HERE
        # define which side of the brick was hit
        # x is the x-coordinate of the ball
        # get the side coordinate by rect.left and rect.right
        return side


class EmptyBrick(Brick):
    def __init__(self, column, row, screen):
        # ADD CODE HERE
        # no score, no color, use inherited __init__ method


class RedBrick(Brick):
    def __init__(self, column, row, screen):
        # ADD CODE HERE
        # score 1, color RED, use inherited __init__ method


class GreenBrick(Brick):
    def __init__(self, column, row, screen):
        # ADD CODE HERE
        # score 2, color GREEN, use inherited __init__ method


class OrangeBrick(Brick):
    def __init__(self, column, row, screen):
        # ADD CODE HERE
        # score 3, color ORANGE, use inherited __init__ method
