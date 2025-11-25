import tkinter as tk
from tkinter import ttk
from .profile_actions import update_summary_action


def add_row(page, tab):
    row_data = {}
    frame = tk.Frame(tab.row_area)
    frame.pack(fill="x", pady=3)

    row_data["category"] = ttk.Combobox(frame, values=[
        "Job", "Freelance", "Billing", "Car", "Subscription",
        "Food", "Entertainment", "Medical", "Other"
    ], width=12)
    row_data["category"].pack(side="left")

    row_data["name"] = tk.Entry(frame, width=12)
    row_data["name"].pack(side="left")

    row_data["amount"] = tk.Entry(frame, width=12)
    row_data["amount"].pack(side="left")

    row_data["frequency"] = ttk.Combobox(frame, values=[
        "Hourly", "Daily", "Weekly", "Monthly", "Yearly"
    ], width=12)
    row_data["frequency"].pack(side="left")

    tk.Button(
        frame,
        text="❌",
        command=lambda f=frame: delete_row(page, f, tab)
    ).pack(side="left")

    tab.rows.append((frame, row_data))
    update_summary_action(page)


def delete_row(page, frame, tab):
    for row in tab.rows:
        if row[0] == frame:
            tab.rows.remove(row)
            break

    frame.destroy()
    update_summary_action(page)