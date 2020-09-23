import pygame

class CardImg():
    def __init__(self, screen, pos, size, card):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.card = card

        self.image = pygame.transform.scale(pygame.image.load('img/' + self.card + '.bmp').convert(), size)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

    def blitme(self):
        self.screen.blit(self.image, self.rect)