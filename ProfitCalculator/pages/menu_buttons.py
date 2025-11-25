import tkinter as tk

BUTTON_COLOR_PROFILE = "#4CAF50"
BUTTON_COLOR_CREATE = "#2196F3"
BUTTON_COLOR_EXIT = "#f44336"
BUTTON_HOVER = "#45a049"


class PillButton(tk.Canvas):
    def __init__(self, parent, text="", command=None, bg="#4CAF50", fg="white", radius=20):
        super().__init__(parent, height=40, bg=parent["bg"], highlightthickness=0)
        self.command = command
        self.text = text
        self.bg = bg
        self.fg = fg
        self.radius = radius
        self.font_size = 8

        self.draw_button()
        if self.command:
            self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", lambda e: self.itemconfig(self.rect, fill=BUTTON_HOVER))
        self.bind("<Leave>", lambda e: self.itemconfig(self.rect, fill=self.bg))

    def draw_button(self):
        self.delete("all")
        w = self.font_size * len(self.text) + 20
        h = self.font_size * 2 + 10
        self.config(width=w, height=h)
        self.rect = self.create_round_rect(0, 0, w, h, self.radius, fill=self.bg)
        self.create_text(w / 2, h / 2, text=self.text, fill=self.fg,
                         font=("Helvetica", self.font_size, "bold"))

    def create_round_rect(self, x1, y1, x2, y2, r=25, **kwargs):
        points = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r,
                  x2, y2-r, x2, y2, x2-r, y2, x1+r, y2,
                  x1, y2, x1, y2-r, x1, y1+r, x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)