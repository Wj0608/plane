# coding=utf-8
__author__ = 'DELL'

import pygame
import sys
from pygame.locals import *
from random import randrange




def init():
    pygame.init()
    #定义一个时间对象

    clock=pygame.time.Clock()

    #最大帧率

    speed=100

    screen_size=400,600   #screen屏幕大小

    pygame.display.set_mode(screen_size)   #窗口

    #全屏为.set_mode(screen_size,FULLSCREEN)

    pygame.mouse.set_visible(0)   #隐藏鼠标



    plane_image=pygame.image.load('plane.png')

    #导入飞机图片(图片大小应做调整)



    sprites=pygame.sprite.RenderUpdates()

    #创建Sprite的容器

    class plane(pygame.sprite.Sprite):

        def __init__(self):

            pygame.sprite.Sprite.__init__(self)

            self.image=plane_image

            self.rect=self.image.get_rect()

            self.rect.top=-self.rect.height

            self.rect.centerx=randrange(screen_size[0]-self.rect.width)+self.rect.width/2

     #控制飞机在窗口内

        def update(self):

            self.rect.top+=1

            if self.rect.top>screen_size[1]:

                self.kill()


    sprites.add(plane())

    #向容器中添加一个plane对象



    screen=pygame.display.get_surface()

    #可用于画图的Surface对象

    bg=(255,255,255)   #背景颜色RGB格式red-blue-green

    screen.fill(bg)   #屏幕填充背景颜色

    pygame.display.flip()   #显示更新后的屏幕




    def clear_callback(surf,rect):

    #清除旧Sprite图形

        surf.fill(bg,rect)

    while True:

        for event in pygame.event.get():

            if event.type=='QUIT':   #关闭窗口

                sys.exit()

            if event.type=='KEYDOWN'and event.key=='K_ESCAPE':

    #Esc退出

                sys.exit()

        sprites.clear(screen,clear_callback)

        sprites.update()
    #调用update()方法更新Sprites对象

        updates=sprites.draw(screen)

    #调用父类RenderUpdates的draw方法

    #返回需要更新的部分

        pygame.display.update(updates)
        clock.tick(speed)

def run():
    init()



if __name__ == '__main__':
    run()