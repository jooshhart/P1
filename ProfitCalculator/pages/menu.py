import tkinter as tk
from .menu_actions import (
    populate_profiles_action,
    create_profile_action,
    on_resize_action,
)
from .menu_buttons import PillButton, BUTTON_COLOR_PROFILE, BUTTON_COLOR_CREATE, BUTTON_COLOR_EXIT

MARGIN = 20


class MenuPage(tk.Frame):
    def __init__(self, app, refresh=False):
        super().__init__(app, bg="#f0f0f0")
        self.app = app

        # ----------------
        # Main container
        # ----------------
        self.container = tk.Frame(self, bg="#f0f0f0", padx=MARGIN, pady=MARGIN)
        self.container.pack(expand=True, fill="both")

        # Title
        self.title_label = tk.Label(
            self.container, text="Profit Calculator",
            font=("Arial", 28, "bold"), bg="#f0f0f0"
        )
        self.title_label.pack(pady=(0, 30))

        # Choose Profile Label
        tk.Label(
            self.container, text="Choose Profile:", font=("Arial", 12, "bold"), bg="#f0f0f0"
        ).pack(pady=(0, 10))

        # ----------------
        # Scrollable container
        # ----------------
        self.scroll_frame = tk.Frame(self.container, bg="#f0f0f0")
        self.scroll_frame.pack(fill="x", expand=False, pady=(0, 20))

        self.canvas = tk.Canvas(self.scroll_frame, bg="#f0f0f0", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.profile_container = tk.Frame(self.canvas, bg="#f0f0f0")

        self.canvas.create_window((0, 0), window=self.profile_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Bind canvas configure for layout
        self.canvas.bind("<Configure>", lambda e: self._arrange_buttons())

        # Bind resize for dynamic adjustment
        self.bind("<Configure>", lambda e: on_resize_action(self))

        # ----------------
        # Create profile section
        # ----------------
        self.create_frame = tk.Frame(self.container, bg="#f0f0f0")
        self.create_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            self.create_frame, text="Create New Profile:", font=("Arial", 12, "bold"), bg="#f0f0f0"
        ).pack(padx=5)
        self.new_entry = tk.Entry(self.create_frame, font=("Arial", 12))
        self.new_entry.pack(side="left", padx=5, fill="x", expand=True)
        self.create_button = PillButton(
            self.create_frame, text="Create", bg=BUTTON_COLOR_CREATE, fg="white",
            command=lambda: create_profile_action(self)
        )
        self.create_button.pack(side="left", padx=5)

        # Exit button
        self.exit_button = PillButton(
            self.container, text="Exit", bg=BUTTON_COLOR_EXIT, fg="white",
            command=self.app.exit_app
        )
        self.exit_button.pack(pady=(0, 10))

        # ----------------
        # Profile buttons
        # ----------------
        self.profile_buttons = []
        populate_profiles_action(self)

        # ----------------
        # Scrollwheel binding for menu only
        # ----------------
        self.bind_scrollwheel()

        # Schedule initial layout after first render
        self.after_idle(self._initial_layout)

    # -------------------------------
    def bind_scrollwheel(self):
        """Bind the scroll wheel to this menu page only."""
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def unbind_scrollwheel(self):
        """Unbind scroll wheel when leaving the menu page."""
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Scroll canvas vertically on mouse wheel."""
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    # -------------------------------
    def _arrange_buttons(self):
        """Arrange profile buttons dynamically within the canvas."""
        if not self.profile_buttons:
            return

        canvas_width = self.canvas.winfo_width() - 2
        if canvas_width <= 1:
            self.after(10, self._arrange_buttons)
            return

        x, y = 0, 0
        max_height_in_row = 0
        padding = 5

        for btn in self.profile_buttons:
            btn.update_idletasks()
            bw = btn.winfo_reqwidth()
            bh = btn.winfo_reqheight()
            max_height_in_row = max(max_height_in_row, bh)

            if x + bw > canvas_width:
                x = 0
                y += max_height_in_row + padding
                max_height_in_row = bh

            btn.place(x=x, y=y)
            x += bw + padding

        self.profile_container.config(width=canvas_width, height=y + max_height_in_row + padding)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # -------------------------------
    def _initial_layout(self):
        on_resize_action(self)