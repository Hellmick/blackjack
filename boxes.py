import pygame

class Box:
    def __init__(self, screen, settings, color, pos, size, enabled=True, text=''):
        self.screen = screen
        self.size = size
        self.pos = pos
        self.text = text
        self.enabled = enabled
        self.color = color
        self.settings = settings

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.txt_surface = settings.font.render(text, True, pygame.Color(0, 0, 0,))

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    def update_text(self, text):
        self.text = text
        self.txt_surface = self.settings.font.render(text, True, pygame.Color(0, 0, 0,))
        self.blitme()

class Button(Box):
    def __init__(self, screen, settings, pos, size=(100, 30), text=''):
        Box.__init__(self, screen=screen, settings=settings, enabled=False, color=settings.color_inact, pos=pos, size=size, text=text)

        self.color_act = settings.color_active
        self.color_inact = settings.color_inact

        self.active = False

    def handle_event(self, event):
        return self.enabled and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
        
class InputBox(Box):

    def __init__(self, screen, settings, pos, size, text=''):
        Box.__init__(self, screen=screen, settings=settings, color=settings.color_inact, pos=pos, size=size, enabled=True)

        self.color_act = settings.color_active
        self.color_inact = settings.color_inact

        self.active = False

    def handle_event(self, event, font):
        if self.enabled:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #check if the user clicked on the box
                if self.rect.collidepoint(event.pos):
                    #if yes, toggle the active var
                    self.active = not self.active
                else:
                    #turn off the box when the user clicks outside the box
                    self.active = False
                self.color = self.color_act if self.active else self.color_inact
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if event.unicode.isnumeric() and len(self.text) <= 8:
                            self.text += event.unicode

                    self.txt_surface = font.render(self.text, True, pygame.Color(0, 0, 0,))