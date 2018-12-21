import pygame
import json
import random

class Floor:
    """Common class for floors"""

    def __init__(self, floor_file):
        with open(floor_file,"r") as f:
            cfg_json = json.loads(f.read())
        self.name = cfg_json["name"]
        self.background = pygame.image.load(cfg_json["background"]).convert_alpha()
        self.space_bg = self.get_space_background()
        self.map = self.format_map(cfg_json["map"])
        self.origin = cfg_json["origin"].split(":")
        self.origin = [int(x) for x in self.origin]
        self.tile_size = cfg_json["tile_size"]
        self.spawn = cfg_json["spawn"].split(":")
        self.spawn = [int(x) for x in self.spawn]

    def format_map(self, map_file):
        with open(map_file,"r") as f:
            map = f.readlines()
        map = [x.strip() for x in map]
        for i in range(len(map)):
            map[i] = map[i].split(",")
            map[i] = [int(j) for j in map[i]]
        return map

    def get_blits(self):
        blits = []
        # Background
        #blits.append((self.background, [0, 0]))
        blits.append((self.space_bg, [0,0]))
        return blits

    def get_space_background(self):
        screen_size = (400,300)
        surf_space = pygame.Surface(screen_size)
        nb_chunk = (self.background.get_size()[0]/50) * (self.background.get_size()[1]/50)
        chunks = []
        stars_per_chunk = 10
        chunk_size = (50,50)
        for chunk in range(nb_chunk):
            surf = pygame.Surface(chunk_size)
            surf.fill((0,0,20))
            for star in range(stars_per_chunk):
                pos_x = random.randint(0, chunk_size[0])
                pos_y = random.randint(0, chunk_size[1])
                pygame.draw.line(surf, (255,255,255), [pos_x, pos_y], [pos_x,pos_y], 1)
            chunks.append(surf)
        pos_x = 0
        pos_y = 0
        for chunk in chunks:
            surf_space.blit(chunk,[pos_x,pos_y])
            pos_x += chunk_size[0]
            if pos_x == screen_size[0]:
                pos_x = 0
                pos_y += chunk_size[1]
        return surf_space
