"""陽光管理器"""
import random
import pygame
from models.sun import Sun
from typing import List

class SunManager:
    def __init__(self):
        self.suns: List[Sun] = []
        self.sun_count = 50  # 初始陽光數量
        self.last_sun_spawn = 0
        self.spawn_interval = 10000  # 每10秒自然生成一個陽光
        self._init_sun_counter()

    def _init_sun_counter(self) -> None:
        """初始化陽光計數器"""
        self.font = pygame.font.Font(None, 36)

    def update(self, current_time: int) -> None:
        """更新陽光系統"""
        # 自然生成陽光
        if current_time - self.last_sun_spawn >= self.spawn_interval:
            self._spawn_sun()
            self.last_sun_spawn = current_time

        # 更新所有陽光
        self.suns = [sun for sun in self.suns 
                    if not sun.update(current_time)]

    def _spawn_sun(self) -> None:
        """生成一個新的陽光"""
        x = random.randint(100, 700)  # 隨機x座標
        sun = Sun(x, -40, random.randint(100, 500))  # 從頂部掉落到隨機高度
        self.suns.append(sun)

    def add_sun_from_sunflower(self, x: int, y: int) -> None:
        """從向日葵生成陽光"""
        sun = Sun(x, y)
        self.suns.append(sun)

    def handle_click(self, pos: tuple[int, int]) -> None:
        """處理點擊事件"""
        for sun in self.suns:
            if sun.is_clicked(pos):
                sun.collect()
                self.sun_count += sun.value

    def spend_sun(self, amount: int) -> bool:
        """消耗陽光"""
        if self.sun_count >= amount:
            self.sun_count -= amount
            return True
        return False

    def draw(self, surface: pygame.Surface) -> None:
        """繪製陽光系統"""
        # 繪製所有陽光
        for sun in self.suns:
            sun.draw(surface)
        
        # 繪製陽光計數器
        sun_text = self.font.render(str(self.sun_count), True, (0, 0, 0))
        sun_icon = pygame.Surface((30, 30))
        sun_icon.fill((255, 255, 0))
        
        surface.blit(sun_icon, (40, 20))
        surface.blit(sun_text, (80, 25))