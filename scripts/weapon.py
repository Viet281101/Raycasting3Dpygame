
from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path:str = path_shotgun, 
                scale:float = 0.4, animation_time:int = 90) -> None:
        super().__init__(game=game, path=path, 
                        scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale,
            self.image.get_height() * scale))
            for img in self.images]
        )
        self.weapon_pos : tuple = (HALF_WIDTH - self.images[0].get_width() // 2,
                                    HEIGHT - self.images[0].get_height())
        self.reloading : bool = False
        self.num_images : int = len(self.images)
        self.frame_counter : int = 0
        self.damage : int = 50
    
    def animate_shot(self) -> None:
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self) -> None:
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self) -> None:
        self.check_animation_time()
        self.animate_shot()
    


