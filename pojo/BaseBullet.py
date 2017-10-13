#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 22:27
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : BaseBullet.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame


class BaseBullet(object):
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass

    def judge(self):
        pass
