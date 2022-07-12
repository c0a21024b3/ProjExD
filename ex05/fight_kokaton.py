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
        

class Bird():
    def __init__(self, fname, zoom, place):
        self.sfc = pg.image.load(fname)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rect = self.sfc.get_rect()
        self.rect.center = place
        self.ball = None 

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
    
    # wasdキーで球を発射
    def attack(self):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_w]:
            self.ball = Ball(5, (0, 128, 0), (0, -1), self.rect.center)
        if key_states[pg.K_a]:
            self.ball = Ball(5, (0, 128, 0), (-1, 0), self.rect.center)
        if key_states[pg.K_s]:
            self.ball = Ball(5, (0, 128, 0), (0, 1), self.rect.center)
        if key_states[pg.K_d]:
            self.ball = Ball(5, (0, 128, 0), (1, 0), self.rect.center)


class Bomb():
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


# 敵のクラス
class Enemy():
    def __init__(self, size, color, tar, scr: Screen):
        self.sfc = pg.Surface(size)
        pg.Surface.fill(self.sfc, color)
        self.rect = self.sfc.get_rect()
        self.rect.centerx = random.randint(0, scr.rect.width)
        self.rect.centery = random.randint(0, scr.rect.height)
        v = self.get_v(tar)
        self.ball = Ball(5, (0, 0, 255), v, self.rect.center)
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rect)
    
    # ターゲットが自身より右にいるか左にいるかの判定
    def get_v(self, tar):
        tx = tar.rect.centerx
        x = self.rect.centerx
        if x >= tx:
            vx = -2
        else:
            vx = 2
        return (vx, 0)

    def attack(self, tar):
        v = self.get_v(tar)
        self.ball = Ball(7, (0, 0, 255), v, self.rect.center)


# こうかとんと敵が放つ球のクラス
class Ball():
    def __init__(self, size, color, v,  place):
        self.sfc = pg.Surface((size*2, size*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rect = self.sfc.get_rect()
        self.rect.center = place
        self.vx, self.vy = v

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rect)
    
    def update(self, scr: Screen):
        self.rect.move_ip(self.vx, self.vy)
        self.blit(scr)
        
    
def main():
    clock = pg.time.Clock()

    screen = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    screen.blit()

    koka = Bird("fig/6.png", 2.0, (900, 400))
    bomb = Bomb((255, 0, 0), 10, (1,1), screen)
    enemy = Enemy((30, 30), (0, 0, 0), koka, screen)

    while True:
        time = pg.time.get_ticks()
        screen.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        koka.update(screen)
        bomb.update(screen)
        enemy.blit(screen)
        koka.attack()
        if koka.ball:
            koka.ball.update(screen)
            koka.ball.blit(screen)
            if enemy.rect.colliderect(koka.ball.rect):
                enemy = Enemy((30, 30), (0, 0, 0), koka, screen)
        
        # 2.5秒後から5秒おきに敵が攻撃
        if 2500 <= time % 5000 <= 2550:
            enemy.attack(koka)
            enemy.ball.blit(screen)
        
        if time >= 2500:
            enemy.ball.update(screen)

        if koka.rect.colliderect(bomb.rect):
            return

        if koka.rect.colliderect(enemy.ball.rect):
            return
        
        pg.display.update()
        clock.tick(1000)


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