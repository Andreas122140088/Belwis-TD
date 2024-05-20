import unittest
import pygame as pg
from turret_child import Turret
from enemy import Enemy
from unittest.mock import Mock

class TestTurret(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.turret_image = pg.Surface((50, 50))
        self.turret_image.fill((0, 255, 0))
        self.bullet_image = pg.Surface((10, 10))
        self.bullet_image.fill((255, 0, 0))
        self.turret = Turret(400, 300, self.turret_image, self.bullet_image)

        # Create a mock enemy
        self.enemy = Mock()
        self.enemy.pos = Vector2(500, 300)

    def tearDown(self):
        pg.quit()

    def test_turret_initialization(self):
        self.assertEqual(self.turret.rect.center, (400, 300))
        self.assertEqual(self.turret.angle, 0)
        self.assertIsNone(self.turret.target)

    def test_turret_rotate_with_target(self):
        self.turret.target = self.enemy
        self.turret.rotate([])
        self.assertNotEqual(self.turret.angle, 0)

    def test_turret_find_target(self):
        enemies = [self.enemy]
        self.turret.find_target(enemies)
        self.assertEqual(self.turret.target, self.enemy)

    def test_turret_shoot(self):
        self.turret.target = self.enemy
        self.assertTrue(self.turret.shoot())

    def test_turret_no_target_no_shoot(self):
        self.turret.target = None
        self.assertFalse(self.turret.shoot())

if __name__ == '__main__':
    unittest.main()
