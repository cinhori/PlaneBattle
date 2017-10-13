#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 16:59
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : EnemyPlane.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
from pojo.EnemyBullet import *
import random


"""
    敌机类
"""
import pygame


class EnemyPlane():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.__image = pygame.image.load("../photo/enemy0.png")
        self.direction = "right"
        self.bulletList = []

    def display(self):
        self.screen.blit(self.__image, (self.x, self.y))
        self.fire()

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bulletList.remove(bullet)

    def move_left(self):
        self.x += 5

    def move_down(self):
        self.y += 5

    def move_right(self):
        self.x -= 5

    def move(self):
        if self.direction == "right":
            self.move_left()
        elif self.direction == "left":
            self.move_right()

        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        randomNum = random.randint(1, 100)
        if randomNum in [5, 10, 15, 20]:
            self.bulletList.append(EnemyBullet(self.screen, self.x, self.y))
