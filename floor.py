import pygame
import json

class Floor:
    """Common class for floors"""

    def __init__(self, floor_file):
        with open(floor_file,"r") as f:
            cfg_json = json.loads(f.read())
        self.name = cfg_json["name"]
        self.background = pygame.image.load(cfg_json["background"]).convert_alpha()
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
        blits.append((self.background, [0, 0]))
        return blits
