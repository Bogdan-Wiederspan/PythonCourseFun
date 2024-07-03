from objects import OrangeBrick, GreenBrick, RedBrick
from constants import WIDTH, HEIGHT, GRAY, BLACK
import pygame

def grid(screen):
    # create a starting grid of bricks
    bricks = []

    for column in range(20):
        for row in range(6):
            if row < 1:
                bricks.append(OrangeBrick(column, row, screen=screen))
            elif row < 3:
                bricks.append(GreenBrick(column, row, screen=screen))
            elif row < 6:
                bricks.append(RedBrick(column, row, screen=screen))
    num_of_bricks = len(bricks)
    return bricks, num_of_bricks

def check_collision(objA, objB):
    # returns True if the ball collides with the object
    return objA.rect.colliderect(objB)


def pause(func, *args, **kwargs):
    """
    Wrapper to pause other functions until press key p, then continue.
    This is a generic pause function.
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
    screen.fill(GRAY)
    width, height = screen.get_size()
    pygame.draw.line(surface=screen, color=BLACK, start_pos=(0, HEIGHT), end_pos=(WIDTH, HEIGHT))
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over!", 1, BLACK)
    screen.blit(text, (width // 2, height // 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False


@pause
def win(screen):
    """
    Show you won message and end game loop after pressing p.
    """
    pause_mode = True
    while pause_mode:
        font = pygame.font.Font(None, 25)
        width, height = screen.get_size()
        text = font.render("You Won! Press p to end", 1, BLACK)
        screen.blit(text, (width // 2, height // 2))
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
    screen.fill(GRAY)
    pygame.draw.line(surface=screen, color=BLACK, start_pos=(0, height), end_pos=(widht, height))

    # score and live text, this is updated every cycle
    # clear font
    font = pygame.font.Font(None, 34)
    # render text
    text = font.render(f"Score: {score}", 1, BLACK)
    text_screen_position = screen.get_height() - 40
    screen.blit(text, (20, text_screen_position))
    text = font.render(f"Lives: {lives}", 1, BLACK)
    screen.blit(text, (160, text_screen_position))
