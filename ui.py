import pygame

def get_blits():
    items = []
    items.append(get_top_bar())
    items.append(get_bottom_bar())
    return items

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
