import unittest

# Importing the data
from enemy_data import ENEMY_SPAWN_DATA, ENEMY_DATA

class TestEnemyData(unittest.TestCase):
    def test_enemy_spawn_data_structure(self):
        # Ensure ENEMY_SPAWN_DATA is a list of dictionaries
        self.assertIsInstance(ENEMY_SPAWN_DATA, list)
        for wave in ENEMY_SPAWN_DATA:
            self.assertIsInstance(wave, dict)
            self.assertIn("weak", wave)
            self.assertIn("medium", wave)
            self.assertIn("strong", wave)
            self.assertIn("elite", wave)
            self.assertIsInstance(wave["weak"], int)
            self.assertIsInstance(wave["medium"], int)
            self.assertIsInstance(wave["strong"], int)
            self.assertIsInstance(wave["elite"], int)
    
    def test_specific_wave_data(self):
        # Check specific wave data
        self.assertEqual(ENEMY_SPAWN_DATA[0]["weak"], 15)
        self.assertEqual(ENEMY_SPAWN_DATA[0]["medium"], 0)
        self.assertEqual(ENEMY_SPAWN_DATA[0]["strong"], 0)
        self.assertEqual(ENEMY_SPAWN_DATA[0]["elite"], 0)
        
        self.assertEqual(ENEMY_SPAWN_DATA[14]["weak"], 25)
        self.assertEqual(ENEMY_SPAWN_DATA[14]["medium"], 25)
        self.assertEqual(ENEMY_SPAWN_DATA[14]["strong"], 25)
        self.assertEqual(ENEMY_SPAWN_DATA[14]["elite"], 25)

    def test_enemy_data_structure(self):
        # Ensure ENEMY_DATA is a dictionary of dictionaries
        self.assertIsInstance(ENEMY_DATA, dict)
        for enemy_type, attributes in ENEMY_DATA.items():
            self.assertIn(enemy_type, ["weak", "medium", "strong", "elite"])
            self.assertIsInstance(attributes, dict)
            self.assertIn("health", attributes)
            self.assertIn("speed", attributes)
            self.assertIsInstance(attributes["health"], int)
            self.assertIsInstance(attributes["speed"], int)

    def test_specific_enemy_data(self):
        # Check specific enemy data
        self.assertEqual(ENEMY_DATA["weak"]["health"], 10)
        self.assertEqual(ENEMY_DATA["weak"]["speed"], 2)
        
        self.assertEqual(ENEMY_DATA["elite"]["health"], 30)
        self.assertEqual(ENEMY_DATA["elite"]["speed"], 6)

if __name__ == '__main__':
    unittest.main()
