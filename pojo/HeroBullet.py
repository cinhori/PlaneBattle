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
from BaseBullet import *


class HeroBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super(HeroBullet, self)\
            .__init__(screen, x + 40, y - 20, "../photo/bullet.png")

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 10:
            return True
        else:
            return False
