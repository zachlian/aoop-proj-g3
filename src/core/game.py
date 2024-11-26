"""遊戲主類"""
import pygame
import sys
from config.settings import GameSettings, Colors
from core.grid import Grid

from core.plant_manager import PlantManager
from models.plant import PlantType
from core.card_manager import CardManager
from core.sun_manager import SunManager
from core.zombie_manager import ZombieManager

class Game:
    def __init__(self):
        pygame.init()
        self._setup_window()
        self._setup_game_objects()
        self.clock = pygame.time.Clock()
        self.is_running = True

    def _setup_window(self) -> None:
        """設置遊戲視窗"""
        self.screen = pygame.display.set_mode((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        pygame.display.set_caption(GameSettings.TITLE)

    def _setup_game_objects(self) -> None:
        """初始化遊戲物件"""
        self.grid = Grid(self.screen)
        self.plant_manager = PlantManager()
        self.card_manager = CardManager()
        self.sun_manager = SunManager()
        self.zombie_manager = ZombieManager()
        self.selected_plant_type = None

    def run(self) -> None:
        """遊戲主循環"""
        while self.is_running:
            self._handle_events()
            self._update()
            self._render()
            self._maintain_frame_rate()

    def _handle_events(self) -> None:
        """處理遊戲事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos)

    def _handle_mouse_click(self, pos: tuple[int, int]) -> None:
        """處理滑鼠點擊事件"""
        
        self.sun_manager.handle_click(pos)
        # 檢查是否點擊卡片
        plant_type = self.card_manager.handle_click(pos)
        if plant_type:
            self.selected_plant_type = plant_type
            return

        # 如果已選擇植物，嘗試放置
        if self.selected_plant_type:
            cell = self.grid.get_cell_from_pos(pos)
            if cell:
                row, col = cell
                if self.plant_manager.add_plant(row, col, self.selected_plant_type):
                    current_time = pygame.time.get_ticks()
                    self.card_manager.use_card(self.selected_plant_type, current_time)
                    self.selected_plant_type = None

    def _update(self) -> None:
        """更新遊戲狀態"""
        current_time = pygame.time.get_ticks()
        self.plant_manager.update(current_time)
        self.card_manager.update(current_time)
        self.sun_manager.update(current_time)
        self.zombie_manager.update(current_time)
        # 檢查碰撞
        self.zombie_manager.check_collisions(self.plant_manager.plants)
        
        # 檢查波次完成
        if self.zombie_manager.wave_complete:
            self.zombie_manager.start_new_wave()
            
    def _render(self) -> None:
        """渲染遊戲畫面"""
        self.screen.fill(Colors.WHITE)
        self.grid.draw()
        self.plant_manager.draw(self.screen, self.grid.start_x, self.grid.start_y)
        self.card_manager.draw(self.screen)
        self.sun_manager.draw(self.screen)
        self.zombie_manager.draw(self.screen)
        pygame.display.flip()

    def _maintain_frame_rate(self) -> None:
        """維持遊戲幀率"""
        self.clock.tick(GameSettings.FPS)

    def _quit_game(self) -> None:
        """退出遊戲"""
        self.is_running = False
        pygame.quit()
        sys.exit()