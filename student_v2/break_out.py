import pygame
from objects import Paddle, Ball, EmptyBrick
from util import grid, check_collision, game_over, press_continue, win
from constants import WIDTH, HEIGHT, RED, BLUE
pygame.init()

score = 0
lives = 3
run_game_loop = True

# Set up the game window
# buffer for font on the bottom of the screen
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

while run_game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game_loop = False

    # ADD CODE HERE
    # draw all elements

    # game logic
    # movement


    # collision detection
    # ball and wall

    for num_brick, brick in enumerate(bricks):
        # ADD CODE HERE
        # draw brick
        # check if ball collides with brick
        is_collision = check_collision(ball, brick)
        not_empty_brick = not isinstance(brick, EmptyBrick)
        if is_collsion and not_empty_brick:
            # ADD CODE HERE
            # play sound
            # increase score
            # decrease number of bricks
            # remove brick
            # reverse the direction of the ball and increase speed

    # ball and paddle interaction
    # ADD CODE HERE
    # check if ball collides with paddle

    # ADD CODE HERE
    # win and loose conditions, use win from util.py

    # ADD CODE HERE
    # loose condition
    # decrease lives, reset ball
    loose_live_condition = ball.y >= HEIGHT
    if loose_live_condition:
        # ADD CODE HERE
        # if no lives left, game over
        loose_game_condition = lives == 0
        if loose_game_condition:
            run_game_loop = game_over(SCREEN)

        press_continue(SCREEN)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
pygame.quit()
