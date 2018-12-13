import sys
import random
import ui
import pygame
from pygame.locals import *
from hero import Hero
from floor import Floor
from ennemy import Ennemy

def set_position(entity, floor):
    entity.pos_x = floor.origin[0] + (entity.loc_x * floor.tile_size)
    entity.pos_y = floor.origin[1] + (entity.loc_y * floor.tile_size)
    return

def set_loc(floor, entity, ennemies, next_loc):
    if next_loc[0] in list(range(len(floor.map))):
        if next_loc[1] in list(range(len(floor.map[next_loc[0]]))):
            if floor.map[next_loc[0]][next_loc[1]] == 1:
                ennemies_loc = [(e.loc_x,e.loc_y) for e in ennemies]
                if (next_loc[0],next_loc[1]) not in ennemies_loc:
                    entity.loc_x = next_loc[0]
                    entity.loc_y = next_loc[1]
    return

def get_ennemy_spawn(floor, ennemies, hero):
    locs = []
    for i in range(len(floor.map)):
        for j in range(len(floor.map[i])):
            if floor.map[i][j] == 1:
                locs.append((i,j))
    ennemies_loc = [(e.loc_x,e.loc_y) for e in ennemies]
    locs = [l for l in locs if l not in ennemies_loc and l != (hero.loc_x,hero.loc_y)]
    loc = random.choice(locs)
    return loc

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
    set_position(hero,floor)

    # Initialize ennemies
    nb_ennemies = 1
    ennemies = []
    for ennemy in range(nb_ennemies):
        ennemies.append(Ennemy())
        loc = get_ennemy_spawn(floor, ennemies, hero)
        ennemies[-1].loc_x = loc[0]
        ennemies[-1].loc_y = loc[1]
        set_position(ennemies[-1], floor)

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
                set_loc(floor,hero,ennemies,next_loc)
                set_position(hero,floor)

        # Get all items to blit
        blits = floor.get_blits()
        blits += ui.get_blits()
        blits += hero.get_blits()
        for ennemy in ennemies:
            blits += ennemy.get_blits()

        # Blit and update display at every frame
        for item in blits:
            screen.blit(item[0],item[1])
        pygame.display.update()

main()