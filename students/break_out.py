import pygame
from objects import Paddle, Ball, grid, EmptyBrick
pygame.init()

# colorspace & constants
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
MAX_BALL_SPEED = 8

# (400 x 600) 20 stones a 20 pixels widht, 30 stones a 20 pixels
WIDTH, HEIGHT = (20 * 20, 30 * 20)

score = 0
lives = 3
run_game_loop = True

# Set up the game window
FONT_BUFFER_PIXEL = 50
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + FONT_BUFFER_PIXEL))
pygame.display.set_caption("Break Out")

clock = pygame.time.Clock()

# init our object instances
paddle = Paddle(WIDTH // 2, HEIGHT - 50, RED, screen=SCREEN, width=100, height=20, speed=7.5)
ball = Ball(WIDTH // 2, HEIGHT // 2, BLUE, screen=SCREEN, speed=4)
bricks, num_of_bricks = grid(screen=SCREEN)

# set up music and sound effects
sound_folder = './sounds'
pygame.mixer.music.load(f'{sound_folder}/stage.mp3')
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(0.2)

sfx_hit_brick = pygame.mixer.Sound(f'{sound_folder}/brick_hit.wav')
sfx_hit_brick.set_volume(0.05)
sfx_death = pygame.mixer.Sound(f'{sound_folder}/death.wav')
sfx_death.set_volume(0.1)

# YOU START CODING HERE
while run_game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game_loop = False

    # screen clearing and drawing
    # background
    SCREEN.fill(GRAY)
    pygame.draw.line(surface=SCREEN, color=BLACK, start_pos=(0, HEIGHT), end_pos=(WIDTH, HEIGHT))

    # add score and live text

    # add draw all elements

    # game logic
    # add movement

    # collision detection
    # ball and wall
    for num_brick, brick in enumerate(bricks):
        brick.draw()
        if ball.collide(brick):
            # add increase score
            # add remove brick
            # add reverse the direction of the ball and increase speed

    # ball and paddle
    if ball.collide(paddle):
        # add increase speed by 10% each time the ball hits the paddle

    # win and loose conditions
    # add win condtion and display text

    # add loose condition and display text
    # add pause the game until press p

    # add if no lives left, game over

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
pygame.quit()
