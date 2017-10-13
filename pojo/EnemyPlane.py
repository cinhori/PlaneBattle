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
from BasePlane import *


"""
    敌机类
"""


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        self.imageList = ["../photo/enemy0.png", "../photo/enemy0_down1.png",
                          "../photo/enemy0_down2.png", "../photo/enemy0_down3.png",
                          "../photo/enemy0_down4.png"]
        BasePlane.__init__(self, screen, 0, 0, 51, 39,  self.imageList)
        self.direction = "right"

    def display(self):
        super(EnemyPlane, self).display()
        self.fire()

    def move(self):
        if self.direction == "right":
            self.moveRight()
        elif self.direction == "left":
            self.moveLeft()

        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        randomNum = random.randint(1, 100)
        bullet = EnemyBullet(self.screen, self.x, self.y)
        if randomNum in [5, 10, 15, 20]:
            BasePlane.fire(self, bullet)
