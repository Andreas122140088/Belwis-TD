import unittest
import pygame as pg
from unittest.mock import Mock
import constants as c
from world import World

class TestWorld(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.map_image = pg.Surface((800, 600))
        self.level_data = {
            "layers": [
                {
                    "name": "non-turret",
                    "data": [1, 2, 3, 4]
                },
                {
                    "name": "waypoints",
                    "objects": [
                        {"polyline": [{"x": 100, "y": 200}, {"x": 300, "y": 400}]}
                    ]
                }
            ]
        }
        self.world = World(self.level_data, self.map_image)

    def tearDown(self):
        pg.quit()

    def test_initialization(self):
        self.assertEqual(self.world.level, 1)
        self.assertEqual(self.world.game_speed, 1)
        self.assertEqual(self.world.health, c.HEALTH)
        self.assertEqual(self.world.money, c.MONEY)
        self.assertEqual(self.world.tile_map, [])
        self.assertEqual(self.world.waypoints, [])
        self.assertEqual(self.world.enemy_list, [])
        self.assertEqual(self.world.spawned_enemies, 0)
        self.assertEqual(self.world.killed_enemies, 0)
        self.assertEqual(self.world.missed_enemies, 0)

    def test_process_data(self):
        self.world.process_data()
        self.assertEqual(self.world.tile_map, [1, 2, 3, 4])
        self.assertEqual(self.world.waypoints, [(100, 200), (300, 400)])

    def test_process_waypoints(self):
        waypoints_data = [{"x": 500, "y": 600}, {"x": 700, "y": 800}]
        self.world.process_waypoints(waypoints_data)
        self.assertEqual(self.world.waypoints, [(500, 600), (700, 800)])

    def test_process_enemies(self):
        ENEMY_SPAWN_DATA = {0: {"enemy_type_1": 3, "enemy_type_2": 2}}
        with unittest.mock.patch.dict('enemy_data.ENEMY_SPAWN_DATA', ENEMY_SPAWN_DATA):
            self.world.process_enemies()
            self.assertEqual(len(self.world.enemy_list), 5)
            self.assertIn("enemy_type_1", self.world.enemy_list)
            self.assertIn("enemy_type_2", self.world.enemy_list)

    def test_check_level_complete(self):
        self.world.enemy_list = ["enemy_type_1", "enemy_type_2"]
        self.world.killed_enemies = 1
        self.world.missed_enemies = 1
        self.assertTrue(self.world.check_level_complete())

    def test_reset_level(self):
        self.world.enemy_list = ["enemy_type_1", "enemy_type_2"]
        self.world.spawned_enemies = 2
        self.world.killed_enemies = 1
        self.world.missed_enemies = 1
        self.world.reset_level()
        self.assertEqual(self.world.enemy_list, [])
        self.assertEqual(self.world.spawned_enemies, 0)
        self.assertEqual(self.world.killed_enemies, 0)
        self.assertEqual(self.world.missed_enemies, 0)

    def test_draw(self):
        surface = pg.Surface((800, 600))
        self.world.draw(surface)
        self.assertTrue(pg.Surface.get_at(surface, (0, 0)) == self.map_image.get_at((0, 0)))

if __name__ == '__main__':
    unittest.main()
