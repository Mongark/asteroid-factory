import pygame
import pygame_menu

class AsteroidFactory:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        self.is_running = True

        self.menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', self.run())
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def run(self):
        while self.is_running:
            self.screen.fill((255, 255, 255))

            self.render()
            self.update()

            pygame.display.flip()

    def render(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                quit()

    def menu_run(self):
        self.menu.mainloop(self.screen)

AsteroidFactory().run()
