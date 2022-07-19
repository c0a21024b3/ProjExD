import sys              # sysモジュールを読み込む
import pygame as pg     # pygameモジュールをpgとして読み込む
from random import randint     # randomモジュール内にあるrandint関数を読み込む


bar_num = 5  # 落ちてくる障害物の最大数
rz_num = 1000 # 弾数を1000で初期化
HP = 500 # HPを500で初期化


# Screen クラスを定義
class Screen:
    def __init__(self, title, wh, image):   # wh:幅高さタプル, image:背景画像ファイル名
        pg.display.set_caption(title)       # タイトルバーにtitleを表示
        self.sfc = pg.display.set_mode(wh)      # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.bgi_sfc = pg.image.load(image)     # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect  

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


# Player クラスを定義
class Player:
    def __init__(self, image, size, xy):    # image:画像ファイル名, size:拡大率, xy:初期座標タプル
        self.sfc = pg.image.load(image)                        # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)    # Surface
        self.rct = self.sfc.get_rect()                         # Rect
        self.rct.center = xy    # こうかとんを表示する座標をxyに設定
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1.0
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1.0
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1.0
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1.0
        self.blit(scr)

    # 移動するキャラクターがビームを打つメソッド
    def atack(self, scr: Screen):
        key_states = pg.key.get_pressed()
        
        if key_states[pg.K_SPACE]:
            pass


# Barクラスを定義
class Bar:
    def __init__(self, size, color, scr: Screen):
        self.sfc = pg.Surface(size)
        pg.Surface.fill(self.sfc, color)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width-self.rct.width) # 横の位置をランダムに設定
        self.rct.centery = -randint(0, 500) # 落ちてくるタイミングをずらすため縦の位置を画面外でランダムに設定
        self.w, self.h = size
        self.rct.width = randint(80, self.w)
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr: Screen):
        self.rct.move_ip(0, 1) # 速度1で落下
        if self.rct.centery > scr.rct.height: # 画面下まで行ったらもう一度落ちてくる
            self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
            self.rct.centery = -randint(0, 500)
            self.rct.width = randint(80, self.w)
        scr.sfc.blit(self.sfc, self.rct)


# Itemクラスを定義
class Item:
    def __init__(self, r, color, scr: Screen):
        self.sfc = pg.Surface((r*2, r*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (r, r), r)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
        self.rct.centery = 0
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr: Screen):
        self.rct.move_ip(0, 1) # 速度1で落下
        scr.sfc.blit(self.sfc, self.rct)


def check_bound(rct, scr_rct):
    
    # [1] rct: こうかとん or 爆弾のRect
    # [2] scr_rct: スクリーンのRect

    yoko, tate = 1, 1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right:
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


def main():
    global rz_num, HP
    inv_point = 0 # 無敵ゲージを0で初期化
    inv = False # 無敵かどうかの判定
    st = 0 # 無敵の開始時刻を保存する関数

    clock = pg.time.Clock()  # 時間計測用のオブジェクト
    screen = Screen("", (700, 900), "fig/pg_bg.jpg")
    screen.blit()

    player = Player("fig/5.png", 1.5, (350, 848))

    bars = [0 for i in range(bar_num)]
    for i in range(bar_num):
        bars[i] = Bar((120, 30), (0,0,0), screen)
        bars[i].blit(screen)
    # bar = Bar((30, 30), (125, 125, 125), screen)
    # bar.blit(screen)

    rz_plus = Item(10, (255, 0, 0), screen)
    rz_plus.rct.centerx = -30 # 弾数追加アイテムを画面外で初期化

    heal = Item(10, (0, 128, 0), screen)
    heal.rct.centerx = -30

    while True:
        time = pg.time.get_ticks()
        screen.blit()

        font = pg.font.Font(None, 80)
        txt = font.render(f"rz:{rz_num}", True, (0, 0, 0))
        screen.sfc.blit(txt, (0, 90))

        font = pg.font.Font(None, 80)
        txt = font.render(f"HP:{HP}", True, (0, 0, 0))
        screen.sfc.blit(txt, (0, 40))

        font = pg.font.Font(None, 40)
        txt = font.render("x"*inv_point, True, (0, 0, 0))
        screen.sfc.blit(txt, (0, 150))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LSHIFT and inv_point == 10:
                    inv_point = 0
                    inv = True
                    st = time # 無敵の開始時刻を保存
        if time - st > 5000: # 無敵は5秒継続
            inv = False
        
        player.update(screen)
        for bar in bars:
            bar.update(screen)
            
            if player.rct.colliderect(bar.rct) and not inv: #無敵状態でなければ
                return
        
        if 0 <= time % 25000 <= 20: # 25秒おき
            rz_plus = Item(10, (255, 0, 0), screen) # 画面内に弾数追加アイテムを生成
            for bar in bars: # 障害物と被らないように
                while rz_plus.rct.colliderect(bar.rct):
                    rz_plus = Item(10, (255, 0, 0), screen)
        rz_plus.update(screen)

        if player.rct.colliderect(rz_plus.rct): # 弾数追加の処理
            rz_num += 3
            rz_plus.rct.centerx = -30
        
        if 0 <= time %40000 <= 20: # 40秒おき
            heal = Item(10, (0, 128, 0), screen) # 画面内に体力回復アイテムを生成
            for bar in bars: # 障害物と被らないように
                while heal.rct.colliderect(bar.rct):
                    heal = Item(10, (0, 128, 0), screen)
        heal.update(screen)

        if player.rct.colliderect(heal.rct): # 体力回復の処理
            HP += 100
            heal.rct.centerx = -30

        pg.display.update()   # 画面を更新する
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()