
import pygame
import random


class FruitCatcherModel:

    def __init__(self):
        self.width = 800
        self.height = 600
        self.state = "menu"
        self.reset_game()
        self.state = "menu"

    def reset_game(self):

        self.player = pygame.Rect(340, 500, 120, 55)

        self.fruits = []

        self.score = 0
        self.lives = 3

        self.level = 1
        self.max_level = 5
        self.target_score = 100

        self.spawn_timer = 0
        self.spawn_interval = 1.7

        self.state = "playing"

    def move_player(self, direction, dt):

        speed = 400
        self.player.x += direction * speed * dt

        if self.player.left < 0:
            self.player.left = 0

        if self.player.right > self.width:
            self.player.right = self.width

    def update_level(self):

        self.level = min(
            self.score // 100 + 1,
            self.max_level
        )

        self.target_score = self.level * 100

        self.spawn_interval = max(
            0.65,
            1.7 - (self.level - 1) * 0.2
        )

    def spawn_fruit(self):

        items = [
            ("apple", 10),
            ("apple", 10),
            ("strawberry", 15),
            ("orange", 5),
            ("rotten", -10),
            ("bomb", 0)
        ]

        kind, points = random.choice(items)

        speed_bonus = (self.level - 1) * 25

        item = {
            "rect": pygame.Rect(
                random.randint(25, self.width - 55),
                -40,
                30,
                30
            ),
            "kind": kind,
            "points": points,
            "speed": random.randint(150, 200) + speed_bonus
        }

        self.fruits.append(item)

    def update(self, dt):

        if self.state != "playing":
            return

        self.update_level()

        self.spawn_timer += dt

        if (
            self.spawn_timer >= self.spawn_interval
            and len(self.fruits) < 2
        ):
            self.spawn_fruit()
            self.spawn_timer = 0

        for fruit in self.fruits[:]:

            fruit["rect"].y += int(
                fruit["speed"] * dt
            )

            # Caught an item
            if fruit["rect"].colliderect(self.player):

                # Caught bomb = GAME OVER
                if fruit["kind"] == "bomb":
                    self.fruits.remove(fruit)
                    self.state = "game_over"
                    return

                # Caught fruit = add points
                self.score += fruit["points"]
                self.score = max(0, self.score)

                self.fruits.remove(fruit)

            # Item missed
            elif fruit["rect"].top > self.height:

                # Only missed fruits reduce lives
                if fruit["kind"] != "bomb":
                    self.lives -= 1

                self.fruits.remove(fruit)

            self.update_level()

            if self.lives <= 0:
                self.state = "game_over"
                return

            if self.score >= 500:
                self.score = 500
                self.state = "victory"
                return
