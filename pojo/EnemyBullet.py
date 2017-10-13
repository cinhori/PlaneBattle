#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 17:16
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : EnemyBullet.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame


class EnemyBullet():
    def __init__(self, screen, x, y):
        self.x = x + 25
        self.y = y + 40
        self.screen = screen
        self.image = pygame.image.load("../photo/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 750:
            return True
        else:
            return False
