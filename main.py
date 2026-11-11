
import pygame

from model import FruitCatcherModel
from view import FruitCatcherView
from controller import FruitCatcherController


def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption(
        "Fruit Catcher: Sweet Basket Challenge"
    )

    clock = pygame.time.Clock()

    model = FruitCatcherModel()
    view = FruitCatcherView()
    controller = FruitCatcherController()

    while controller.running:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            controller.handle_event(event, model)

        controller.update(dt, model)

        model.update(dt)

        view.draw(screen, model)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
