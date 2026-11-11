
import pygame
import math


class FruitCatcherView:

    def __init__(self):
        self.title_font = pygame.font.SysFont("arial", 42, bold=True)
        self.large_font = pygame.font.SysFont("arial", 34, bold=True)
        self.font = pygame.font.SysFont("arial", 23, bold=True)
        self.small_font = pygame.font.SysFont("arial", 17)

        self.sky = (185, 230, 255)
        self.green = (105, 190, 105)
        self.dark_green = (45, 130, 65)
        self.pink = (255, 130, 180)
        self.white = (255, 255, 255)
        self.dark = (65, 65, 85)

    def draw_text(self, screen, text, font, color, x, y):
        image = font.render(str(text), True, color)
        screen.blit(image, (x, y))

    def draw_cloud(self, screen, x, y):
        pygame.draw.circle(screen, self.white, (x, y), 25)
        pygame.draw.circle(screen, self.white, (x + 25, y - 10), 30)
        pygame.draw.circle(screen, self.white, (x + 55, y), 24)
        pygame.draw.rect(
            screen, self.white,
            (x - 5, y, 65, 25)
        )

    def draw_flower(self, screen, x, y):
        pygame.draw.line(
            screen, self.dark_green,
            (x, y), (x, y + 25), 4
        )

        for angle in range(0, 360, 72):
            px = x + int(math.cos(math.radians(angle)) * 9)
            py = y + int(math.sin(math.radians(angle)) * 9)

            pygame.draw.circle(
                screen, self.pink, (px, py), 7
            )

        pygame.draw.circle(screen, (255, 220, 70), (x, y), 6)

    def draw_background(self, screen):
        screen.fill(self.sky)

        self.draw_cloud(screen, 100, 100)
        self.draw_cloud(screen, 610, 125)
        self.draw_cloud(screen, 390, 75)

        pygame.draw.rect(
            screen, self.green,
            (0, 440, 800, 160)
        )

        pygame.draw.rect(
            screen, self.dark_green,
            (0, 470, 800, 130)
        )

        for x in range(40, 800, 100):
            self.draw_flower(screen, x, 475)

    def draw_heart(self, screen, x, y, size=15):
        pygame.draw.circle(
            screen, (255, 65, 105),
            (x - size // 2, y), size // 2
        )

        pygame.draw.circle(
            screen, (255, 65, 105),
            (x + size // 2, y), size // 2
        )

        points = [
            (x - size, y + 2),
            (x + size, y + 2),
            (x, y + size + 8)
        ]

        pygame.draw.polygon(
            screen, (255, 65, 105), points
        )

    def draw_basket(self, screen, rect):
        x, y, w, h = rect

        # Basket handle
        pygame.draw.arc(
            screen, (125, 75, 35),
            (x + 20, y - 35, w - 40, 65),
            0, math.pi, 6
        )

        # Basket body
        pygame.draw.rect(
            screen, (190, 120, 55),
            rect, border_radius=12
        )

        # Basket top
        pygame.draw.rect(
            screen, (130, 75, 35),
            (x - 5, y, w + 10, 12),
            border_radius=5
        )

        # Basket weaving
        for line_y in range(y + 18, y + h, 13):
            pygame.draw.line(
                screen, (235, 175, 95),
                (x + 5, line_y),
                (x + w - 5, line_y), 3
            )

        for line_x in range(x + 15, x + w, 20):
            pygame.draw.line(
                screen, (135, 80, 35),
                (line_x, y + 13),
                (line_x, y + h - 5), 2
            )

    def draw_fruit(self, screen, fruit):
        rect = fruit["rect"]
        kind = fruit["kind"]

        x = rect.centerx
        y = rect.centery

        if kind == "apple":
            pygame.draw.circle(
                screen, (230, 45, 65), (x, y), 16
            )
            pygame.draw.line(
                screen, (90, 55, 30),
                (x, y - 13), (x + 3, y - 22), 4
            )
            pygame.draw.ellipse(
                screen, (55, 160, 65),
                (x + 2, y - 22, 13, 7)
            )

        elif kind == "strawberry":
            points = [
                (x - 14, y - 10),
                (x + 14, y - 10),
                (x, y + 18)
            ]

            pygame.draw.polygon(
                screen, (235, 45, 90), points
            )

            pygame.draw.circle(
                screen, (235, 45, 90),
                (x, y - 8), 13
            )

            for sx, sy in [
                (-6, -3), (5, -3), (-3, 7), (5, 8)
            ]:
                pygame.draw.circle(
                    screen, (255, 230, 90),
                    (x + sx, y + sy), 2
                )

            pygame.draw.ellipse(
                screen, (50, 160, 65),
                (x - 9, y - 22, 18, 8)
            )

        elif kind == "orange":
            pygame.draw.circle(
                screen, (255, 155, 30), (x, y), 16
            )
            pygame.draw.circle(
                screen, (255, 200, 75),
                (x - 5, y - 5), 4
            )
            pygame.draw.line(
                screen, (80, 130, 45),
                (x, y - 14), (x + 3, y - 21), 3
            )

        elif kind == "rotten":
            pygame.draw.circle(
                screen, (110, 125, 55), (x, y), 16
            )
            pygame.draw.circle(
                screen, (75, 85, 35), (x + 5, y + 4), 5
            )

        elif kind == "bomb":
            pygame.draw.circle(
                screen, (45, 45, 55), (x, y), 16
            )
            pygame.draw.line(
                screen, (90, 60, 35),
                (x, y - 14), (x + 7, y - 23), 4
            )
            pygame.draw.circle(
                screen, (255, 180, 35),
                (x + 8, y - 24), 4
            )

    def draw_hud(self, screen, model):
        pygame.draw.rect(
            screen, self.white,
            (15, 15, 770, 85),
            border_radius=20
        )

        pygame.draw.rect(
            screen, (230, 220, 245),
            (15, 15, 770, 85), 3,
            border_radius=20
        )

        self.draw_text(
            screen, f"SCORE: {model.score}",
            self.font, (205, 55, 125), 35, 28
        )

        self.draw_text(
            screen, f"LEVEL: {model.level}",
            self.font, (115, 90, 210), 300, 28
        )

        self.draw_text(
            screen, "LIVES:",
            self.font, self.dark, 550, 28
        )

        for i in range(model.lives):
            self.draw_heart(screen, 645 + i * 35, 42, 15)

        # Progress bar
        pygame.draw.rect(
            screen, (225, 225, 235),
            (35, 75, 730, 12),
            border_radius=6
        )

        progress = min(model.score % 100, 100)

        if model.score >= 500:
            progress = 100

        bar_width = int(730 * progress / 100)

        pygame.draw.rect(
            screen, self.pink,
            (35, 75, bar_width, 12),
            border_radius=6
        )

    def draw_menu(self, screen):
        self.draw_background(screen)

        pygame.draw.rect(
            screen, self.white,
            (100, 150, 600, 300),
            border_radius=30
        )

        self.draw_text(
            screen, "FRUIT CATCHER",
            self.title_font, (225, 65, 135),
            190, 190
        )

        self.draw_text(
            screen, "SWEET BASKET CHALLENGE",
            self.font, (100, 110, 180),
            205, 250
        )

        self.draw_text(
            screen, "Catch fruits and earn points!",
            self.small_font, self.dark,
            265, 305
        )

        self.draw_text(
            screen, "Use LEFT and RIGHT arrow keys",
            self.small_font, self.dark,
            245, 335
        )

        self.draw_text(
            screen, "Press ENTER to START",
            self.font, (225, 65, 135),
            260, 385
        )

    def draw_game(self, screen, model):
        self.draw_background(screen)
        self.draw_hud(screen, model)

        for fruit in model.fruits:
            self.draw_fruit(screen, fruit)

        self.draw_basket(screen, model.player)

    def draw_end_screen(self, screen, model):
        self.draw_background(screen)

        pygame.draw.rect(
            screen, self.white,
            (120, 170, 560, 250),
            border_radius=30
        )

        if model.state == "victory":
            heading = "YOU WIN!"
            color = (50, 170, 90)
            message = "Congratulations!"
        else:
            heading = "GAME OVER"
            color = (225, 65, 100)
            message = "Better luck next time!"

        self.draw_text(
            screen, heading,
            self.title_font, color, 270, 205
        )

        self.draw_text(
            screen, message,
            self.font, self.dark, 275, 270
        )

        self.draw_text(
            screen, f"FINAL SCORE: {model.score}",
            self.font, (205, 75, 140), 275, 320
        )

        self.draw_text(
            screen, "Press ENTER to play again",
            self.small_font, self.dark, 275, 370
        )

    def draw(self, screen, model):
        if model.state == "menu":
            self.draw_menu(screen)

        elif model.state == "playing":
            self.draw_game(screen, model)

        elif model.state in ["game_over", "victory"]:
            self.draw_end_screen(screen, model)
