#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 16:41
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : HeroBullet.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame


class HeroBullet:
    def __init__(self, screen, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load("../photo/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 20
