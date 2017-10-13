#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 17:45
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : BasePlane.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame


class BasePlane(object):
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        self.screen = screen
        self.__image = pygame.image.load(image).convert()
        self.bulletList = []

    def display(self):
        self.screen.blit(self.__image, (self.x, self.y))

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bulletList.remove(bullet)

    def moveLeft(self):
        self.x -= 5

    def moveDown(self):
        self.y += 5

    def moveRight(self):
        self.x += 5

    def fire(self, bullet):
        self.bulletList.append(bullet)
