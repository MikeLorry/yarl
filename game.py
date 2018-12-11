import sys
import ui
import pygame
from pygame.locals import *
from hero import Hero

def main():
    # initialize game engine
    pygame.init()

    # Setup main window
    window_width=400
    window_height=300
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("N.E.R.D.S.")

    # Initialize Hero
    hero = Hero()

    # Example of event handling
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.pos_x -= 50
                if event.key == pygame.K_RIGHT:
                    hero.pos_x += 50
                if event.key == pygame.K_UP:
                    hero.pos_y -= 50
                if event.key == pygame.K_DOWN:
                    hero.pos_y += 50
        # Draw UI
        for item in ui.get_ui_items(hero):
            screen.blit(item[0],item[1])

        # Draw characters
        screen.blit(hero.img, [hero.pos_x, hero.pos_y])
        alien_img = pygame.image.load("spirit.png").convert_alpha()
        screen.blit(alien_img, [185,110])

        # Update display at every frame
        pygame.display.update()

main()