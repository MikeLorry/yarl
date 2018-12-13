import names
import pygame

class Ennemy:
    """Common class for Ennemies"""

    def __init__(self):
        self.name = names.get_first_name()
        self.type = "ennemy"
        self.avatar = "assets/alien.png"
        self.max_life = 3
        self.life = self.max_life
        self.pos_x = 0
        self.pos_y = 0
        self.loc_x = 0
        self.loc_y = 0
        self.img = pygame.image.load(self.avatar).convert_alpha()

    def get_blits(self):
        blits = []

        # Avatar
        blits.append((self.img, [self.pos_x, self.pos_y]))

        # Life Bar
        surf_life = pygame.Surface((self.life * (40/self.max_life), 3))
        surf_life.fill((255,0,0))
        blits.append((surf_life,[self.pos_x+5,self.pos_y+7]))
        return blits
