class Button():
    def __init__(self,image, pos, text_input, font, warna_dasar, warna_bayangan):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.warna_dasar = warna_dasar
        self.warna_bayangan = warna_bayangan
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.warna_dasar)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)


    def check_for_input(self, posisi):
        if posisi[0] in range(self.rect.left, self.rect.right) and posisi[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def berubahWarna(self, posisi):
        if posisi[0] in range(self.rect.left, self.rect.right) and posisi[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.warna_bayangan)
        else:
            self.text = self.font.render(self.text_input, True, self.warna_dasar)
