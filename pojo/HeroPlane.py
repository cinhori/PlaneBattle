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
        self.imageList = ["../photo/hero1.png", "../photo/hero_blowup_n1.png",
                          "../photo/hero_blowup_n2.png", "../photo/hero_blowup_n3.png",
                          "../photo/hero_blowup_n4.png"]
        BasePlane.__init__(self, screen, 210, 700, 100, 124, self.imageList)

    def fire(self):
        bullet = HeroBullet(self.screen, self.x, self.y)
        BasePlane.fire(self, bullet)
