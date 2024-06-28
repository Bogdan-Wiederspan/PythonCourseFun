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

while run_game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game_loop = False

    # screen clearing and drawing
    # background
    SCREEN.fill(GRAY)
    pygame.draw.line(surface=SCREEN, color=BLACK, start_pos=(0, HEIGHT), end_pos=(WIDTH, HEIGHT))

    # score and live text
    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", 1, BLACK)
    SCREEN.blit(text, (20, SCREEN.get_height() - 40))
    text = font.render(f"Lives: {lives}", 1, BLACK)
    SCREEN.blit(text, (160, SCREEN.get_height() - 40))

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
        if ball.collide(brick):
            pygame.mixer.Sound.play(sfx_hit_brick)
            score += brick.score
            num_of_bricks -= 1
            # replace the brick with an empty brick that has the same position
            bricks[num_brick] = EmptyBrick(brick.x, brick.y, screen=brick.screen)
            # reverse the direction of the ball and increase speed
            ball.direction_y *= -1
            if isinstance(brick, EmptyBrick):
                ball.speed = min(ball.speed * 1.01, MAX_BALL_SPEED)

    # ball and paddle
    # increase speed by 10% each time the ball hits the paddle
    if ball.collide(paddle):
        ball.direction_y = -1
        ball.speed = min(ball.speed * 1.10, MAX_BALL_SPEED)

    # win and loose conditions
    win_condition = num_of_bricks == 0
    if win_condition:
        font = pygame.font.Font(None, 74)
        text = font.render("You Won!", 1, BLACK)
        SCREEN.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        run_game_loop = False

    loose_live_condition = ball.y >= HEIGHT
    if loose_live_condition:
        pygame.mixer.Sound.play(sfx_death)
        lives -= 1
        ball.reset()

        # pause the game until press p
        pause_mode = True
        while pause_mode:
            font = pygame.font.Font(None, 74)
            text = font.render("Press p to continue", 1, BLACK)
            SCREEN.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause_mode = False
        # if no lives left, game over
        loose_game_condition = lives == 0
        if loose_game_condition:
            # clear screen and display game over message
            SCREEN.fill(GRAY)
            pygame.draw.line(surface=SCREEN, color=BLACK, start_pos=(0, HEIGHT), end_pos=(WIDTH, HEIGHT))
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over!", 1, BLACK)
            SCREEN.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_game_loop = False

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
pygame.quit()
