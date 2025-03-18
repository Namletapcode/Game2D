import pygame
import sys
from settings import Settings      # chinhr nhan vat thanh hinh tron, va cham dan reset lai luon
import time
from Enemy import BulletManager
from player import Player
class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bullet_manager = BulletManager()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Game lo")
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock() 
        self.player = Player(self)
        self.group=pygame.sprite.Group()
        self.FIRE_BULLET_EVENT=pygame.USEREVENT+1
        pygame.time.set_timer(self.FIRE_BULLET_EVENT,millis=100)
        self.enemy_x, self.enemy_y = self.settings.screen_width // 2, self.settings.screen_height // 2

    def run(self):
        while True:
            self.dt = min(self.clock.tick(self.settings.fps) / 1000, self.settings.dt_max)  #thời gian giữa 2 khung hình khi chuyển động
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Giải phóng tài nguyên và kết thúc chương trình lập tức
                sys.exit()
            if event.type == self.FIRE_BULLET_EVENT:
                self.player.shoot()
               

    def update_screen(self):
        self.screen.fill((30,30,30))#xóa mh trước khi vẽ nv mới
        self.player.update_player()
        self.player.draw_player()
        if pygame.time.get_ticks() % 50 == 0:
            self.bullet_manager.create_ring(self.enemy_x, self.enemy_y, num_bullets=24, speed=3)
            self.bullet_manager.create_stack(self.enemy_x, self.enemy_y, num_bullets=8, speed=3)
        self.bullet_manager.update()
        self.bullet_manager.draw(self.screen)
        self.group.update(self.dt)
        self.group.draw(self.screen)
        pygame.display.flip()

game = Game()
game.run()
