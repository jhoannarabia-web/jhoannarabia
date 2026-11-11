
import pygame


class FruitCatcherController:

    def __init__(self):
        self.running = True

    def handle_event(self, event, model):

        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                self.running = False

            elif event.key == pygame.K_RETURN:

                if model.state in [
                    "menu",
                    "game_over",
                    "victory"
                ]:
                    model.reset_game()

    def update(self, dt, model):

        if model.state != "playing":
            return

        keys = pygame.key.get_pressed()

        direction = 0

        if keys[pygame.K_LEFT]:
            direction = -1

        if keys[pygame.K_RIGHT]:
            direction = 1

        model.move_player(direction, dt)
