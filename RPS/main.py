"""
main.py
-------
Entry point for the Rock Paper Scissors Pygame app.
Handles the main loop, drawing, and event handling.
"""

import pygame
import sys
from game_logic import RockPaperScissorsGame
from button import Button

class RPSApp:
    """
    Main application class for the Rock Paper Scissors game.
    Handles UI and game loop.
    """
    WIDTH, HEIGHT = 500, 400
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)
    BLUE = (100, 149, 237)
    GREEN = (60, 179, 113)
    RED = (220, 20, 60)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rock Paper Scissors")
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 48)
        self.clock = pygame.time.Clock()
        self.game = RockPaperScissorsGame()
        self.buttons = self.create_buttons()

    def create_buttons(self):
        """
        Create and return a list of Button objects for each choice.
        """
        choices = RockPaperScissorsGame.CHOICES
        button_rects = [
            (50, 300, 120, 50),
            (190, 300, 120, 50),
            (330, 300, 120, 50)
        ]
        return [
            Button(button_rects[i], choices[i], self.GRAY, self.font)
            for i in range(3)
        ]

    def draw(self):
        """
        Draw the UI elements on the screen.
        """
        self.screen.fill(self.WHITE)
        # Title
        title = self.big_font.render("Rock Paper Scissors", True, self.BLUE)
        self.screen.blit(title, (self.WIDTH//2 - title.get_width()//2, 30))
        # Buttons
        for button in self.buttons:
            button.draw(self.screen)
        # Choices and result
        if self.game.player_choice:
            player_label = self.font.render(f"You: {self.game.player_choice}", True, self.GREEN)
            self.screen.blit(player_label, (50, 120))
        if self.game.computer_choice:
            comp_label = self.font.render(f"Computer: {self.game.computer_choice}", True, self.RED)
            self.screen.blit(comp_label, (50, 170))
        if self.game.result:
            result_label = self.big_font.render(self.game.result, True, self.BLACK)
            self.screen.blit(result_label, (self.WIDTH//2 - result_label.get_width()//2, 220))

    def run(self):
        """
        Main loop: handle events, update, and draw.
        """
        running = True
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, button in enumerate(self.buttons):
                        if button.is_clicked(event.pos):
                            self.game.play_round(RockPaperScissorsGame.CHOICES[i])
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    RPSApp().run()