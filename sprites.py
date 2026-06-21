import pygame
from constants import *

class GridBlock(pygame.sprite.Sprite):
    def __init__(self, position, groups, color):
        super().__init__(groups)
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)
