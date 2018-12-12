import sys
import ui
import pygame
from pygame.locals import *
from hero import Hero
from floor import Floor

def set_position(floor, entity, next_loc):
    if next_loc[0] in list(range(len(floor.map))):
        if next_loc[1] in list(range(len(floor.map[next_loc[0]]))):
            if floor.map[next_loc[0]][next_loc[1]] == 1:
                entity.loc_x = next_loc[0]
                entity.loc_y = next_loc[1]
                entity.pos_x = floor.origin[0] + (entity.loc_x * floor.tile_size)
                entity.pos_y = floor.origin[1] + (entity.loc_y * floor.tile_size)
    return

def main():
    # initialize game engine
    pygame.init()

    # Setup main window
    window_width=400
    window_height=300
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("YARL!")

    # Initialize Hero
    floor = Floor("floors/dungeon.json")
    hero = Hero()
    print(hero.name + " just entered " + floor.name)
    hero.loc_x = floor.spawn[0]
    hero.loc_y = floor.spawn[1]
    set_position(floor,hero,[hero.loc_x,hero.loc_y])

    # Example of event handling
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                next_loc = [hero.loc_x, hero.loc_y]
                if event.key == pygame.K_LEFT:
                    next_loc[0] -= 1
                if event.key == pygame.K_RIGHT:
                    next_loc[0] += 1
                if event.key == pygame.K_UP:
                    next_loc[1] -= 1
                if event.key == pygame.K_DOWN:
                    next_loc[1] += 1
                set_position(floor,hero,next_loc)

        # Get all items to blit
        blits = floor.get_blits()
        blits += ui.get_blits()
        blits += hero.get_blits()
        alien_img = pygame.image.load("assets/spirit.png").convert_alpha()
        blits.append((alien_img, [185,110]))

        # Blit and update display at every frame
        for item in blits:
            screen.blit(item[0],item[1])
        pygame.display.update()

main()