

import pygame as pg
from settings import *

class Sound():
    def __init__(self, game) -> None:
        self.game = game
        pg.mixer.init()
        self.path : str = path_sound
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')

