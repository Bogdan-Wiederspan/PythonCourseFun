import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define game objects
dino_width = 40
dino_height = 60
dino_x = 50
dino_y = HEIGHT - dino_height - 10
dino_jump_speed = -15
dino_gravity = 0.8

obstacle_width = 30
obstacle_height = 70
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 10
obstacle_speed = 5

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y == HEIGHT - dino_height - 10:
                dino_jump_speed = -15

    # Update dino position
    dino_jump_speed += dino_gravity
    dino_y += dino_jump_speed

    # Keep dino on the ground
    if dino_y > HEIGHT - dino_height - 10:
        dino_y = HEIGHT - dino_height - 10
        dino_jump_speed = 0

    # Update obstacle position
    obstacle_x -= obstacle_speed

    # Reset obstacle when it goes off-screen
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - obstacle_height - 10

    # Check for collision
    if (
        dino_x + dino_width > obstacle_x
        and dino_x < obstacle_x + obstacle_width
        and dino_y + dino_height > obstacle_y
    ):
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw game objects
    pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
