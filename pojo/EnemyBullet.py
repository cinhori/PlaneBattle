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
from BaseBullet import *


class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super(EnemyBullet, self)\
            .__init__(screen, x + 25, y + 40, "../photo/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 750:
            return True
        else:
            return False
