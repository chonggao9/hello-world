import random
import time

import pygame
from pygame.constants import *

#玩家飞机类
class HomePlan(pygame.sprite.Sprite):
    def __init__(self,screen):
        #精灵类代码继承必须
        pygame.sprite.Sprite.__init__(self)

        # 创建一个图片，当玩家飞机
        self.player = pygame.image.load("./images/me1.png")

        #根据images获取矩形对象
        self.rect = self.player.get_rect() #rect :矩形
        self.rect.topleft=[190, 500]

        # 初始坐标
        #self.x = 190
        #self.y = 500

        # 飞行速度
        self.speed = 5
        self.screen = screen
        #子弹列表
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        # 连续监听键盘
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            #控制飞机的飞行范围
            if self.rect.top > 0:
                self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            #控制飞机的飞行范围
            if self.rect.bottom < 700:
                self.rect.bottom += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            #控制飞机的飞行范围
            if self.rect.left > 0:
                self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            #控制飞机的飞行范围
            print(self.rect.right)
            if self.rect.right < 480:
                self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            #按下空格键发送子弹
            bullet = Billet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()


    def display(self):
        # 把背飞机景图片贴到窗口中
        self.screen.blit(self.player, self.rect)

        #遍历子弹
        #for bullet in self.bullets  :
        #    bullet.auto_move()
        #    bullet.display()

        #更新子弹坐标
        self.bullets.update()

        #把所有子弹全部添加到屏幕
        self.bullets.draw(self.screen)

#敌人飞机类
class EnemyPlan(pygame.sprite.Sprite):
    def __init__(self,screen):
        # 精灵类代码继承必须
        pygame.sprite.Sprite.__init__(self)

        # 创建一个图片，当敌方飞机
        self.player = pygame.image.load("./images/enemy1.png")

        #根据images获取矩形对象
        self.rect = self.player.get_rect() #rect :矩形
        self.rect.topleft=[0, 0]

        # 初始坐标
        #self.x = 0
        #self.y = 0

        # 飞行速度
        self.speed = 1
        self.screen = screen

        #子弹列表
        self.bullets = pygame.sprite.Group()
        #敌机移动方向
        self.direction = 'right'

    def display(self):
        # 把背飞机景图片贴到窗口中
        self.screen.blit(self.player,self.rect)
        #遍历子弹
        #for bullet in self.bullets:
        #    bullet.auto_move()
        #    bullet.display()

        # 更新子弹坐标
        self.bullets.update()

        # 把所有子弹全部添加到屏幕
        self.bullets.draw(self.screen)

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed

        if self.rect.right > 480 - 45:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'

    def auto_fire(self):
        """自动发射子弹 创建子弹对象 添加进列表"""
        random_mub = random.randint(1,20)
        if random_mub == 8:
            bullet = EnemyBillet(self.screen,self.rect.left,self.rect.top)
            self.bullets.add(bullet)


#敌机子弹类
class EnemyBillet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        pygame.sprite.Sprite.__init__(self)

        #初始化图片
        self.image = pygame.image.load("./images/bullet1.png")

        # 获取矩形对象
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+50/2-8/2,y+39]

        #坐标
        #self.x = x+50/2-8/2
        #self.y = y+39

        #窗口
        self.screen = screen
        self.speed = 10

    def update(self):
        # 修改子弹的位置
        self.rect.top += self.speed
        # 如果子弹移除屏幕上方，则销毁子弹对象
        if self.rect.top > 852:
            self.kill()

#玩家子弹类
class Billet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        pygame.sprite.Sprite.__init__(self)

        #初始化图片
        self.image = pygame.image.load("./images/bullet2.png")

        #获取矩形对象
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+51-3,y-11]

        #坐标
        #self.x = x+51-3
        #self.y = y-11

        #窗口
        self.screen = screen
        self.speed = 10

    def update(self):
        # 修改子弹的位置
        self.rect.top -= self.speed
        # 如果子弹移除屏幕上方，则销毁子弹对象
        if self.rect.top < -22:
            self.kill()


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
        time.sleep(0.01)




if __name__ == '__main__':
    main()
