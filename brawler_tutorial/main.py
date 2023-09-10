# Import modules
import pygame

# Initialize pygame module
pygame.init()

# Create game window

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates a game window and assigns to the screen variable
pygame.display.set_caption("Brawler")


# Load background image from current folder structure
background_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha() # convert_alpha helps image load with the current pixel set?

# Function for drawing background
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Scale the background image to the width and height of the display
    screen.blit(scaled_background, (0, 0)) # Blit is used to draw the background onto the screen

# Game loop
run = True
while run:

    # Draw Background
    draw_background()
    
    # event handler - searching for user manually closing the window and closing game loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    # Update Display
    pygame.display.update()
    
# exit pygame
pygame.quit()