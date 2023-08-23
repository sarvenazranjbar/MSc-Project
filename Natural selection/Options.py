import pygame

from Button import Button



class Options:
    def __init__(self, window):
        self.window = window
        self.width, self.height = window.get_size()
        self.font = pygame.font.Font(None, 30)
        self.option_buttons = [
            Button(250, 150, 200, 50, (255, 255, 255), 'Spatial Elimination Selection', 12),
            Button(250, 250, 200, 50, (255, 255, 255), 'Food Selection', 12),
            Button(250, 350, 200, 50, (255, 255, 255), 'Disease Selection', 12)
        ]
        self.selected_mode = None

    def draw(self):
        """
        Renders the buttons for each option on the screen.
        """
        self.window.fill((0, 0, 0))
        for button in self.option_buttons:
            button.draw(self.window)
        pygame.display.flip()

    def run(self):
        """
        Continuously checks for button clicks until a selection mode is chosen.
        """
        while self.selected_mode is None:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.option_buttons:
                        if button.is_over(pos):
                            self.selected_mode = button.text
            self.draw()
