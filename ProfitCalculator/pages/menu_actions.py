import tkinter as tk
from tkinter import messagebox
from .menu_buttons import PillButton, BUTTON_COLOR_PROFILE
from services.profile_io import load_all_profiles, save_all_profiles


def populate_profiles_action(page):
    for widget in page.profile_container.winfo_children():
        widget.destroy()

    profiles = list(load_all_profiles().keys())
    page.profile_buttons = []

    for profile_name in profiles:
        btn = PillButton(
            page.profile_container,
            text=profile_name,
            bg=BUTTON_COLOR_PROFILE,
            fg="white",
            command=lambda name=profile_name: page.app.show_profile_page(name)
        )
        btn.pack(padx=5, pady=5, side="left")
        page.profile_buttons.append(btn)

    page.after_idle(page._arrange_buttons)


def create_profile_action(page):
    name = page.new_entry.get().strip()
    if not name:
        messagebox.showwarning("Error", "Profile name cannot be empty.")
        return

    profiles = load_all_profiles()
    if name in profiles:
        messagebox.showerror("Error", "Profile already exists.")
        return

    profiles[name] = {"income": [], "expenses": []}
    save_all_profiles(profiles)
    page.new_entry.delete(0, tk.END)
    populate_profiles_action(page)


def on_resize_action(page):
    width = page.winfo_width()
    new_title_size = max(18, min(int(width / 20), 60))
    page.title_label.config(font=("Arial", new_title_size, "bold"))

    canvas_width = max(width - 10, 100)
    page.canvas.config(width=canvas_width)

    if page.profile_buttons:
        btn_height = page.profile_buttons[0].winfo_height() or 40
        page.canvas.config(height=int(btn_height * 2.8))

    page._arrange_buttons()


def on_mousewheel_action(canvas, event):
    """Scroll the canvas vertically with the mouse wheel."""
    if canvas.winfo_exists():  # make sure canvas still exists
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")