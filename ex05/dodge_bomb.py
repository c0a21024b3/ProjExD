import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, size, bgname):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(bgname)
        self.bg_rect = self.bg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rect)
        

class Bird:
    def __init__(self, fname, zoom, place):
        self.sfc = pg.image.load(fname)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rect = self.sfc.get_rect()
        self.rect.center = place

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rect)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            self.rect.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rect.centery += 1
        if key_states[pg.K_LEFT]:
            self.rect.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rect.centerx += 1
        
        yoko, tate = check_bound(self.rect, scr.rect)
        if (yoko, tate) != (0,0):
            self.rect.centerx += yoko
            self.rect.centery += tate

        self.blit(scr)


class Bomb:
    def __init__(self, color, r, v, scr: Screen):
        self.sfc = pg.Surface((r*2, r*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (r, r), r)
        self.rect = self.sfc.get_rect()
        self.rect.centerx = random.randint(0, scr.rect.width)
        self.rect.centery = random.randint(0, scr.rect.height)
        self.vx, self.vy = v

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rect)
    
    def update(self, scr: Screen):
        self.rect.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rect, scr.rect)
        if yoko != 0:
            self.vx *= -1
        if tate != 0:
            self.vy *= -1
        self.blit(scr)


def main():
    clock = pg.time.Clock()

    # 練習1：スクリーンと背景画像
    # pg.display.set_caption("逃げろ！こうかとん")
    # screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    # screen_rct = screen_sfc.get_rect()            # Rect
    # bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    # bgimg_rct = bgimg_sfc.get_rect()              # Rect
    # screen_sfc.blit(bgimg_sfc, bgimg_rct)
    screen = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    screen.blit()

    # 練習3：こうかとん
    # kkimg_sfc = pg.image.load("fig/6.png")    # Surface
    # kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  # Surface
    # kkimg_rct = kkimg_sfc.get_rect()          # Rect
    # kkimg_rct.center = 900, 400
    koka = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5：爆弾
    # bmimg_sfc = pg.Surface((20, 20)) # Surface
    # bmimg_sfc.set_colorkey((0, 0, 0)) 
    # pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    # bmimg_rct = bmimg_sfc.get_rect() # Rect
    # bmimg_rct.centerx = random.randint(0, screen_rct.width)
    # bmimg_rct.centery = random.randint(0, screen_rct.height)
    # vx, vy = +1, +1 # 練習6
    bomb = Bomb((255, 0, 0), 10, (1,1), screen)

    while True:
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        # key_states = pg.key.get_pressed() # 辞書
        # if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        # if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        # if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        # if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        # 練習7
        # if check_bound(kkimg_rct, screen_rct) != (1, 1): # 領域外だったら
        #     if key_states[pg.K_UP]    == True: kkimg_rct.centery += 1
        #     if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 1
        #     if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 1
        #     if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        koka.update(screen)


        # 練習6
        #bmimg_rct.move_ip(vx, vy)
        # 練習5
        # screen_sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習7
        #yoko, tate = check_bound(bmimg_rct, screen_rct)
        #vx *= yoko
        #vy *= tate
        bomb.update(screen)

        # 練習8
        # if kkimg_rct.colliderect(bmimg_rct): return
        if koka.rect.colliderect(bomb.rect):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rect: pg.Rect, scr_rect: pg.Rect):
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