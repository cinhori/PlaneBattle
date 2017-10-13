#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 16:59
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : EnemyPlane.py
# @Software: PyCharm
# @Contact : lilei93s@163.com

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

    def display(self):
        self.screen.blit(self.__image, (self.x, self.y))

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
        pass
