import pygame
import random
import math


# Elijah Bailey
# P5HW
# 11/20


# Initialize pygame
pygame.init()

# Function to get user inputs
def get_game_settings():
    # Ask the user for three variables: health, player speed, and number of enemies
    while True:
        try:
            player_health = int(input("Enter the starting health for the player (e.g., 3): "))
            player_speed = int(input("Enter the speed of the player (e.g., 5): "))
            num_enemies = int(input("Enter the number of enemies to spawn at the start (e.g., 6): "))
            if player_health <= 0 or player_speed <= 0 or num_enemies <= 0:
                print("Please enter positive values for all settings.")
                continue
            return player_health, player_speed, num_enemies
        except ValueError:
            print("Invalid input! Please enter integer values.")

# Get user settings
player_health, player_speed, num_enemies = get_game_settings()

# Set up the game screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga Replica")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define FPS
FPS = 60
clock = pygame.time.Clock()

# Load images (use basic shapes or import your own images)
player_img = pygame.Surface((50, 40))
player_img.fill(BLUE)
bullet_img = pygame.Surface((5, 10))
bullet_img.fill(RED)
enemy_img = pygame.Surface((50, 40))
enemy_img.fill(GREEN)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, health, speed):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = speed
        self.health = health  # Set health from user input

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(1, 3)

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create the player with user-defined health and speed
player = Player(player_health, player_speed)
all_sprites.add(player)

# Create enemies with user-defined number of enemies
for i in range(num_enemies):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Initialize score
score = 0

# Function to show the death screen and ask for play again
def show_death_screen():
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over! Press 'R' to Restart or 'Q' to Quit.", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    # Wait for player input to restart or quit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()  # Quit the game

# Function to display controls
def display_controls():
    font = pygame.font.SysFont(None, 28)
    controls = [
        "Controls:",
        "Move Left: Arrow Left",
        "Move Right: Arrow Right",
        "Shoot: Spacebar"
    ]
    y_offset = 30  # Starting Y position for controls text
    for line in controls:
        control_text = font.render(line, True, WHITE)
        screen.blit(control_text, (20, y_offset))
        y_offset += 30

# Main game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a bullet
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update game objects
    all_sprites.update()

    # Check for bullet collision with enemies
    for bullet in bullets:
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        for hit in enemies_hit:
            bullet.kill()  # Remove bullet on hit
            enemy = Enemy()  # Create new enemy
            all_sprites.add(enemy)
            enemies.add(enemy)
            # Increase score
            score += 10

    # Check if the player collides with enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        # Reduce health
        player.health -= 1
        if player.health > 0:
            # Respawn enemies after player collision
            for _ in range(3):  # Respawn 3 new enemies
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)
        else:
            # Player loses if health reaches 0
            if show_death_screen():
                # Restart the game if the player presses 'R'
                player = Player(player_health, player_speed)
                all_sprites = pygame.sprite.Group(player)
                bullets = pygame.sprite.Group()
                enemies = pygame.sprite.Group()
                for i in range(num_enemies):
                    enemy = Enemy()
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                score = 0  # Reset score
            else:
                running = False  # Exit game if 'Q' is pressed

    # Draw everything
    screen.fill(BLACK)

    # Draw the health bar (3 hearts)
    for i in range(player.health):
        pygame.draw.rect(screen, RED, (20 + i * 30, 20, 20, 20))  # Simple heart icon (just a rectangle for now)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

    # Draw the player and all sprites
    all_sprites.draw(screen)

    # Display controls
    display_controls()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
