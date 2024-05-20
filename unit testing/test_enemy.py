import unittest
import pygame as pg
from pygame.math import Vector2
from enemy import Enemy
from unittest.mock import Mock

class TestEnemy(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.waypoints = [(0, 0), (100, 0), (100, 100)]
        self.images = {"enemy_type_1": pg.Surface((50, 50))}
        self.images["enemy_type_1"].fill((255, 0, 0))

        self.enemy_data_mock = {
            "enemy_type_1": {
                "health": 100,
                "speed": 1.0
            }
        }

        self.enemy = Enemy("enemy_type_1", self.waypoints, self.images)
        self.world_mock = Mock()
        self.world_mock.health = 10
        self.world_mock.missed_enemies = 0
        self.world_mock.killed_enemies = 0
        self.world_mock.money = 0
        self.world_mock.game_speed = 1.0

    def tearDown(self):
        pg.quit()

    def test_enemy_initialization(self):
        self.assertEqual(self.enemy.pos, Vector2(self.waypoints[0]))
        self.assertEqual(self.enemy.target_waypoint, 1)
        self.assertEqual(self.enemy.health, self.enemy_data_mock["enemy_type_1"]["health"])
        self.assertEqual(self.enemy.speed, self.enemy_data_mock["enemy_type_1"]["speed"])

    def test_enemy_move(self):
        initial_pos = self.enemy.pos.copy()
        self.enemy.move(self.world_mock)
        self.assertNotEqual(self.enemy.pos, initial_pos)

    def test_enemy_reaches_waypoint(self):
        self.enemy.pos = Vector2(100, 0)
        self.enemy.move(self.world_mock)
        self.assertEqual(self.enemy.target_waypoint, 2)

    def test_enemy_reaches_end_of_path(self):
        self.enemy.pos = Vector2(100, 100)
        self.enemy.target_waypoint = 3
        self.enemy.move(self.world_mock)
        self.assertTrue(self.enemy not in self.world_mock.health)
        self.assertEqual(self.world_mock.health, 9)
        self.assertEqual(self.world_mock.missed_enemies, 1)

    def test_enemy_rotation(self):
        self.enemy.rotate()
        self.assertEqual(self.enemy.angle, 0)

    def test_enemy_check_alive(self):
        self.enemy.health = 0
        self.enemy.check_alive(self.world_mock)
        self.assertEqual(self.world_mock.killed_enemies, 1)
        self.assertEqual(self.world_mock.money, c.KILL_REWARD)

if __name__ == '__main__':
    unittest.main()
