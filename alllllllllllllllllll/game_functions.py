import pygame
import sys
from bullet import Bullet
from alien import Alien




def get_number_aliens_x(ai_settings, alien_width):
  available_space_x = ai_settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
      # Создание пришельца и размещение его в ряду.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
  """создание флот пришельцев"""
  alien = Alien(ai_settings, screen)

  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
  number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

  for row_number in range(number_rows):
    for alien_number in range(number_aliens_x):
      create_alien(ai_settings, screen, aliens, alien_number, row_number)


  
def get_number_rows(ai_settings, ship_hieght, alien_height):
  """Определяет количество рядов помещающихся на экране"""
  available_space_y = (ai_settings.screen_heigth - (3 * alien_height) - ship_hieght)
  number_rows = int(available_space_y / (2 * alien_height)) 
  return number_rows


def check_fleet_edges(ai_settings, aliens):
  """Реагирует на достижение пришельцем края экрана."""
  for alien in aliens.sprites():
    if alien.check_edges():
      check_fleet_edges(ai_settings, aliens)
      break

def check_fleet_directions(ai_settings, aliens):
  """Опускает весь флот и меняет направление флота."""
  for alien in aliens.sprites():
    alien.rect.y += ai_settings.fleet_drop_speed
  ai_settings.fleet_direction *= -1



def chek_keydown_events(event, ai_settings, screen, ship, bullets):
  if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
    ship.moving_right = True
  elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
    ship.moving_left = True
  elif (event.key == pygame.K_w) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
    fire_bullets(ai_settings, screen, ship, bullets)
  elif event.key == pygame.K_q:
    sys.exit()

def fire_bullets(ai_settings, screen, ship, bullets):  
  if len(bullets) < ai_settings.bullets_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
  

def chek_keyup_events(event, ship):
  if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
    ship.moving_right = False
  elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
    ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
  """Обробатываем нажатие клавиш и событие мыши"""
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        chek_keydown_events(event, ai_settings, screen, ship, bullets)
      elif event.type == pygame.KEYUP:
        chek_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
  """Обновляет изоброжение на экране и отоброжает новый экран"""
  screen.fill(ai_settings.bg_color)

  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  aliens.draw(screen)

  pygame.display.flip()

def update_aliens(ai_settings, aliens):
  """
  Проверяет достиг ли флот края экрана,
  после чего обновляет позицию пришельцев.
  """
  check_fleet_edges(ai_settings, aliens)
  aliens.update()

def bullets_update(bullets):
  """Обновление позиции пуль и удаление старых."""
  # обновление позиции
  bullets.update()
  # удаление старых пуль.
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)


  # отоброжение последнего прорисовонного экрана
