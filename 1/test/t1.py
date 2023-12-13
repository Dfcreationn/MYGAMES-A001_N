import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Change Screen Color")

# Set initial background color
background_color = (255, 255, 255)  # White

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update display with the new background color
    screen.fill(background_color)
    pygame.display.flip()

    # You can change the background color here based on your needs
    # For example, change to red after a certain condition is met:
    # if some_condition:
    #     background_color = (255, 0, 0)  # Red

    pygame.time.Clock().tick(60)  # Limit frames per second

# The game loop will continue running until you close the window
