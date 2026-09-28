import pygame as pg
from random import randrange

# Setup
pg.init()

points = 0
dt = 0
size = 80
def get_dimension(prop):
  return prop[0]*size, prop[1]*size

width, height = get_dimension((10, 10))
screen = pg.display.set_mode((width, height))
pg.display.set_caption(f"Jogo da Cobrinha. Pontuação: {points}")

clock = pg.time.Clock()
running = True
eat = False

last_key = "right"

colors = {
  "green": (87,193,119),
  "red": (240,25, 55),
  "gray": (135, 120, 122)
}

class Snack:
  def __init__(self):
    self.head = [width/2, height/2]

  def up(self):
    new = self.head[1] - size * dt
    if new < 0:
      self.head[1] = height - size
    else:
      self.head[1] = new

  def down(self):
    new = self.head[1] + size * dt
    if new > height - size:
      self.head[1] = 0
    else:
      self.head[1] = new

  def left(self):
    new = self.head[0] - size * dt
    if new < 0:
      self.head[0] = width - size
    else:
      self.head[0] = new

  def right(self):
    new = self.head[0] + size * dt
    if new > width - size:
      self.head[0] = 0
    else:
      self.head[0] = new

  def draw(self):
    pg.draw.rect(screen, colors["gray"], (self.head[0], self.head[1], size, size))

snack = Snack()

class Apple:
  def __init__(self):
    self.radius = round(size/2)
    self.x = randrange(self.radius, width - self.radius, size)
    self.y = randrange(self.radius, height - self.radius, size)

  def move(self):
    self.x = randrange(self.radius, width - self.radius, size)
    self.y = randrange(self.radius, height - self.radius, size)

  def draw(self):
    pg.draw.circle(screen, colors['red'], (self.x, self.y), self.radius)

apple = Apple()

def check_eat():
  global eat, points

  equal_x = abs(snack.head[0] - apple.x) < size
  equal_y = abs(snack.head[1] - apple.y) < size

  if equal_x and equal_y:
    eat = True
    points += 1
    pg.display.set_caption(f"Jogo da Cobrinha. Pontuação: {points}")

def game():
  global last_key, eat

  if eat:
    apple.move()
    eat = False

  apple.draw()
  
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_UP:
      last_key = "up"
    elif event.key == pg.K_DOWN:
      last_key = "down"
    elif event.key == pg.K_LEFT:
      last_key = "left"
    elif event.key == pg.K_RIGHT:
      last_key = "right"

  getattr(snack, last_key)()
  snack.draw()

  check_eat()

while running:
  # Cofigurar fechaento da janela
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

  # O trabalho fica aqui
  screen.fill(colors["green"])

  game()
  
  pg.display.flip()

  # FPS
  dt = clock.tick(60) / 500

pg.quit()