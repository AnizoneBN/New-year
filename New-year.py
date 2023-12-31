import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy New Year 2023!")

# Set up colors
black = (0, 0, 0)
white = (0, 0, 0)
red = (255, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Display Happy New Year message
text = font.render("Happy New Year 2024!", True, red)
text_rect = text.get_rect(center=(width // 2, height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the message
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
sys.exit()