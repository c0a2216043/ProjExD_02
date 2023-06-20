import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1000, 600


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bd_img = pg.Surface((20, 20))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_img.set_colorkey((0, 0, 0))
    clock = pg.time.Clock()
    tmr = 0
    
    bd_rct = bd_img.get_rect()
    vx, vy = 5, 5 
    
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)
    
    move_dict = {
        pg.K_UP: (0, -5),
        pg.K_DOWN: (0, +5),
        pg.K_LEFT: (-5, 0),
        pg.K_RIGHT: (+5, 0)
    }
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed()
        total_move = [0, 0]
        
        for key, move in move_dict.items():
            if key_lst[key]:
                total_move[0] += move[0]
                total_move[1] += move[1]
        kk_rct.move_ip(total_move)
        bd_rct.move_ip(vx, vy)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bd_img,bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    