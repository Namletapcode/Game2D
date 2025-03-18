import pygame
import math
from settings import Settings
class Bullet_enemy:
    def __init__(self, x, y, angle, speed, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.angle = angle  # Góc di chuyển
        self.speed = speed
        self.color = color
        self.radius = 5  # Kích thước đạn
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def update(self):
        """Di chuyển đạn theo hướng đã tính toán"""
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Vẽ đạn lên màn hình"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

