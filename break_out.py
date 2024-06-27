import pygame
from Objects import Paddle, Ball, Brick, grid, EmptyBrick
pygame.init()

# colorspace
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
MAX_BALL_SPEED = 10

# 20 stones a 20 pixels widht, 30 stones a 20 (600 x 400)
WIDTH, HEIGHT = (20 * 20, 30 * 20 )



score = 0
lives = 3

# Set up the game window


FONT_BUFFER_PIXEL = 50
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + FONT_BUFFER_PIXEL))
pygame.display.set_caption("Break Out")

clock = pygame.time.Clock()
running = True

# init our object instances
paddle = Paddle(WIDTH // 2, HEIGHT - 50, RED, screen=SCREEN, width=100, height=20, speed = 7.5)
ball = Ball(WIDTH // 2, HEIGHT // 2, BLUE, screen=SCREEN)
bricks, num_of_bricks = grid(screen=SCREEN)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    SCREEN.fill(GRAY)
    pygame.draw.line(surface=SCREEN, color=BLACK, start_pos=(0, HEIGHT), end_pos=(WIDTH, HEIGHT))

    paddle.move()
    ball.move()
    for num_brick, brick in enumerate(bricks):
        brick.draw()
        if ball.collide(brick):
            score += brick.score
            num_of_bricks -= 1
            #bricks.remove(brick)
            bricks[num_brick] =EmptyBrick(brick.x, brick.y, screen=brick.screen)
            ball.direction_y *= -1
            if isinstance(brick, EmptyBrick):
                ball.speed = min(ball.speed * 1.01, MAX_BALL_SPEED)

    ball.draw()
    paddle.draw()

    # paddle - ball collision
    if ball.collide(paddle):
        ball.direction_y = -1
        # increase speed by 10% each time the ball hits the paddle
        ball.speed = min(ball.speed * 1.10, MAX_BALL_SPEED)

    # brick - ball collision


    # score live fonts
    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", 1, BLACK)
    SCREEN.blit(text, (20, SCREEN.get_height() - 40))
    text = font.render(f"Lives: {lives}", 1, BLACK)
    SCREEN.blit(text, (160, SCREEN.get_height() - 40))

    if num_of_bricks == 0:
        font = pygame.font.Font(None, 74)
        text = font.render("You Won!", 1, BLACK)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        running = False

    if ball.y >= HEIGHT:
        lives -= 1
        ball.reset()

        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over!", 1, BLACK)
            SCREEN.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            running = False
    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game

#pygame.quit()
