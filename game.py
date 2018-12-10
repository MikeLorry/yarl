import pygame
import sys
from pygame.locals import *
from hero import Hero

def main():
    # initialize game engine
    pygame.init()

    # Init fonts
    pygame.font.init()
    font_comic = pygame.font.SysFont('Comic Sans MS', 30)

    # Setup main window
    window_width=400
    window_height=300
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("N.E.R.D.S.")

    # Load background image
    img_background = pygame.image.load("dungeon.jpg").convert()

    # Initialize Hero
    hero = Hero()
    surf_hero_name = font_comic.render(hero.name, True, (200, 255, 200))
    img_hero = pygame.image.load(hero.avatar).convert()
    img_heart = pygame.image.load("heart.gif").convert()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(img_background, [0, 0])
        screen.blit(surf_hero_name,(10,10))
        screen.blit(img_hero, [100, 100])
        surf_life = pygame.Surface((hero.max_life * 16, 16))
        for i in range(hero.life):
            surf_life.blit(img_heart,(i*16,0))
        screen.blit(surf_life, [130, 10])
        pygame.display.update()

main()