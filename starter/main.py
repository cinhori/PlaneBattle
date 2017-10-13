#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 13:00
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Contact : lilei93s@163.com

import pygame
from pygame.locals import *
import time

'''
    1. 搭建界面，主要完成窗口和背景图的显示
'''

def main():
    # 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("../photo/background.png").convert()

    hero = pygame.image.load("../photo/hero1.png").convert()

    x = 210
    y = 700
    # 把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()

        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 判断是否是点击了退出按钮
            if event.type == pygame.locals.QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x -= 5
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 5
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

        time.sleep(0.01)

if __name__ == "__main__":
    main()