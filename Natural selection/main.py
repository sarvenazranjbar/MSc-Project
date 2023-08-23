import pygame
from World import World
from Options import Options
from food import Food
from foodWorld import WorldFood
import random
from VirusWorld import VirusWorld
def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))

    options = Options(window)
    options.run()
    # Check the mode selected by the user and initialize the corresponding world
    if options.selected_mode == 'Spatial Elimination Selection':
        world = World(window, population_size=25)
        world.create_cells()
        while True:
            world.step()

    elif options.selected_mode == 'Food Selection':
        world = WorldFood(window, population_size=20)
        world.create_cells()

        running = True

        while running:
            world.step()
            world.draw_cells()

            world.next_button.draw(window)

            generations_text = world.font.render(f'Generations: {world.generations}', True, (255, 255, 255))
            window.blit(generations_text, (10, 10))
            # Update the display
            pygame.display.flip()
            # Handle events like closing the window and clicking the 'Next' button
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if world.next_button.is_over(pos):
                        world.eliminate_and_reproduce()
                        world.generations += 1
                        # Generate new food sources for the next cycle
                        world.foods = [Food(random.randint(0, world.width), random.randint(0, world.height)) for _
                                       in range(50)]
    elif options.selected_mode == 'Disease Selection':
        world = VirusWorld(window, population_size=60)
        world.create_cells()
        running = True
        while running:
            world.step()
            pygame.display.flip()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if world.next_button.is_over(pos):
                        world.eliminate_and_reproduce()
                        world.draw_cells()
                        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


