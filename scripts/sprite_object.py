

import pygame as pg
from settings import *
import os
from collections import deque



class SpriteObject():
    def __init__(self, game, path:str = path_candlebra, 
                pos:tuple=(10.5, 3.5), 
                scale:float = 0.7, 
                shift:float = 0.27) -> None:
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH : int = self.image.get_width()
        self.IMAGE_HALF_WIDTH : int = self.image.get_width() // 2
        self.IMAGE_RATIO : float = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self) -> None:
        proj : float = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width : float = proj_width // 2
        height_shift : float = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos : tuple[float, float] = (self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift)

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self) -> None:
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta : float = math.atan2(dy, dx)

        delta : float = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays : float = delta / DELTA_ANGLE
        self.screen_x : float = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist : float = math.hypot(dx, dy)
        self.norm_dist : float = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self) -> None:
        self.get_sprite()



class AnimatedSprite(SpriteObject):
    def __init__(self, game, path:str = path_green_light, 
                pos:tuple = (11.5, 3.5), 
                scale:float = 0.8, 
                shift:float = 0.15, 
                animation_time:int = 120) -> None:
        super().__init__(game, path, pos, scale, shift)
        self.animation_time:int = animation_time
        self.path:str = path.rsplit('/', 1)[0]
        self.images:deque = self.get_images(self.path)
        self.animation_time_prev:int = pg.time.get_ticks()
        self.animation_trigger : bool = False
    
    def update(self) -> None:
        super().update()
        self.check_animation_time()
        self.animate(self.images)
    
    def animate(self, images) -> None:
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]
    
    def check_animation_time(self) -> None:
        self.animation_trigger : bool = False
        time_now : int = pg.time.get_ticks()
        if (time_now - self.animation_time_prev) > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True
    
    def get_images(self, path) -> deque:
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images


