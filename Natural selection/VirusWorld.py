import random
import pygame
from Button import Button
from Cell import Cell
from Virus import Virus
class VirusWorld:
    def __init__(self, window, population_size):
            self.window = window
            self.width, self.height = window.get_size()
            self.population_size = population_size
            self.cells = []
            self.virus = Virus(random.randint(0, self.width), random.randint(0, self.height), (0, 0, 255), 10)
            self.generations = 0
            self.font = pygame.font.Font(None, 30)
            self.next_button = Button(250, 450, 200, 50, (255, 0, 0), 'Next', 20)
            self.mutation_rate = 0.05

    def create_cells(self):
        """
        Randomly creates and positions cells within the window boundaries.
        """
        for _ in range(self.population_size):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            attractive = random.choice([True, False])
            angle = random.choice([0, 3.14 / 2, 3.14, 3 * (3.14 / 2)])
            self.cells.append(Cell(x, y, attractive, angle))
            self.draw_cells()
            pygame.display.flip()

    def create_virus(self):
        """
        Randomly creates and positions a virus within the window boundaries.
        """
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        color = (0, 0, 255)
        size = 15
        self.virus = Virus(x, y, color, size)

    def draw_cells(self):
        """
        Draws the current state of the world on the window, including cells, the virus, and the generation count.
        """
        self.window.fill((0, 0, 0))
        if self.virus is not None:
            pygame.draw.circle(self.window, self.virus.color, (self.virus.x, self.virus.y), self.virus.size)
        for cell in self.cells:
            pygame.draw.circle(self.window, cell.color, (cell.x, cell.y), cell.size)
        generations_text = self.font.render(f'Generations: {self.generations}', True, (255, 255, 255))
        self.window.blit(generations_text, (10, 10))
        self.next_button.draw(self.window)

    def step(self):
        """
        Processes one step in the simulation. If it's the first generation and there's a virus, the virus spreads to cells it contacts.
        Cells also spread the virus to other cells they contact.
        """
        if self.generations == 0 and self.virus is not None:
            pygame.draw.circle(self.window, self.virus.color, (self.virus.x, self.virus.y), self.virus.size)
        for cell1 in self.cells:
            for cell2 in self.cells:
                if cell2.color == (0, 0, 255):
                    if cell1.color == (255, 0, 255): continue
                    distance = ((cell1.x - cell2.x) ** 2 + (cell1.y - cell2.y) ** 2) ** 0.5
                    if distance < cell1.size + cell2.size:
                        cell1.color = (0, 0, 255)

            if self.generations == 0 and self.virus is not None:
                distance = ((cell1.x - self.virus.x) ** 2 + (cell1.y - self.virus.y) ** 2) ** 0.5
                if distance < cell1.size + self.virus.size:
                    cell1.color = (0, 0, 255)

            cell1.step(self.width, self.height)

        self.draw_cells()

    def eliminate_and_reproduce(self):
        """
        Uninfected cells reproduce normally. Infected cells have a chance to reproduce based on a reproduction rate.
        Some of the offspring from infected cells might become immune.
        After the first generation, the virus is removed from the world.
        """
        reproduction_rate_infected = 0.5
        immunity_rate = 0.75
        new_cells = []

        for cell in self.cells:
            if cell.color != (0, 0, 255):
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                new_cell = Cell(x, y, cell.attractive, cell.angle, color=cell.color)
                new_cells.append(new_cell)
            elif random.random() < reproduction_rate_infected:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                new_cell = Cell(x, y, cell.attractive, cell.angle, color=cell.color)
                if random.random() > immunity_rate:
                    new_cell.color = (255, 0, 255)
                new_cells.append(new_cell)

        self.cells = new_cells

        if self.generations == 0:
            self.virus = None

        self.generations += 1
        self.draw_cells()