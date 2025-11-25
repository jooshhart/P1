import tkinter as tk
from tkinter import ttk
from services.profile_io import load_profile
from .profile_tabs import build_tab
from .profile_rows import add_row, delete_row
from .profile_actions import (
    populate_profile,
    save_profile_data,
    rename_profile_action,
    delete_profile_action,
    update_summary_action
)


class ProfilePage(tk.Frame):
    def __init__(self, app, profile_name):
        super().__init__(app)
        self.app = app
        self.profile_name = profile_name

        # -------------------------------------
        # TOP BAR
        # -------------------------------------
        top_bar = tk.Frame(self)
        top_bar.pack(fill="x", pady=5, padx=5)

        tk.Button(top_bar, text="← Back to Menu",
                  command=self.back).pack(side="left", padx=5)

        tk.Button(top_bar, text="🗑 Delete Profile",
                  fg="white", bg="#c0392b",
                  command=lambda: delete_profile_action(self)
                  ).pack(side="right", padx=5)

        # -------------------------------------
        # TITLE + RENAME
        # -------------------------------------
        title_bar = tk.Frame(self)
        title_bar.pack(pady=5)

        self.title_label = tk.Label(
            title_bar,
            text=f"Profile: {profile_name}",
            font=("Arial", 18)
        )
        self.title_label.pack(side="left")

        tk.Button(
            title_bar,
            text="✏ Rename",
            command=lambda: rename_profile_action(self)
        ).pack(side="left", padx=10)

        # -------------------------------------
        # MAIN CONTAINER
        # -------------------------------------
        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=20)

        self.notebook = ttk.Notebook(container)
        self.notebook.pack(side="left", fill="both", expand=True)

        # Tabs
        self.income_tab = tk.Frame(self.notebook)
        self.expense_tab = tk.Frame(self.notebook)
        self.summary_tab = tk.Frame(self.notebook)

        self.notebook.add(self.income_tab, text="Income")
        self.notebook.add(self.expense_tab, text="Expenses")
        self.notebook.add(self.summary_tab, text="Summary")

        # Row storage
        self.income_rows = []
        self.expense_rows = []

        # Build tabs (scrollable logic now in profile_tabs.py)
        build_tab(self, self.income_tab, self.income_rows)
        build_tab(self, self.expense_tab, self.expense_rows)

        self.summary_label = tk.Label(self.summary_tab, text="", font=("Arial", 12))
        self.summary_label.pack(pady=15)

        # Load profile data
        data = load_profile(profile_name)
        populate_profile(self, data)

        update_summary_action(self)

        # Auto-save on exit
        self.app.protocol("WM_DELETE_WINDOW", self.app_exit_handler)

    # -------------------------------------
    def app_exit_handler(self):
        try:
            save_profile_data(self)
        except:
            pass
        self.app.destroy()

    # -------------------------------------
    def back(self):
        save_profile_data(self)
        self.app.show_menu_page(refresh=True)