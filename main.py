import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Apple")

# Set up the apple image
apple_image = pygame.image.load("apple.gif")
apple_rect = apple_image.get_rect()
apple_rect.center = (window_width // 2, window_height // 2)

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the player clicked on the apple
            if apple_rect.collidepoint(event.pos):
                score += 1
    
    # Fill the window with a darker background
    window.fill((50, 0, 0))
    
    # Draw the apple
    window.blit(apple_image, apple_rect)
    
    # Draw the score
    score_text = font.render(f"{score}", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.midtop = (window_width // 2-17, 160)
    window.blit(score_text, score_rect)
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()