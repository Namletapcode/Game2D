import pygame
import sys
from settings import Settings
from Bullet_enemy import Bullet_enemy
import math
class BulletManager:
    def __init__(self):
        self.bullets = []  # Danh sách chứa đạn
        self.spawn_time = 0  # Dùng để tính thời gian tạo đạn mới
        self.angle_offset=0
        self.settings= Settings()
    def create_ring(self, x, y, num_bullets=20, speed=3):
        """Tạo một vòng tròn đạn"""
        angle_step = 2 * math.pi / num_bullets  # Chia đều góc cho từng viên đạn
        for i in range(num_bullets):
            angle = i * angle_step
            self.bullets.append(Bullet_enemy(x, y, angle, speed))
    def create_stack(self, x, y, num_bullets=6, speed=4):
        base_angle = math.radians(self.angle_offset)
        angle_step = math.pi / num_bullets  # Chia đều các viên đạn trong nhóm

        for i in range(num_bullets):
            angle = base_angle + i * angle_step
            self.bullets.append(Bullet_enemy(x, y, angle, speed))

        self.angle_offset += 10  # Tăng góc quay để mỗi lần bắn sẽ xoay 10°
    def update(self):
        for bullet in self.bullets:
            bullet.update()
        
        self.bullets = [b for b in self.bullets if 0 <= b.x <= self.settings.screen_width and 0 <= b.y <= self.settings.screen_height]

    def draw(self, screen):
        """Vẽ tất cả đạn"""
        for bullet in self.bullets:
            bullet.draw(screen)