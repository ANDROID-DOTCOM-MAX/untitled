#Don : Dificultad creciente, enemigos avanzados, más power ups, todo en pantalla (100% MakeCode Arcade compatible)

# Fondo espacial bonito y colorido
scene.set_background_image(img("""
    7 7 7 7 7 7 1 7 7 7 7 7 7 7 7 7
    7 1 7 7 7 7 7 7 7 7 7 2 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 5 5 7 1 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 2 7
    7 7 6 6 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 2 7 7 7 7 4 7
    7 7 7 7 7 3 3 3 7 7 7 7 7 7 7 7
    7 7 7 1 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 2 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 1 7 7 7
    7 7 7 7 7 1 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
"""))

don_pollo_img = img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 2 . . . . .
    . . . . . . 2 2 2 2 2 . . . . .
    . . . . . 2 2 2 2 2 2 2 . . . .
    . . . . 5 5 5 2 2 2 5 5 5 . . .
    . . . . 5 5 5 2 2 2 5 5 5 . . .
    . . . . . . 2 2 2 2 2 . . . . .
    . . . . . . 2 2 2 2 2 . . . . .
    . . . . . . . 4 2 4 . . . . . .
    . . . . . 1 . 1 1 1 . 1 . . . .
    . . . . . f 6 f f 6 f . . . . .
    . . . . . f 6 f f 6 f . . . . .
    . . . . . f f f f f f . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")

pollo_bala_img = img("""
    . . 2 2 . .
    . 2 4 2 2 .
    2 2 2 2 2 2
    . 2 1 2 . .
    . 2 2 2 . .
    . . . . . .
    . . . . . .
    . . . . . .
""")

enemigo_img = img("""
    . . 3 3 3 3 3 . .
    . 3 3 3 3 3 3 3 .
    3 3 3 3 3 3 3 3 3
    3 3 6 3 3 6 3 3 3
    3 3 3 3 3 3 3 3 3
    3 6 6 3 3 6 6 3 3
    . 3 3 6 6 3 3 3 .
    . . 3 3 3 3 3 . .
""")

enemigo_bala_img = img("""
    . . 8 8 . .
    . 8 6 8 8 .
    8 8 8 8 8 8
    . 8 6 8 . .
    . 8 8 8 . .
    . . . . . .
    . . . . . .
    . . . . . .
""")

powerup_imgs = [
    img(""" # Vida extra
        . . . . . . . . . . . . . . . .
        . . . . . 7 7 7 . . . . . . . .
        . . . . 7 7 9 7 7 . . . . . . .
        . . . 7 9 9 9 9 7 . . . . . . .
        . . . 7 9 7 7 9 7 . . . . . . .
        . . . 7 9 7 7 9 7 . . . . . . .
        . . . 7 9 9 9 9 7 . . . . . . .
        . . . . 7 7 9 7 7 . . . . . . .
        . . . . . 7 7 7 . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    img(""" # Multidisparo
        . . . . . 1 1 1 . . . . . . . .
        . . . . 1 1 5 1 1 . . . . . . .
        . . . 1 5 5 5 5 1 . . . . . . .
        . . . 1 5 1 1 5 1 . . . . . . .
        . . . 1 5 1 1 5 1 . . . . . . .
        . . . 1 5 5 5 5 1 . . . . . . .
        . . . . 1 1 5 1 1 . . . . . . .
        . . . . . 1 1 1 . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    img(""" # Escudo
        . . . . . 2 2 2 . . . . . . . .
        . . . . 2 2 1 2 2 . . . . . . .
        . . . 2 1 1 1 1 2 . . . . . . .
        . . . 2 1 2 2 1 2 . . . . . . .
        . . . 2 1 2 2 1 2 . . . . . . .
        . . . 2 1 1 1 1 2 . . . . . . .
        . . . . 2 2 1 2 2 . . . . . . .
        . . . . . 2 2 2 . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """)
]
POWERUP_LIFE = 0
POWERUP_MULTI = 1
POWERUP_SHIELD = 2

don_pollo = sprites.create(don_pollo_img, SpriteKind.player)
don_pollo.set_position(20, 60)
controller.move_sprite(don_pollo, 100, 100)
don_pollo.set_stay_in_screen(True)
scene.camera_follow_sprite(don_pollo)
info.set_life(3)

has_shield = False
multi_shot = False

start_time = game.runtime()
enemigo_interval = 2000
enemigo_speed = 50
enemigo_shoot_cd = 1000
enemigo_hp = 1
powerup_interval = 7000

def level_up():
    global enemigo_speed, enemigo_interval, enemigo_shoot_cd, enemigo_hp, powerup_interval
    tiempo = (game.runtime() - start_time) // 20000
    enemigo_speed = 50 + tiempo * 10
    enemigo_interval = max(700, 2000 - tiempo * 150)
    enemigo_shoot_cd = max(300, 1000 - tiempo * 60)
