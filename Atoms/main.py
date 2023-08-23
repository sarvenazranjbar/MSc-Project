# Imports
import pygame
from itertools import combinations
from Components.Atom import Atom
from Components.BasicComponent import BasicComponent
from Components.Carbon import Carbon
from Components.Nitrogen import Nitrogen
from Components.Sulfur import Sulfur
from Components.Phosphorus import Phosphorus
from Components.Oxygen import Oxygen
from Components.Hydrogen import Hydrogen

window_size = 500
cells = []
particle_numbers = 3
BaseClass = BasicComponent
Atom.window_size = window_size
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Lilis world')

def draw(surface, x, y, color):
    """
    A utility function to draw the atomic particles in the visualization window.
    """
    for i in range(particle_numbers):
        pygame.draw.line(surface, color, (x, y-1), (x, y+2), abs(3))


components = [
    Carbon(),
    Nitrogen(),
    Sulfur(),
    Hydrogen(),
    Oxygen(),
    Sulfur(),
    Phosphorus()
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill(0)
    # For every pair of atomic components, apply the rule for interaction.
    for component1, component2 in combinations(components, 2):
        BaseClass.rule(component1, component2)
        BaseClass.rule(component2, component1)

    # Draw all the atomic components on the screen
    for component in components:
        for created_atom in component.group:
            draw(window, created_atom.x, created_atom.y, created_atom.colour)

    pygame.display.flip()

