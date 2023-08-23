import random
from math import sin, cos

class Cell:
    def __init__(self, x, y, attractive, angle, size=5, has_eaten=False, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.attractive = attractive
        self.angle = angle
        self.right_steps = 0
        self.size = size
        self.color = color
        self.has_eaten = has_eaten

    def step(self, world_width, world_height):
        """
        Moves the cell one step in the direction of its angle.
        Ensures that the cell stays within the provided world dimensions.
        """
        step_x = cos(self.angle)
        step_y = sin(self.angle)
        new_x = self.x + step_x
        new_y = self.y + step_y
        if new_x < world_width and new_x >= 0:
            self.x = new_x
        if new_y < world_height and new_y >= 0:
            self.y = new_y
