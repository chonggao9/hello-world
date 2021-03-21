import time

import pygame
from pygame.constants import *


def main():
    #创建一个窗口
    screen=pygame.display.set_mode((480,700),5,43)
    #创建一个图片，当背景图片
    background =pygame.image.load("./images/background.png")
    #创建一个图片，当玩家飞机
    player =pygame.image.load("./images/me1.png")

    #初始坐标
    x = 190
    y = 500
    #飞行速度
    speed = 5

    while True:
        # 把背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 把背景图片贴到窗口中
        screen.blit(player, (x, y))

        #获取事件
        for event in pygame.event.get():
            #判断事件的类型
            if event.type == pygame.QUIT:
                #关闭窗口
                pygame.quit()
                #python程序退出
                exit()

        #连续监听键盘
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            print("上")
            y -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print("下")
            y += speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("左")
            x -= speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("右")
            x += speed
        if key_pressed[K_SPACE]:
            print("空格")

        #显示窗口中的内容
        pygame.display.update()
        time.sleep(0.005)




if __name__ == '__main__':
    main()