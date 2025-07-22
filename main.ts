// Don : Dificultad creciente, enemigos avanzados, más power ups, todo en pantalla (100% MakeCode Arcade compatible)
//  Fondo espacial bonito y colorido
scene.setBackgroundImage(img`
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
`)
let don_pollo_img = img`
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
`
let pollo_bala_img = img`
    . . 2 2 . .
    . 2 4 2 2 .
    2 2 2 2 2 2
    . 2 1 2 . .
    . 2 2 2 . .
    . . . . . .
    . . . . . .
    . . . . . .
`
let enemigo_img = img`
    . . 3 3 3 3 3 . .
    . 3 3 3 3 3 3 3 .
    3 3 3 3 3 3 3 3 3
    3 3 6 3 3 6 3 3 3
    3 3 3 3 3 3 3 3 3
    3 6 6 3 3 6 6 3 3
    . 3 3 6 6 3 3 3 .
    . . 3 3 3 3 3 . .
`
let enemigo_bala_img = img`
    . . 8 8 . .
    . 8 6 8 8 .
    8 8 8 8 8 8
    . 8 6 8 . .
    . 8 8 8 . .
    . . . . . .
    . . . . . .
    . . . . . .
`
let powerup_imgs = [img` # Vida extra
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
    `, img` # Multidisparo
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
    `, img` # Escudo
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
    `]
let POWERUP_LIFE = 0
let POWERUP_MULTI = 1
let POWERUP_SHIELD = 2
let don_pollo = sprites.create(don_pollo_img, SpriteKind.Player)
don_pollo.setPosition(20, 60)
controller.moveSprite(don_pollo, 100, 100)
don_pollo.setStayInScreen(true)
scene.cameraFollowSprite(don_pollo)
info.setLife(3)
let has_shield = false
let multi_shot = false
let start_time = game.runtime()
let enemigo_interval = 2000
let enemigo_speed = 50
let enemigo_shoot_cd = 1000
let enemigo_hp = 1
let powerup_interval = 7000
function level_up() {
    
    let tiempo = Math.idiv(game.runtime() - start_time, 20000)
    enemigo_speed = 50 + tiempo * 10
    enemigo_interval = Math.max(700, 2000 - tiempo * 150)
    enemigo_shoot_cd = Math.max(300, 1000 - tiempo * 60)
}

