"""植物管理器"""
from typing import Dict, Tuple
import pygame
from models.plant import Plant, Sunflower, Peashooter, PlantType

class PlantManager:
    def __init__(self):
        self.plants: Dict[Tuple[int, int], Plant] = {}

    def add_plant(self, row: int, col: int, plant_type: PlantType) -> bool:
        """添加植物"""
        if self.can_place_plant(row, col):
            if plant_type == PlantType.SUNFLOWER:
                plant = Sunflower(row, col)
            elif plant_type == PlantType.PEASHOOTER:
                plant = Peashooter(row, col)
            else:
                return False

            self.plants[(row, col)] = plant
            return True
        return False

    def can_place_plant(self, row: int, col: int) -> bool:
        """檢查是否可以放置植物"""
        return (row, col) not in self.plants

    def update(self, current_time: int) -> None:
        """更新所有植物"""
        for plant in self.plants.values():
            plant.update(current_time)

    def draw(self, surface: pygame.Surface, grid_start_x: int, grid_start_y: int) -> None:
        """繪製所有植物"""
        for plant in self.plants.values():
            plant.draw(surface, grid_start_x, grid_start_y)