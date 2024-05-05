import pygame
import sys
from button import Button

pygame.init()
pygame.mixer.init()

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("asset/main_menu.png")

        self.play_button = Button(image = pygame.image.load("asset/start_tp.png"), pos = (630, 400), text_input = "",
                                  font = self.get_font(0), warna_dasar = "Navy", warna_bayangan = "White")
        self.keluar_button = Button(image=None, pos=(640, 610), text_input="KELUAR", font=self.get_font(35),
                                    warna_dasar="Navy", warna_bayangan="red")
        
    def get_font(self, size):
        return pygame.font.Font("asset/font.ttf", size)

    def display(self):
        self.musik = pygame.mixer.music.load("asset/musik_menu.mp3")
        pygame.mixer.music.play(-1)
        
        while True:
            menu_mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.background, (0, 0))
            
            self.keluar_button.berubahWarna(menu_mouse_pos)
            self.keluar_button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.check_for_input(menu_mouse_pos):
                        return "play"
                    if self.keluar_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
                        
            #self.keluar_button.update(self.screen)
            self.play_button.update(self.screen)
            
            pygame.display.update()

    def playing(self):
        pygame.mixer.music.stop()

        self.game_musik = pygame.mixer.music.load("asset/suara_game.mp3")
        pygame.mixer.music.play(-1)

        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            self.screen.fill("Cyan")

            play_text = self.get_font(50).render("Layar main", True, "Navy")
            play_rect = play_text.get_rect(center = (640, 260))

            self.screen.blit(play_text, play_rect)

            play_back = Button(image = None, pos = (640, 460), text_input = "Kembali ke Menu Utama",
                               font = self.get_font(45), warna_dasar = "navy", warna_bayangan = "red")
            play_back.berubahWarna(play_mouse_pos)
            play_back.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back.check_for_input(play_mouse_pos):
                        return "menu"
                        
            pygame.display.update()

def main():
    pygame.init()

    screen = pygame.display.set_mode((1290, 720))
    pygame.display.set_caption("Menu")
    menu_screen = MenuScreen(screen)

    while True:
        action = menu_screen.display()
        if action == "play":
            action = menu_screen.playing()
            if action == "menu":
                pygame.mixer.music.stop()
                continue
                
main()
