import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def game_run():
  # инициализирует pygame, settings и объекты экрана 
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
  pygame.display.set_caption('Alien Invasion')
  # создание коробля
  ship = Ship(ai_settings, screen)
  # Создание группы для хранения пуль
  bullets = Group()
  # Создание пришельца.
  aliens = Group()

  # Создание флота пришельцев.
  gf.create_fleet(ai_settings, screen, ship, aliens)
  # запуск основного цикла
  while True:
      gf.check_events(ai_settings, screen, ship, bullets)
      ship.update()
      gf.bullets_update(bullets)
      gf.update_aliens(ai_settings, aliens)
      # удаление пуль вышедших за край.
      

      gf.update_screen(ai_settings, screen, ship, aliens, bullets)




game_run()