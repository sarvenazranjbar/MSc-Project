import random
import pygame
from Cell import Cell
from food import Food
from Button import Button

class WorldFood:
    def __init__(self, window, population_size):
        self.window = window
        self.width, self.height = window.get_size()
        self.population_size = population_size
        self.cells = []
        self.foods = [Food(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(50)]
        self.generations = 0
        self.font = pygame.font.Font(None, 30)
        self.next_button = Button(250, 450, 200, 50, (255, 0, 0), 'Next', 20)
        self.mutation_rate = 0.05

    def create_cells(self):
        """
        Creates cells at random positions with random attributes within the world.
        """
        for _ in range(self.population_size):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            attractive = random.choice([True, False])
            angle = random.choice([0, 3.14/2, 3.14, 3*(3.14/2)])
            self.cells.append(Cell(x, y, attractive, angle))
            self.draw_cells()
            pygame.display.flip()

    def draw_cells(self):
        """
        Draws the food and cells on the screen and displays the current generation count.
        """
        self.window.fill((0, 0, 0))
        for food in self.foods:
            pygame.draw.circle(self.window, food.color, (food.x, food.y), food.size)
        for cell in self.cells:
            pygame.draw.circle(self.window, cell.color, (cell.x, cell.y), cell.size)
        generations_text = self.font.render(f'Generations: {self.generations}', True, (255, 255, 255))
        self.window.blit(generations_text, (10, 10))

    def step(self):
        """
        Moves cells, allows cells to consume food, and updates the display for each frame.
        """
        for cell in self.cells:
            for food in self.foods:
                if abs(cell.x - food.x) < cell.size and abs(cell.y - food.y) < cell.size:
                    self.foods.remove(food)
                    cell.has_eaten = True
            cell.step(self.width, self.height)

        self.draw_cells()
        self.next_button.draw(self.window)
        generations_text = self.font.render(f'Generations: {self.generations}', True, (255, 255, 255))
        self.window.blit(generations_text, (10, 10))

    def eliminate_and_reproduce(self):
        """
        Retains cells that have eaten, creates new cells through crossover, introduces mutations,
        and resets the food sources in the world.
        """
        surviving_cells = [cell for cell in self.cells if cell.has_eaten]
        new_cells = []
        for i in range(len(surviving_cells) - 1):
            new_cell = self.crossover(surviving_cells[i], surviving_cells[i+1])
            self.mutation(new_cell)
            new_cells.append(new_cell)
        self.foods = [Food(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(50)]
        self.cells = new_cells
        self.draw_cells()
        pygame.display.flip()

    def crossover(self, cell1, cell2):
        """
        Generates a new cell by blending attributes from two parent cells.
        """
        new_x = (cell1.x + cell2.x) / 2
        new_y = (cell1.y + cell2.y) / 2
        new_att = random.choice([cell1.attractive, cell2.attractive])
        if random.choice([True, False]):
            new_col = (255, 0, 0)
            new_dir = (cell1.angle + cell2.angle) / 2
        else:
            chosen_cell = random.choice([cell1, cell2])
            new_dir = chosen_cell.angle
            new_col = chosen_cell.color
        return Cell(new_x, new_y, new_att, new_dir, color=new_col)

    def mutation(self, cell):
        """
        Introduces random changes to a cell's attributes based on a predetermined mutation rate.
        """
        if random.random() < self.mutation_rate:
            cell.x = self.get_random_position(True)
            cell.y = self.get_random_position(False)
            cell.color = (0, 255, 0)
            cell.direction_preference = random.random() * (2 * 3.14)

    def get_random_position(self, is_x):
        """
        Returns a random position (either x or y) within the boundaries of the world's dimensions.
        """
        lower_x, lower_y = 0, 0
        upper_x, upper_y = self.width, self.height
        if is_x:
            return random.randint(lower_x, upper_x)
        return random.randint(lower_y, upper_y)