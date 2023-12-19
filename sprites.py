import pygame as pg
from pygame.sprite import Sprite
pg.init()
pg.display.set_caption("Decision Analysis")

from pygame.math import Vector2 as vec
import os
from settings import *

class Solids:
    def __init__(self, x, y, w, h,text,size,color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.topleft = vec(x,y)
    


