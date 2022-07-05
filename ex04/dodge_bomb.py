import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    #clock.tick(0.5)

    pg.display.set_caption("逃げろ！こうかとん！")
    screen = pg.display.set_mode((1600, 900))
    screen_rect = screen.get_rect()

    bg = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg.get_rect()
    screen.blit(bg, bg_rect)

    koka = pg.image.load("fig/3.png")
    koka = pg.transform.rotozoom(koka, 0, 2.0)
    koka_rect = koka.get_rect()
    koka_rect.center = 900, 400

    bomb = pg.Surface((20, 20))
    bomb.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    bomb_rect = bomb.get_rect()
    bomb_rect.center = random.randint(0,screen_rect.width),                        random.randint(0, screen_rect.height)
    vx, vy = 1, 1

    while True:
        #clock.tick(1000)
        screen.blit(bg, bg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        key_states = pg.key.get_pressed()# キー入力状態の辞書
        # 上下左右に動かす
        if key_states[pg.K_UP]:
            koka_rect.centery -= 1
        if key_states[pg.K_DOWN]:
            koka_rect.centery += 1
        if key_states[pg.K_LEFT]:
            koka_rect.centerx -= 1
        if key_states[pg.K_RIGHT]:
            koka_rect.centerx += 1
        
        yoko, tate = check_bound(koka_rect, screen_rect)
        if (yoko, tate) != (0,0):
            koka_rect.centerx += yoko
            koka_rect.centery += tate
        screen.blit(koka, koka_rect)

        bomb_rect.move_ip(vx, vy)
        yoko, tate = check_bound(bomb_rect, screen_rect)
        if yoko != 0:
            vx *= -1
        if tate != 0:
            vy *= -1
        screen.blit(bomb, bomb_rect)
        clock.tick(1000)

        pg.display.update()

def check_bound(rect, scr_rect):
    yoko, tate = 0, 0
    if rect.left < scr_rect.left:
        yoko = 1
    if rect.right > scr_rect.right:
        yoko = -1
    if rect.top < scr_rect.top:
        tate = 1
    if rect.bottom > scr_rect.bottom:
        tate = -1
    return (yoko, tate)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()