import pygame as pg
import sys
import random
import datetime

def main():
    clock = pg.time.Clock()

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

    #1つ目の爆弾を生成
    bomb1 = pg.Surface((20, 20))
    bomb1.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb1, (255, 0, 0), (10, 10), 10) # 赤色
    bomb1_rect = bomb1.get_rect()
    bomb1_rect.center = random.randint(0,screen_rect.width), random.randint(0, screen_rect.height)
    vx1, vy1 = 1, 1 # 縦横方向の速度

    # 残りの爆弾は画面外に生成
    bomb2 = pg.Surface((20, 20))
    bomb2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2, (0, 0, 255), (10, 10), 10) # 青色
    bomb2_rect = bomb2.get_rect()
    bomb2_rect.center = -50,-50 # 初期位置を画面外に設定
    vx2, vy2 = 0, 0 # 速度を0で初期化

    #以下同様
    bomb3 = pg.Surface((20, 20))
    bomb3.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb3, (0, 128, 0), (10, 10), 10) # 緑色
    bomb3_rect = bomb3.get_rect()
    bomb3_rect.center = -50,-50
    vx3, vy3 = 0, 0

    bomb4 = pg.Surface((20, 20))
    bomb4.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb4, (255, 255, 0), (10, 10), 10) # 黄色
    bomb4_rect = bomb4.get_rect()
    bomb4_rect.center = -50,-50
    vx4, vy4 = 0, 0

    bombs = [(bomb1, bomb1_rect), (bomb2, bomb2_rect), (bomb3, bomb3_rect),(bomb4, bomb4_rect)] # 爆弾のリスト


    while True:
        clock.tick(1000)
        time = pg.time.get_ticks() # 経過時間を取得

        screen.blit(bg, bg_rect)

        # 経過時間の表示
        font = pg.font.Font(None, 80)
        txt = font.render(str(time/1000)[:-1], True, (0, 0, 0))
        screen.blit(txt, (760, 40))

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

        bomb1_rect.move_ip(vx1, vy1)
        yoko, tate = check_bound(bomb1_rect, screen_rect)
        if yoko != 0:
            vx1 *= -1
        if tate != 0:
            vy1 *= -1
        screen.blit(bomb1, bomb1_rect)

        if 19950 <= time <= 20000: # 経過時間20秒なら 誤差込み
            vx2 = -1 * vx1 # 横は1つ目と逆
            vy2 = 2 * vy1 # 縦は1つ目の倍速
            # 1つ目の位置に移動
            bomb2_rect.centerx = bomb1_rect.centerx
            bomb2_rect.centery = bomb1_rect.centery
        bomb2_rect.move_ip(vx2, vy2)
        yoko, tate = check_bound(bomb2_rect, screen_rect)
        if yoko != 0:
            vx2 *= -1
        if tate != 0:
            vy2 *= -1
        screen.blit(bomb2, bomb2_rect)

        if 39950 <= time <= 40000: # 経過時間40秒なら 誤差込み
            vx3 = 2 * vx1 # 横は1つ目の倍速
            vy3 = -1 * vy1 # 縦は1つ目と逆
            # 1つ目の位置に移動
            bomb3_rect.centerx = bomb1_rect.centerx
            bomb3_rect.centery = bomb1_rect.centery
        bomb3_rect.move_ip(vx3, vy3)
        yoko, tate = check_bound(bomb3_rect, screen_rect)
        if yoko != 0:
            vx3 *= -1
        if tate != 0:
            vy3 *= -1
        screen.blit(bomb3, bomb3_rect)

        if 59950 <= time <= 60000: # 経過時間60秒なら 誤差込み
            vx4 = -2 * vx1 # 横は1つ目と逆で倍速
            vy4 = 2 * vy1 # 縦は1つ目の倍速
            # 1つ目の位置に移動
            bomb4_rect.centerx = bomb1_rect.centerx
            bomb4_rect.centery = bomb1_rect.centery
        bomb4_rect.move_ip(vx4, vy4)
        yoko, tate = check_bound(bomb4_rect, screen_rect)
        if yoko != 0:
            vx4 *= -1
        if tate != 0:
            vy4 *= -1
        screen.blit(bomb4, bomb4_rect)
        
        # 全ての爆弾について接触判定を行う
        for x in bombs:
            if koka_rect.colliderect(x[1]):
                return
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