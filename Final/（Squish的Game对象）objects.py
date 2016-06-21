import pygame. config. os
from random import randrange

"这个模块包括Squish的游戏对象

class SquishSprite(pygame.sprite.Sprite):
"""
Squish中所有子图形的范型超类。构造函数负责载入图像，
设置子图形的rect和area属性，并且允许它在指定区域内进行移动。area由屏幕的大小和留白决定。
"""

def_init_(self, image):
   pygame.sprite.Sprite._init_(self)
   self.image = pygame.image.load(image).convert()
   self.rect = self.image.get_rect()
   screen = pygame.display.get_surface()
   shrink = -config.margin * 2
   self.area = screen.get_rect().inflate(shrink, shrink)
class Weight(SquishSprite):
"""
落下的磁铁。它使用了SquishSprite构造函数设置它的磁铁图像，并且会以给定的速度作为构造函数的参数来设置下落的速度。
"""
def_init_(self, speed):
  SquishSprite._init_(self, config.weight_image)
  self.speed = speed
  self.reset()
  
def reset(self):
"""
将磁铁移动到屏幕顶端，放置到任意水平位置上。
"""
  x = randrange(self.area.left.area.right)
  self.rect.midbottom = x,0

def update(self):
"""
根据它的速度将磁铁垂直移动一段距离。并且根据它是否触及屏幕底端来设置landed属性。
"""
  self.rect.top += self.speed
  self.landed = self.rect.top >= self.area.bottom

class qinnv(SquishSprite):
"""
绝望的琴女。它使用SquishSprite构造函数设置香蕉的图像，并且会停留在屏幕底端。
它的水平位置由当前的鼠标位置（有一定限制）决定。
"""

def_init_(self):
   SquishSprite._init_(self, config.qinnv_image)
   self.rect.bottom = self.area.bottom
   #在没有琴女的部分进行填充。
   #如果磁铁移动到了这些区域，它不会
   #被判定为碰撞（或者说琴女被压扁）：
   self.pad_top = config.qinnv_pad_top
   self.pad_side = config.qinnv_pad_side
   
def update(self):
  """
  将琴女中心点的横坐标设定为当前鼠标指针的横坐标，并且使用rect的clamp方法确保qinnv停留在
  所允许的范围内。
  """
  self.rect.centerx = pygame.mouse.get_pos()[0]
  self.rect = self.rect.clamp(self.area)
  
def touches(self, other):
  """
  确定琴女是否触碰了另外的子图形（比如磁铁）。除了使用rect的colliderect方法外，首先要计算一个
  不包括琴女图像顶端和侧边“空区域”的新矩形
  """
  #使用适当的填充缩小边界：
  bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
  #移动边界，将它们放置到qinnv的底部。
  bounds.bottom = self.rect.bottom
  #检查边界是否和其他对象的rect交叉。
  return bounds.colliderect(other.rect)

   
