import pygame

# GLOBAL VARIABLES
display_resolution = (1200, 650)
clock = pygame.time.Clock()

# COLORS
white = (255, 255, 255)

# Window configuration for the editor
def init_window():
    pygame.init()
    gameDisplay = pygame.display.set_mode(display_resolution)
    gameDisplay.fill(white)
    pygame.display.set_caption('Polygon Editor - CG')

# Running user interaction through window
# Here we define the events with the user
def run_window():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)

def main():
    init_window()
    run_window()

if __name__ == '__main__':
    main()