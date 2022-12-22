
import pygame as pg
from settings import *


class ObjectRenderer():
    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen
        self.wall_textures : dict = self.load_wall_textures()
        self.sky_image = self.get_texture(path_sky_bg, (WIDTH, HALF_HEIGHT))
        self.sky_offset : int = 0

    def draw(self) -> None:
        self.draw_background()
        self.render_game_objects()
    
    def draw_background(self) -> None:
        self.sky_offset : float = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        ##### floor:
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self) -> None:
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res:tuple=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)


    def load_wall_textures(self) -> dict:
        return {
            1: self.get_texture(path_textures + '1.png'),
            2: self.get_texture(path_textures + '2.png'),
            3: self.get_texture(path_textures + '3.png'),
            4: self.get_texture(path_textures + '4.png'),
            5: self.get_texture(path_textures + '5.png'),
        }
