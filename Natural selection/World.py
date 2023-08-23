import pygame
from Cell import Cell
import random
from Button import Button

class World:
    def __init__(self, window, population_size):
        self.window = window
        self.width, self.height = window.get_size()
        self.population_size = population_size
        self.cells = []
        self.generations = 0
        self.font = pygame.font.Font(None, 30)
        self.next_button = Button(250, 450, 200, 50, (255, 0, 0), 'Next', 20)
        self.mutation_rate = 0.0001

    def create_cells(self):
        # Initialize the world with a set of cells with random positions and properties.
        for _ in range(self.population_size):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            attractive = random.choice([True, False])
            angle = random.choice([0, 3.14/2, 3.14, 3*(3.14/2)])
            self.cells.append(Cell(x, y, attractive, angle))
            self.draw_cells()
            pygame.display.flip()

    def step(self):
        """
        Responsible for the main simulation loop. Handles user input, checks for interaction with the "Next" button,
        and updates the cell's position and rendering.
        """
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_button.is_over(pos):
                    self.eliminate_and_reproduce()
                    self.generations += 1

            if event.type == pygame.MOUSEMOTION:
                if self.next_button.is_over(pos):
                    self.next_button.color = (255, 0, 0)
                else:
                    self.next_button.color = (0, 255, 0)

        for cell in self.cells:
            cell.step(self.width, self.height)

        self.window.fill((0, 0, 0))
        self.draw_cells()
        pygame.display.flip()

    def draw_cells(self):
        # Draw cells, generation count, and the 'Next' button
        self.window.fill((0, 0, 0))
        for cell in self.cells:
            pygame.draw.circle(self.window, cell.color, (cell.x, cell.y), cell.size)

        # Display generation count
        generations_text = f'Generations: {self.generations}'
        generations_surface = self.font.render(generations_text, False, (255, 255, 255))
        self.window.blit(generations_surface, (10, 10))

        self.next_button.draw(self.window)

    def eliminate_and_reproduce(self):
        """
        Performs natural selection and reproduction. Only keeps cells to the left of the window's midpoint.
        Creates new cells via crossover and mutation.
        """
        self.cells = [cell for cell in self.cells if cell.x <= self.width / 2]
        new_cells = []
        for _ in range(1):
            for i in range(len(self.cells) - 1):
                new_cell = self.crossover(self.cells[i], self.cells[i+1])
                self.mutation(new_cell)
                new_cells.append(new_cell)
        self.cells = new_cells
        self.draw_cells()
        pygame.display.flip()

    def crossover(self, cell1, cell2):
        # Average position of the two cells
        new_x = (cell1.x + cell2.x) / 2
        new_y = (cell1.y + cell2.y) / 2
        new_att = random.choice([cell1.attractive, cell2.attractive])
        # Randomly choose if the new cell will be an average or just adopt a parent's property
        if random.choice([True, False]):
            new_col = (255, 0, 0)
            new_dir = (cell1.angle + cell2.angle) / 2
        else:
            chosen_cell = random.choice([cell1, cell2])
            new_dir = chosen_cell.angle
            new_col = chosen_cell.color
        return Cell(new_x, new_y, new_att, new_dir, color=new_col)

    def mutation(self, cell):
        if random.random() < self.mutation_rate:
            cell.x = self.get_random_position(True)
            cell.y = self.get_random_position(False)
            cell.color = (0, 255, 0)
            # A random direction preference
            cell.direction_preference = random.random() * (2 * 3.14)

    def get_random_position(self, is_x):
        # Get a random position within the world's dimensions
        lower_x, lower_y = 0, 0
        upper_x, upper_y = self.width, self.height
        if is_x:
            return random.randint(lower_x, upper_x)
        return random.randint(lower_y, upper_y)