from objects import OrangeBrick, GreenBrick, RedBrick
from constants import WIDTH, HEIGHT, GRAY, BLACK
import pygame


def grid(screen):
    # create a starting grid of bricks
    bricks = []

    # 1 row of orange bricks, 2 rows of green bricks, 3 rows of red bricks
    for column in range(20):
        # ADD CODE HERE
    # return bricks and number of bricks
    # num of bricks is used to calculate the win condition
    pass


def check_collision(objA, objB):
    # returns True if the ball collides with the object
    return objA.rect.colliderect(objB)


def pause(func, *args, **kwargs):
    """
    Wrapper to pause other functions until press key p, then continue.
    This is a generic pause function.

    We used this function way to often, so we decided to make a generic one
    """
    def wrapper(*args, **kwargs):
        pause_mode = True
        while pause_mode:
            func(*args, **kwargs)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause_mode = False
    return wrapper


@pause
def game_over(screen):
    """
    Set up the game over screen
    """
    # see win function for how to set up the screen
    # first CLEAR the screen
    # ADD CODE HERE

    # render text
    # ADD CODE HERE
    # wait for key press to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False


@pause
def win(screen):
    """
    Show you won message and end game loop after pressing p.
    """
    font = pygame.font.Font(None, 25)
    width, height = screen.get_size()
    text = font.render("You Won! Press p to end", 1, BLACK)
    screen.blit(text, (width // 2, height // 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return False


@pause
def press_continue(screen):
    """
    Pause the game until press p, then continue
    """
    font = pygame.font.Font(None, 25)
    width, height = screen.get_size()
    text = font.render("Press p to continue", 1, BLACK)
    screen.blit(text, (width // 2, height // 2))
    pygame.display.flip()


def draw_static_background(screen, height=HEIGHT, widht=WIDTH, score=0, lives=3):
    # screen clearing and drawing
    # background
    # ADD CODE HERE
    screen.fill(GRAY)
    pygame.draw.line(surface=screen, color=BLACK, start_pos=(0, height), end_pos=(widht, height))

    # score and live text, this is updated every cycle
    # clear font
    font = pygame.font.Font(None, 34)
    # render scores and lives at bottom
    # ADD CODE HERE
