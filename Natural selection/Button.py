import pygame

class Button:
    def __init__(self, x, y, width, height, color, text='', fontsize=60):
        self.color = color
        self.x = x - (width / 2)
        self.y = y - (height / 2)
        self.width = width
        self.height = height
        self.text = text
        self.fontsize = fontsize

    def draw(self, win, outline=None):
        """
        Draws the button on the provided pygame window.
        Draws an outline if a color for it is provided.
        Also renders the text on the button if any.
        """
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.fontsize)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        """
        Returns True if the given position (like mouse coordinates)
        is within the button's boundaries. Otherwise, returns False.
        """
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False