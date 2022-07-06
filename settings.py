# -*- coding: UTF-8 -*-
"""
@author:91656
@file_name:settings.py
@time:2022/07/04 17:57
@IDE:PyCharm
@copyright:计算学堂
"""


class Settings:
    """保存《外星人入侵》游戏所有的设置的类"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        #子弹设置
        self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3