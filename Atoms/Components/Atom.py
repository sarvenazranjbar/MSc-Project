import random


class Atom:
    window_size = 0
    def __init__(self, colour: str):
        self.colour = colour
        self.x = Atom.randomxy()
        self.y = Atom.randomxy()
        self.vx = Atom.randomxy()
        self.vy = Atom.randomxy()

    @staticmethod
    def randomxy():
        return round(random.random() * Atom.window_size + 1) # Returns a random number between 1 and window_size