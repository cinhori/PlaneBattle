#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 15:07
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : HeroPlane.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame
from HeroBullet import HeroBullet


class HeroPlane:
    def __init__(self, screen):
        self.x = 210
        self.y = 700
        self.screen = screen
        self.__image = pygame.image.load("../photo/hero1.png").convert()
        self.bulletList = []

    def display(self):
        self.screen.blit(self.__image, (self.x, self.y))

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        self.x -= 5

    def moveRight(self):
        self.x += 5

    def fire(self):
        self.bulletList.append(HeroBullet(self.screen, self.x, self.y))
