#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 15:19
# @Author  : cinhori
# @Desc    : 
# @Site    : 
# @File    : InitScreen.py
# @Software: PyCharm
# @Contact : lilei93s@163.com
import pygame
import pygame.display


class InitScreen:
    def __init__(self):
        # 创建一个窗口，用来显示内容
        self.__screen = pygame.display.set_mode((480, 852), 0, 32)

        # 创建一个和窗口大小的图片，用来充当背景
        self.__background = pygame.image.load("../photo/background.png").convert()

    def display(self):
        self.__screen.blit(self.__background, (0, 0))

    def getScreen(self):
        return self.__screen