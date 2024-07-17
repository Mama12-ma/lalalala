import pygame

class Ship():

  def __init__(self, ai_settings, screen):
    """инициализирует корабль и задает его изначальную позицию"""
    self.screen = screen
    self.ai_settings = ai_settings

    # Загрузка изоброжения коробля и получение прямоугольника.
    self.image = pygame.image.load('images\ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    # каждый новый корабль появляется в нижнем крае экрана
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    # Сохранение вещественной координаты коробля.
    self.center = float(self.rect.centerx)
    self.ai_settings.ship_speed = 1

    self.moving_right = False
    self.moving_left = False

  def update(self):
    """Обновляет позицию коробля с учетом флага."""
    # Обновление атребута center, не rect
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed
    if self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed
      # Обновление атрибута rect на основании self.center.
    self.rect.centerx = self.center
    


  def blitme(self):
    """рисует корабль в текущей позиции."""
    self.screen.blit(self.image, self.rect)