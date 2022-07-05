import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    #clock.tick(0.5)

    pg.display.set_caption("逃げろ！こうかとん！")
    screen = pg.display.set_mode((1600, 900))

    bg = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg.get_rect()
    screen.blit(bg, bg_rect)

    koka = pg.image.load("fig/3.png")
    koka = pg.transform.rotozoom(koka, 0, 2.0)
    koka_rect = koka.get_rect()
    koka_rect.center = 900, 400

    while True:
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
        screen.blit(koka, koka_rect)



        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()