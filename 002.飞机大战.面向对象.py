import random
import time

import pygame
from pygame.constants import *

#玩家飞机类
class HomePlan(object):
    def __init__(self,screen):
        # 创建一个图片，当玩家飞机
        self.player = pygame.image.load("./images/me1.png")
        # 初始坐标
        self.x = 190
        self.y = 500
        # 飞行速度
        self.speed = 5
        self.screen = screen
        #子弹列表
        self.bullets = []

    def key_control(self):
        # 连续监听键盘
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            #控制飞机的飞行范围
            if self.y > 0:
                self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            #控制飞机的飞行范围
            if self.y < 600:
                self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            #控制飞机的飞行范围
            if self.x > 0:
                self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            #控制飞机的飞行范围
            if self.x < 378:
                self.x += self.speed
        if key_pressed[K_SPACE]:
            #按下空格键发送子弹
            bullet = Billet(self.screen, self.x, self.y)
            self.bullets.append(bullet)

    def display(self):
        # 把背飞机景图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        #遍历子弹
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

#敌人飞机类
class EnemyPlan(object):
    def __init__(self,screen):
        # 创建一个图片，当敌方飞机
        self.player = pygame.image.load("./images/enemy1.png")
        # 初始坐标
        self.x = 0
        self.y = 0
        # 飞行速度
        self.speed = 1
        self.screen = screen
        #子弹列表
        self.bullets = []
        #敌机移动方向
        self.direction = 'right'

    def display(self):
        # 把背飞机景图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        #遍历子弹
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

        if self.x > 480 - 45:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        """自动发射子弹 创建子弹对象 添加进列表"""
        random_mub = random.randint(1,20)
        if random_mub == 8:
            bullet = EnemyBillet(self.screen,self.x,self.y)
            self.bullets.append(bullet)


#子弹类
class EnemyBillet(object):
    def __init__(self,screen,x,y):
        #坐标
        self.x = x+50/2-8/2
        self.y = y+39
        #图片
        self.image = pygame.image.load("./images/bullet1.png")
        #窗口
        self.screen = screen
        self.speed = 10

    def display(self):
        #显示子弹到窗口
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        #修改子弹的位置
        self.y +=self.speed


#敌机子弹类
class Billet(object):
    def __init__(self,screen,x,y):
        #坐标
        self.x = x+51-3
        self.y = y-11
        #图片
        self.image = pygame.image.load("./images/bullet2.png")
        #窗口
        self.screen = screen
        self.speed = 10

    def display(self):
        #显示子弹到窗口
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        #修改子弹的位置
        self.y -=self.speed


class GameSound(object):
    def __init__(self):
        pygame.mixer.init() #音乐模块初始化
        pygame.mixer.music.load("./images/BGM.mp3") #导入音乐
        pygame.mixer.music.set_volume(0.5) #设置音乐大小

    def playBGM(self):
        pygame.mixer.music.play(-1) #开始播放音乐

def main():
    sound = GameSound()
    sound.playBGM()
    #1创建一个窗口
    screen=pygame.display.set_mode((480,700),5,43)
    #2创建一个图片，当背景图片
    background =pygame.image.load("./images/background.png")
    #3创建玩家飞机的对象
    player = HomePlan(screen)
    #4创建敌方飞机的对象
    enemyplan = EnemyPlan(screen)

    while True:
        # 把背景图片贴到窗口中
        screen.blit(background, (0, 0))


        #获取事件
        for event in pygame.event.get():
            #判断事件的类型
            if event.type == pygame.QUIT:
                #关闭窗口
                pygame.quit()
                #python程序退出
                exit()

        #监控飞机的按键
        player.key_control()
        #显示我方飞机
        player.display()
        #显示敌方飞机
        enemyplan.display()
        #敌方飞机自动移动
        enemyplan.auto_move()
        #敌方飞机自动发射子弹
        enemyplan.auto_fire()

        #显示窗口中的内容
        pygame.display.update()
        time.sleep(0.005)




if __name__ == '__main__':
    main()