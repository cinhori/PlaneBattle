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
import time


class BasePlane(object):
    def __init__(self, screen, x, y, width, length, imageList):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.screen = screen
        self.imageList = imageList
        self.__image = pygame.image.load(self.imageList[0]).convert()
        self.bulletList = []
        self.hit = False
        self.__imageNum = 1

    def display(self):
        if self.hit:
            image = self.imageList[0]
            self.__imageNum += 1
            if self.__imageNum == 5:
                image = self.imageList[1]
            elif self.__imageNum == 10:
                image = self.imageList[2]
            elif self.__imageNum == 15:
                image = self.imageList[3]
            elif self.__imageNum == 20:
                image = self.imageList[4]
            self.__image = pygame.image.load(image).convert()
            if image == self.imageList[4]:
                time.sleep(1)
                exit()

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

    def isHit(self, bulletList):
        for bullet in bulletList:
            if bullet.x in range(self.x, self.x + self.width) \
                    and bullet.y in range(self.y, self.y + self.length):
                self.hit = True
                break
            else:
                self.hit = False




