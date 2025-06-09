"""
button.py
----------
Defines a reusable Button class for Pygame GUIs.
"""

import pygame

class Button:
    """
    Represents a clickable button in a Pygame window.
    """
    def __init__(self, rect, text, color, font, text_color=(0,0,0)):
        """
        Initialize the button.

        rect: tuple (x, y, width, height)
        text: string to display on the button
        color: background color (RGB tuple)
        font: pygame.font.Font object
        text_color: color of the text (default black)
        """
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.font = font
        self.text_color = text_color

    def draw(self, surface):
        """
        Draw the button on the given surface.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        label = self.font.render(self.text, True, self.text_color)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    def is_clicked(self, pos):
        """
        Return True if the given position (x, y) is inside the button.
        """
        return self.rect.collidepoint(pos)