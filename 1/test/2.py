import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Touchscreen Joystick")

# Joystick properties
joystick_radius = 50
joystick_color = (0, 0, 0)  # Red

# Initial joystick position
JSC = [width // 2, height // 2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # Check for touch/mouse motion
            if pygame.mouse.get_pressed()[0]:
                print(JSC)
                # Left mouse button pressed
                touch_pos = pygame.mouse.get_pos()
                distance = pygame.math.Vector2(touch_pos[0] - JSC[0], touch_pos[1] - JSC[1])
                magnitude = min(distance.length(), joystick_radius)
                normalized = distance.normalize() if distance.length() > 0 else pygame.math.Vector2(0, 0)
                JSC = [int(JSC[0] + normalized.x * magnitude), int(JSC[1] + normalized.y * magnitude)]

    screen.fill((255, 255, 255))  # White background

    # Draw joystick
    pygame.draw.circle(screen, joystick_color, JSC, joystick_radius)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
