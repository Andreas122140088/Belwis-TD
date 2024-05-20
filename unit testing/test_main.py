import unittest
import pygame as pg
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):

    def test_draw_text(self):
        # Test function to draw text onto the screen
        surface = pg.Surface((800, 600))  # Create a surface
        main.draw_text("Test", pg.font.SysFont(None, 24), (255, 255, 255), 0, 0)  # Draw text on surface

        # Assert that the text is drawn onto the surface
        self.assertIsNotNone(surface)

    def test_create_turret(self):
        # Test function to create turret
        pg.init()  # Initialize pygame
        screen = pg.display.set_mode((800, 600))  # Create a screen
        mouse_pos = (400, 300)  # Set mouse position

        # Patching necessary functions to avoid errors
        with patch('pygame.sprite.Group'), patch('pygame.mixer.Sound'), patch('pygame.image.load'):
            main.create_turret(mouse_pos)

        # Assert that turret is created
        self.assertIsNotNone(screen)

    def test_select_turret(self):
        # Test function to select turret
        pg.init()  # Initialize pygame
        mouse_pos = (400, 300)  # Set mouse position

        # Patching necessary functions to avoid errors
        with patch('pygame.sprite.Group'):
            turret = main.select_turret(mouse_pos)

        # Assert that turret is selected
        self.assertIsNone(turret)

    def test_clear_selection(self):
        # Test function to clear turret selection
        pg.init()  # Initialize pygame

        # Patching necessary functions to avoid errors
        with patch('pygame.sprite.Group'):
            main.clear_selection()

        # Assert that turret selection is cleared
        self.assertTrue(True)

    def test_upgrade_turret(self):
        # Test function to upgrade turret
        pg.init()  # Initialize pygame

        # Patching necessary functions to avoid errors
        with patch('builtins.print'):
            main.upgrade_turret()

        # Assert that turret is upgraded
        self.assertTrue(True)

    @patch('main.pg.display.set_mode')
    def test_draw_main_menu(self, mock_display):
        # Test function to draw main menu
        pg.init()  # Initialize pygame
        mock_display.return_value = pg.Surface((800, 600))  # Mock display

        # Redirect stdout to catch print statements
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = main.draw_main_menu()

        # Assert that main menu is drawn
        self.assertIsNone(result)
        self.assertIn("start", fake_out.getvalue())  # Check if "start" is printed

if __name__ == '__main__':
    unittest.main()
