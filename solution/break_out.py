import pygame
from objects import Paddle, Ball, EmptyBrick
from util import grid, check_collision, game_over, press_continue, win, draw_static_background
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

    # draw background
    draw_static_background(
        SCREEN,
        height=HEIGHT,
        widht=WIDTH,
        score=score,
        lives=lives)

    # draw all elements
    paddle.draw()
    ball.draw()

    # game logic
    # movement
    paddle.move()
    ball.move()

    # collision detection
    # ball and wall
    for num_brick, brick in enumerate(bricks):
        brick.draw()
        if check_collision(ball, brick) and not isinstance(brick, EmptyBrick):
            pygame.mixer.Sound.play(sfx_hit_brick)
            score += brick.score
            num_of_bricks -= 1
            # replace the brick with an empty brick that has the same position
            # pop(num_brick) is an alternativ way, but creates graphic bugs
            bricks[num_brick] = EmptyBrick(brick.x, brick.y, screen=brick.screen)
            # bricks.pop(num_brick)
            # reverse the direction of the ball and increase speed
            side_hit = brick.side_hit(ball.x)
            ball.collide_with_brick(side_hit)

    # ball and paddle interaction
    if check_collision(ball, paddle):
        ball.collide_with_paddle()

    # win and loose conditions
    win_condition = num_of_bricks == 0
    if win_condition:
        run_game_loop = win(SCREEN)

    loose_live_condition = ball.y >= HEIGHT
    if loose_live_condition:
        pygame.mixer.Sound.play(sfx_death)
        lives -= 1
        ball.reset()

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
