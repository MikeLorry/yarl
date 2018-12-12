import names
import pygame

class Hero:
    """Common class for Heroes"""

    def __init__(self):
        self.name = names.get_first_name()
        self.avatar = "assets/robot.png"
        self.max_life = 10
        self.life = self.max_life
        self.pos_x = 69
        self.pos_y = 83
        self.loc_x = 0
        self.loc_y = 0
        self.img = pygame.image.load(self.avatar).convert_alpha()

    def defend(self,force,type="hit"):
        print("Attacked by " + str(force) + " " + type)
        return

    def heal(self,points):
        if self.life + points >= self.max_max_life:
            self.life = self.max_life
            print("Back to full health")
        else:
            self.life += points
            print("Healed " + str(points) + " life points")
        return

    def get_blits(self):
        blits = []

        # Hero avatar
        blits.append((self.img, [self.pos_x, self.pos_y]))

        # Hero name
        pos_x = 10
        pos_y = 7
        pygame.font.init()
        font_comic = pygame.font.SysFont('Comic Sans MS', 30)
        surf_hero_name = font_comic.render(self.name, True, (200, 255, 200))
        blits.append((surf_hero_name,[pos_x,pos_y]))

        # Life Bar
        pos_x = 130
        pos_y = 9
        img_heart = pygame.image.load("assets/heart.png").convert_alpha()
        surf_life = pygame.Surface((self.life * 16, 16))
        surf_life.set_colorkey((0,0,0))
        for i in range(self.life):
            surf_life.blit(img_heart,(i*16,0))
        blits.append((surf_life,[pos_x,pos_y]))
        return blits