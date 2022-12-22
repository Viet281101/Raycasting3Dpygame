
from sprite_object import *
from settings import *


class ObjectHandler():
    def __init__(self, game) -> None:
        self.game = game
        self.sprite_list : list = []
        self.static_sprite_path : str = path_static_sprite
        self.anim_sprite_path : str = path_animate_sprite
        add_sprite = self.add_sprite

        ##### sprite map:
        add_sprite(SpriteObject(game, path=path_candlebra))
        add_sprite(AnimatedSprite(game, path=path_green_light))
    
    def update(self) -> None:
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite) -> None:
        self.sprite_list.append(sprite)


