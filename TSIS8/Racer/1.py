import pygame
import random

# Initialize pygame
pygame.init()


background = pygame.image.load("TSIS8\Racer\AnimatedStreet.png")

# Set up the screen
screen_width = 680
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer Game")


# Set up the clock
clock = pygame.time.Clock()


# Load the images
car_image = pygame.image.load("TSIS8\Racer\Player.png").convert_alpha()
enemy_image = pygame.image.load("TSIS8\Racer\Enemy.png").convert_alpha()

# Set up the car
car_x = screen_width // 2
car_y = screen_height - car_image.get_height() - 20
car_speed = 5

# Set up the enemies
enemy_list = []
enemy_speed = 3
enemy_spawn_time = 1000
last_enemy_spawn_time = 0

# Set up the score
score = 0
font = pygame.font.Font(None, 30)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    elif keys[pygame.K_RIGHT]:
        car_x += car_speed
    
    # Spawn enemies
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn_time > enemy_spawn_time:
        last_enemy_spawn_time = current_time
        enemy_x = random.randint(0, screen_width - enemy_image.get_width())
        enemy_y = -enemy_image.get_height()
        enemy_list.append((enemy_x, enemy_y))
    
    # Move the enemies
    for i, enemy in enumerate(enemy_list):
        enemy_x, enemy_y = enemy
        enemy_y += enemy_speed
        enemy_list[i] = (enemy_x, enemy_y)
        
        # Check for collision with the car
        if enemy_y + enemy_image.get_height() > car_y and \
           enemy_y < car_y + car_image.get_height() and \
           enemy_x + enemy_image.get_width() > car_x and \
           enemy_x < car_x + car_image.get_width():
            running = False
    
    # Remove enemies that have gone off the screen
    enemy_list = [(enemy_x, enemy_y) for enemy_x, enemy_y in enemy_list
                  if enemy_y < screen_height]
    
    # Draw the background
    screen.fill((255, 255, 255))
    
    # Draw the car
    screen.blit(car_image, (car_x, car_y))
    
    # Draw the enemies
    for enemy_x, enemy_y in enemy_list:
        screen.blit(enemy_image, (enemy_x, enemy_y))
    
    # Draw the score
    score += len(enemy_list)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Update the screen
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(60)

# Clean up pygame
pygame.quit()