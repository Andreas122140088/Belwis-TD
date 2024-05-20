import unittest
import pygame as pg
from pygame.math import Vector2
from unittest.mock import Mock
import constants as c
from turret import Turret

class TestTurret(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.sprite_sheets = [pg.Surface((100, 100))]
        self.sprite_sheets[0].fill((0, 255, 0))
        self.shot_fx = Mock()
        self.turret = Turret(self.sprite_sheets, 5, 5, self.shot_fx, cooldown=1000, range=200)
        
        # Create a mock enemy
        self.enemy = Mock()
        self.enemy.pos = Vector2(300, 300)
        self.enemy.health = 100

        # Create a mock world
        self.world = Mock()
        self.world.game_speed = 1.0

    def tearDown(self):
        pg.quit()

    def test_turret_initialization(self):
        self.assertEqual(self.turret.cooldown, 1000)
        self.assertEqual(self.turret.range, 200)
        self.assertEqual(self.turret.tile_x, 5)
        self.assertEqual(self.turret.tile_y, 5)
        self.assertFalse(self.turret.selected)

    def test_upgrade(self):
        self.turret.upgrade(cooldown=500, range=300)
        self.assertEqual(self.turret.cooldown, 500)
        self.assertEqual(self.turret.range, 300)

    def test_load_images(self):
        images = self.turret.load_images(self.sprite_sheets[0])
        self.assertEqual(len(images), c.ANIMATION_STEPS)

    def test_pick_target(self):
        enemy_group = [self.enemy]
        self.turret.pick_target(enemy_group)
        self.assertEqual(self.turret.target, self.enemy)
        self.assertEqual(self.enemy.health, 100 - c.DAMAGE)
        self.shot_fx.play.assert_called_once()

    def test_no_target_out_of_range(self):
        enemy_group = [self.enemy]
        self.enemy.pos = Vector2(1000, 1000)
        self.turret.pick_target(enemy_group)
        self.assertIsNone(self.turret.target)
        self.shot_fx.play.assert_not_called()

    def test_play_animation(self):
        self.turret.target = self.enemy
        self.turret.play_animation()
        self.assertEqual(self.turret.frame_index, 1)

    def test_play_animation_reset(self):
        self.turret.target = self.enemy
        self.turret.frame_index = len(self.turret.animation_list) - 1
        self.turret.play_animation()
        self.assertEqual(self.turret.frame_index, 0)
        self.assertIsNone(self.turret.target)

if __name__ == '__main__':
    unittest.main()
