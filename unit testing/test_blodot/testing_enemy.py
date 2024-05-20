import unittest
from unittest.mock import MagicMock
import pygame as pg
from pygame.math import Vector2
import math
import constants as c
from enemy import Enemy
from enemy_data import ENEMY_DATA

# Mock the constants module and data
c = MagicMock()
c.KILL_REWARD = 1

class TestEnemy(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.enemy_type = 'weak'
        self.waypoints = [(0, 0), (100, 0), (100, 100)]
        self.images = {self.enemy_type: pg.Surface((50, 50))}
        self.enemy = Enemy(self.enemy_type, self.waypoints, self.images)
        self.world = MagicMock()
        self.world.health = 10
        self.world.missed_enemies = 0
        self.world.killed_enemies = 0
        self.world.money = 0
        self.world.game_speed = 1

    def tearDown(self):
        pg.quit()

    def test_initialization(self):
        self.assertEqual(self.enemy.pos, Vector2(self.waypoints[0]))
        self.assertEqual(self.enemy.target_waypoint, 1)
        self.assertEqual(self.enemy.health, ENEMY_DATA[self.enemy_type]['health'])
        self.assertEqual(self.enemy.speed, ENEMY_DATA[self.enemy_type]['speed'])
        self.assertEqual(self.enemy.rect.center, self.enemy.pos)

    def test_rotation(self):
        self.enemy.move(self.world)  # Move towards the first waypoint
        self.enemy.rotate()
        expected_angle = math.degrees(math.atan2(0, 100))  # Moving right
        self.assertAlmostEqual(self.enemy.angle, expected_angle, delta=1)

    def test_reaching_waypoint(self):
        self.enemy.pos = Vector2(self.waypoints[1])  # Manually set position to the first waypoint
        self.enemy.move(self.world)
        self.assertEqual(self.enemy.target_waypoint, 2)

    def test_health_check(self):
        self.enemy.health = 0
        self.enemy.check_alive(self.world)
        self.assertFalse(self.enemy.alive())
        self.assertEqual(self.world.killed_enemies, 1)
        self.assertEqual(self.world.money, c.KILL_REWARD)

if __name__ == '__main__':
    unittest.main()
