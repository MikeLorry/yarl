import pygame

def get_ui_items(hero):
    items = []
    items.append(get_background())
    items.append(get_top_bar())
    items.append(get_bottom_bar())
    items.append(get_hero_name(hero.name))
    items.append(get_life_bar(hero.life))
    return items

def get_background():
    pos_x = 0
    pos_y = 0
    img_background = pygame.image.load("dungeon.jpg").convert()
    return (img_background,[pos_x,pos_y])

def get_top_bar():
    pos_x = 0
    pos_y = 0
    surf_top_bar = pygame.Surface((400, 30))
    surf_top_bar.fill((0, 0, 0))
    surf_top_bar.set_alpha(160)
    return (surf_top_bar,[pos_x,pos_y])

def get_bottom_bar():
    pos_x = 0
    pos_y = 260
    surf_bottom_bar = pygame.Surface((400, 40))
    surf_bottom_bar.fill((0, 0, 0))
    for step in range(7):
        pygame.draw.lines(surf_bottom_bar, (200,200,200), False, [((step+1)*50,5), ((step+1)*50,35)], 3)
    surf_bottom_bar.set_alpha(160)
    return (surf_bottom_bar,[pos_x,pos_y])

def get_hero_name(name):
    pos_x = 10
    pos_y = 7
    pygame.font.init()
    font_comic = pygame.font.SysFont('Comic Sans MS', 30)
    surf_hero_name = font_comic.render(name, True, (200, 255, 200))
    return (surf_hero_name,[pos_x,pos_y])

def get_life_bar(life_points):
    pos_x = 130
    pos_y = 9
    img_heart = pygame.image.load("heart.png").convert_alpha()
    surf_life = pygame.Surface((life_points * 16, 16))
    surf_life.set_colorkey((0,0,0))
    for i in range(life_points):
        surf_life.blit(img_heart,(i*16,0))
    return (surf_life,[pos_x,pos_y])