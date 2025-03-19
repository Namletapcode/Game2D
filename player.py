import pygame
from settings import Settings
from bullet import Bullet
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__() #kế thừa lớp con từ lớp cha
        self.settings=Settings()
        self.screen=game.screen
        self.screen_rect=game.screen_rect
        #self.rect=pygame.Rect(self.settings.screen_width//2,self.settings.screen_height-40,30,30)
        self.direction=pygame.Vector2(0,0)
        self.bullets=[]
        self.radius=5
        self.x=self.settings.screen_width//2
        self.y=self.settings.screen_height-40
    def draw_player(self):
        pygame.draw.circle(self.screen,(255,0,0),(self.x,self.y),self.radius)
    def update_player(self):
        self.input()
        self.move()
        for bullet in self.bullets:
           bullet.update()
           bullet.draw()
           if bullet.y <0:
               self.bullets.remove(bullet)
              
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else: self.direction.x=0 
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else: self.direction.y=0
      
    def move(self):
         if self.direction.x and self.direction.y:
             self.direction.normalize()
         self.x+=self.direction.x * self.settings.player_speed
         self.y+=self.direction.y * self.settings.player_speed
    def handle_screen_collision(self):
        """Ngăn hình tròn đi ra ngoài màn hình"""
        if self.x - self.radius < 0:
            self.x = self.radius  # Giữ trong giới hạn trái
        if self.x + self.radius > self.settings.screen_width:
            self.x = self.settings.screen_width - self.radius  # Giữ trong giới hạn phải
        if self.y - self.radius < 0:
            self.y = self.radius  # Giữ trong giới hạn trên
        if self.y + self.radius > self.settings.screen_height:
            self.y = self.settings.screen_height - self.radius
   
        