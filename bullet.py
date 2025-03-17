import pygame
class Bullet:
    def __init__(self, game,x,y):
      self.screen=game.screen
      self.settings=game.settings
      self.x=x
      self.y=y
      self.rect=pygame.rect.Rect(self.x,self.y,3,7)
    def update(self):
       self.y-=10
       self.rect.y=self.y
    def draw(self):
       pygame.draw.rect(self.screen,(255,255,0),self.rect)


