
from settings import *
import pygame as pg
import math


class Player():
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self) -> None:
        sin_a : float = math.sin(self.angle)
        cos_a : float = math.cos(self.angle)
        dx, dy = 0, 0
        speed : float = float(PLAYER_SPEED) * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        ####### UP:
        if keys[pg.K_z]: 
            dx += speed_cos; dy += speed_sin
        ####### DOWN:
        elif keys[pg.K_s]: 
            dx -= speed_cos; dy -= speed_sin
        ####### LEFT:
        elif keys[pg.K_q]: 
            dx += speed_sin; dy -= speed_cos
        ####### RIGHT:
        elif keys[pg.K_d]: 
            dx -= speed_sin; dy += speed_cos

        self.check_wall_collision(float(dx), float(dy))

        ######## control angle with key:
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # elif keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        self.angle %= math.tau ## tau = 2*pi

    def check_wall(self, x:int, y:int) -> tuple:
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx:float, dy:float) -> None:
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self) -> None:
        ######## test raycast line:
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle),
        #             self.y * 100 + WIDTH * math.sin(self.angle)), 2)

        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)        

    
    def mouse_control(self) -> None:
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_WIDTH])
        self.rel : int = pg.mouse.get_rel()[0]
        self.rel : int = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time
    
    def update(self) -> None:
        self.movement()
        self.mouse_control()
    
    @property
    def pos(self) -> tuple:
        return (self.x, self.y)
    
    @property
    def map_pos(self) -> tuple:
        return (int(self.x), int(self.y))
    

