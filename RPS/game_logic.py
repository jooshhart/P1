"""
game_logic.py
-------------
Contains the core logic for Rock Paper Scissors.
"""

import random

class RockPaperScissorsGame:
    """
    Handles the logic for a Rock Paper Scissors game.
    """
    CHOICES = ["Rock", "Paper", "Scissors"]

    def __init__(self):
        self.player_choice = ""
        self.computer_choice = ""
        self.result = ""

    def play_round(self, player_choice):
        """
        Play a round with the given player choice.
        """
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.CHOICES)
        self.result = self.get_winner(self.player_choice, self.computer_choice)

    def get_winner(self, player, computer):
        """
        Determine the winner.
        """
        if player == computer:
            return "Tie!"
        if (player == "Rock" and computer == "Scissors") or \
           (player == "Paper" and computer == "Rock") or \
           (player == "Scissors" and computer == "Paper"):
            return "You Win!"
        return "You Lose!"