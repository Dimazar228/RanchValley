import pygame
from settings import *
from player import Player
from overlay import Overlay


class Level:
    def __init__(self):
        # get the display
        self.display_surface = pygame.display.get_surface()

        # all sprites
        self.all_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((640, 360), self.all_sprites)  # DON'T FORGET TO CHANGE THIS VALUE

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        self.overlay.display()
