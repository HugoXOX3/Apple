import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Apple")

#You can change the "apple.gif" in the your favourite picture
apple_image = pygame.image.load("apple.gif")
apple_rect = apple_image.get_rect()
apple_rect.center = (window_width // 2, window_height // 2)

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the timer variables
start_time = time.time()  # Get the current time
gift = 0

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
    
    # Change this to the colour that you want
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
    
    # Check the timer
    elapsed_time = time.time() - start_time
    if elapsed_time >= 10800:  # 3 hours (3 hours * 60 minutes * 60 seconds)
        start_time = time.time()  # Reset the timer
        
        #Rewrite this 2 line by using the api in steam so Player can earn from this
        gift += 1
        print("Received a gift!")
    
    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
