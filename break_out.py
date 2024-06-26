import pygame
import paddle, playball, brick
pygame.init()


# colorspace
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
MAX_BALL_SPEED = 10


# 20 stones a 20 pixels widht, 30 stones a 20 (600 x 400)
WIDTH, HEIGHT = (20 * 20, 30 * 20 )
score = 0
lives = 3

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Break Out")

clock = pygame.time.Clock()
running = True

WIDTH = screen.get_width()
HEIGHT = screen.get_height()
paddle = paddle.Paddle(WIDTH // 2, HEIGHT - 50, RED)
ball = playball.Ball(WIDTH // 2, HEIGHT // 2, BLUE)
bricks, num_of_bricks = brick.grid(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw game objects
    paddle.move(screen)
    ball.move(screen)
    for column, column_bricks in enumerate(bricks):
        for row, row_brick in enumerate(column_bricks):
            row_brick.draw(screen)
            if ball.collide(row_brick):
                score += row_brick.score
                num_of_bricks -= 1
                bricks[column][row] = brick.EmptyBrick(row_brick.x, row_brick.y)


    ball.draw(screen)
    paddle.draw(screen)

    if ball.collide(paddle):
        ball.direction_y = -1
        # increase speed by 10% each time the ball hits the paddle
        ball.speed = min(ball.speed * 1.10, MAX_BALL_SPEED)


    # score live fonts
    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", 1, BLACK)
    screen.blit(text, (20,screen.get_height() - 40))
    text = font.render(f"Lives: {lives}", 1, BLACK)
    screen.blit(text, (120,screen.get_height() - 40))

    if num_of_bricks == 0:
        font = pygame.font.Font(None, 74)
        text = font.render("You Won!", 1, BLACK)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        running = False

    if ball.y >= HEIGHT - ball.radius:
        lives -= 1

        ball = playball.Ball(WIDTH // 2, HEIGHT // 2, BLUE)
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over!", 1, BLACK)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
            running = False
    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(20)

# Quit the game

#pygame.quit()
