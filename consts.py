# Window Attributes
S_WIDTH = 640
S_HEIGHT = 360

# Controls
P_LEFT = "a"
P_UP = "w"
P_RIGHT = "d"
P_DOWN = "s"
P_SHOOT = "space"

ASSETS_PATH = "assets/"

# Art
BUBBLE_PATH = ASSETS_PATH + "bubbles/"
BUBBLE_OPTIONS = [BUBBLE_PATH + "bubble_0.png", BUBBLE_PATH + "bubble_1.png"]
BUBBLE_BURST = [BUBBLE_PATH + "burst_1.png", BUBBLE_PATH + "burst_0.png"]

TADPOLE_PATH = ASSETS_PATH + "tadpole/"
TADPOLE = TADPOLE_PATH + "tadpole.png"

# Player attributes
P_HITBOX_X = 32
P_HITBOX_Y = 16
P_SPEED = 250
P_W_COOLDOWN = 0.1

# Bullet attributes
B_SPEED = 300
B_DAMAGE = 1

# Enemy attributes
E_HITBOX_X = 32
E_HITBOX_Y = 24
E_SPEED = 150
E_HP = 1
E_SHOOTER_HP = 5
E_SHOOTER_SPEED = 100
E_SHOTS = 5
E_COOLDOWN = 1

# world attributes
LANES = [60, 120, 180, 240, 300]


# Waves
WAVE_1 = [
    (None, 0, 2, False),
    (0, 0, 0.5, False),
    (0, 0, 0, False),
    (0, 1, 0.5, False),
    (0, 1, 0, False),
    (0, 2, 0.5, False),
    (0, 2, 0, False),
    (0, 3, 0.5, False),
    (0, 3, 0, False),
    (0, 4, 0.5, False),
    (0, 4, 1, False),
    (1, 0, 0, True),
    (1, 4, 5, True),
    (1, 1, 0, False),
    (1, 2, 0, False),
    (1, 3, 0, False),
]
