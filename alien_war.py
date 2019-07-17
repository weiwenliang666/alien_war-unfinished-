from sett import AlienSett

from alien import Alien

from ship import Ship

from botton import Button

from game_stats import GameStats
from scoreboard import Scoreboard

import game_function as gf

from pygame.sprite import Group

import sys

import pygame


def run_game():
    #初始化pygame，设置和屏幕对象
    pygame.init()
    ai_sett = AlienSett()
    screen = pygame.display.set_mode(
        (ai_sett.screen_width, ai_sett.screen_height))
    pygame.display.set_caption("Press P to start")

    #创建Play按钮
    play_button = Button(ai_sett, screen, "Play")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_sett)
    sb = Scoreboard(ai_sett, screen, stats)

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(screen, ai_sett)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_sett,screen,ship,aliens)


    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_sett, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_sett, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_sett, screen, stats,  ship, aliens ,bullets)
            gf.update_screen(ai_sett, screen, stats, sb, ship, aliens, bullets,  play_button)




run_game()