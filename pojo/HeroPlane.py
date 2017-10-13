#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 15:07
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : HeroPlane.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
from HeroBullet import HeroBullet
from BasePlane import *


class HeroPlane(BasePlane):
    def __init__(self, screen):
        BasePlane.__init__(self, screen, 210, 700, "../photo/hero1.png")

    def fire(self):
        bullet = HeroBullet(self.screen, self.x, self.y)
        BasePlane.fire(self, bullet)
