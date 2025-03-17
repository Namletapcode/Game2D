import sys
import pygame
import time
from settings import Settings
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Touhou')
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()
        self.clock  = pygame.time.Clock()
        self.player = Player(self)
        self.group = pygame.sprite.Group()
        self.FIRE_BULLET_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FIRE_BULLET_EVENT, 100)
    
    def run(self):
        while True:
            self.dt = min(self.clock.tick(self.settings.fps) / 1000, self.settings.dt_max)
            self.check_events()
            self.update_screen()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == self.FIRE_BULLET_EVENT:
                self.player.shoot()
        
    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.player.update_player()
        self.player.draw_player()
        self.group.update(self.dt)
        self.group.draw(self.screen)
        pygame.display.flip()

    
game = Game()
game.run()