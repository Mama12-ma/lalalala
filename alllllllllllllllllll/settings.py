class Settings():
  # класс для хранения всех настроек Alien Invasion
  def __init__(self):
    """инициализирует все настройки игры"""
    self.alien_speed_factor = 1
    self.fleet_drop_speed = 10
    self.fleet_direction = 1

    self.screen_width = 1200
    self.screen_heigth = 800
    self.bg_color = (250, 250, 250)
    # настройки пули
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 13
    self.bullet_color = 60, 60, 60
    self.bullets_allowed = 100