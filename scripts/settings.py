
import math


############### game settings: 
WIDTH : int = 1600
HEIGHT : int = 900
RES : tuple = (WIDTH, HEIGHT)

HALF_WIDTH : int = WIDTH // 2
HALF_HEIGHT : int = HEIGHT // 2

FPS : int = 0

can_play : bool = True


################## mouse control:
MOUSE_SENSITIVITY : float = 0.0003
MOUSE_MAX_REL : int = 40
MOUSE_BORDER_LEFT : int = 100
MOUSE_BORDER_RIGHT : int = WIDTH - MOUSE_BORDER_LEFT


############## mini map:
player_pos_x : int = 1.5
player_pos_y : int = 5

PLAYER_POS : tuple = (player_pos_x, player_pos_y)
PLAYER_ANGLE : int = 0
PLAYER_SPEED : float = 0.004
PLAYER_ROT_SPEED : float = 0.002
PLAYER_SIZE_SCALE : int = 60


################ build:
FLOOR_COLOR : tuple = (30, 30, 30)

FOV : float = (math.pi / 3)
HALF_FOV : float = (FOV / 2)
NUM_RAYS : int = WIDTH // 2
HALF_NUM_RAYS : int = NUM_RAYS // 2
DELTA_ANGLE : float = (FOV / NUM_RAYS)
MAX_DEPTH : int = 20

SCREEN_DIST : float = HALF_WIDTH / math.tan(HALF_FOV)
SCALE : int = WIDTH // NUM_RAYS


TEXTURE_SIZE : int = 256
HALF_TEXTURE_SIZE : int = TEXTURE_SIZE // 2



#################################### sources game path:
path_textures : str = '../assets/images/textures/'
path_static_sprite : str = '../assets/images/sprites/static_sprites/'
path_animate_sprite : str = '../assets/images/sprites/animated_sprites/'
path_candlebra : str = path_static_sprite + 'candlebra.png'
path_green_light : str = path_animate_sprite + 'green_light/0.png'
path_red_light : str = path_animate_sprite + 'red_light/0.png'
path_sky_bg : str = path_textures + 'sky.png'
path_shotgun : str = '../assets/images/sprites/weapon/shotgun/0.png'
path_sound : str = '../assets/sound/'


