import unittest
import pygame as pg
from button import Button

class TestButton(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.image = pg.Surface((100, 50))  # Dummy image for button
        self.image.fill((255, 0, 0))
        self.button = Button(100, 100, self.image, single_click=True)

    def tearDown(self):
        pg.quit()

    def test_button_initialization(self):
        self.assertEqual(self.button.rect.topleft, (100, 100))
        self.assertFalse(self.button.clicked)
        self.assertTrue(self.button.single_click)

    def test_button_draw_no_click(self):
        pg.mouse.set_pos((150, 125))
        pg.event.clear()
        self.assertFalse(self.button.draw(self.screen))

    def test_button_draw_single_click(self):
        pg.mouse.set_pos((150, 125))
        pg.mouse.get_pressed = lambda: (1, 0, 0)
        pg.event.clear()
        self.assertTrue(self.button.draw(self.screen))
        self.assertTrue(self.button.clicked)

    def test_button_draw_click_release(self):
        pg.mouse.set_pos((150, 125))
        pg.mouse.get_pressed = lambda: (1, 0, 0)
        pg.event.clear()
        self.button.draw(self.screen)  # Click
        pg.mouse.get_pressed = lambda: (0, 0, 0)
        self.button.draw(self.screen)  # Release
        self.assertFalse(self.button.clicked)

if __name__ == '__main__':
    unittest.main()
