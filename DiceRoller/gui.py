import tkinter as tk
from logic import DICE_TYPES, roll_dice

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("D&D Dice Roller")

        tk.Label(self.root, text="Select dice type:").pack(pady=5)
        self.dice_var = tk.StringVar(value="d20")
        self.dice_menu = tk.OptionMenu(self.root, self.dice_var, *DICE_TYPES.keys())
        self.dice_menu.pack(pady=5)

        tk.Label(self.root, text="Number of dice:").pack(pady=5)
        self.num_var = tk.IntVar(value=1)
        self.num_entry = tk.Entry(self.root, textvariable=self.num_var, width=5)
        self.num_entry.pack(pady=5)

        self.roll_button = tk.Button(self.root, text="Roll", command=self.roll_dice_gui)
        self.roll_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Result will appear here.")
        self.result_label.pack(pady=10)

    def roll_dice_gui(self):
        dice_type = self.dice_var.get()
        num = self.num_var.get()
        if num < 1:
            self.result_label.config(text="Please enter a positive number of dice.")
            return
        rolls, total = roll_dice(dice_type, num)
        self.result_label.config(
            text=f"Rolls: {rolls}\nTotal: {total}"
        )

    def run(self):
        self.root.mainloop()