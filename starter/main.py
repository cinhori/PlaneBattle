#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 13:00
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Contact : lilei93s@163.com

from pygame.locals import *
import time
from pojo.HeroPlane import *
from pojo.InitScreen import *
from pojo.EnemyPlane import *

'''
    启动方法
'''


def main():
    screen = InitScreen()
    hero = HeroPlane(screen.getScreen())
    enemy = EnemyPlane(screen.getScreen())

    while True:
        screen.display()
        hero.display()
        enemy.display()
        enemy.move()
        pygame.display.update()

        keyReader(hero)

        if not hero.hit and hero.isHit(enemy.bulletList):
            hero.hit = True

        if not enemy.hit and enemy.isHit(hero.bulletList):
            enemy.hit = True

        time.sleep(0.05)


def keyReader(hero):
    "获取键盘事件"
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
                hero.moveLeft()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.moveRight()
            elif event.key == K_b:
                print('boom')
                hero.hit = True
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero.fire()


if __name__ == "__main__":
    main()
