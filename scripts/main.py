
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from button import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *


class Game():
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time : int = 1
        self.new_game()
    
    def new_game(self) -> None:
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)

    def update(self) -> None:
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()

        pg.display.flip()
        self.delta_time = int(self.clock.tick(FPS))
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self) -> None:
        ####### view 3D:
        self.object_renderer.draw()
        self.weapon.draw()
        pg.mouse.set_visible(False)

        ####### view 2D:
        # self.screen.fill('black')
        # self.map.draw()
        # self.player.draw()
    
    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            self.player.single_fire_event(event)
    
    def play(self) -> None:
        while can_play:
            self.check_events()
            self.update()
            self.draw()



#### main function:
def main(args) -> None:
    game = Game()
    game.play()



if __name__ == '__main__':

    ##### main
    main(sys.argv)


