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

    # 把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (210, 700))
        pygame.display.update()

        time.sleep(0.01)

if __name__ == "__main__":
    main()