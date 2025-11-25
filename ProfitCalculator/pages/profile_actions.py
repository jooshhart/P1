import tkinter as tk
from tkinter import messagebox, simpledialog
from services.calculations import calculate_monthly_summary
from services.profile_io import (
    load_all_profiles,
    save_all_profiles,
    save_profile
)


def populate_profile(page, data):
    # Income
    for item in data.get("income", []):
        page.notebook.select(0)
        page.income_tab.add_button.invoke()  # trigger add_row
        frame, row = page.income_tab.rows[-1]
        row["category"].set(item.get("category", ""))
        row["name"].insert(0, item.get("name", ""))
        row["amount"].insert(0, item.get("amount", ""))
        row["frequency"].set(item.get("frequency", ""))

    # Expenses
    for item in data.get("expenses", []):
        page.notebook.select(1)
        page.income_tab.add_button.invoke()
        frame, row = page.expense_tab.rows[-1]
        row["category"].set(item.get("category", ""))
        row["name"].insert(0, item.get("name", ""))
        row["amount"].insert(0, item.get("amount", ""))
        row["frequency"].set(item.get("frequency", ""))


def update_summary_action(page):
    summary = calculate_monthly_summary(page.income_rows, page.expense_rows)
    page.summary_label.config(text=summary)


def save_profile_data(page):
    data = {"income": [], "expenses": []}

    for frame, row in page.income_rows:
        data["income"].append({
            "category": row["category"].get(),
            "name": row["name"].get(),
            "amount": row["amount"].get(),
            "frequency": row["frequency"].get()
        })

    for frame, row in page.expense_rows:
        data["expenses"].append({
            "category": row["category"].get(),
            "name": row["name"].get(),
            "amount": row["amount"].get(),
            "frequency": row["frequency"].get()
        })

    save_profile(page.profile_name, data)


def rename_profile_action(page):
    new_name = simpledialog.askstring("Rename Profile", "Enter a new profile name:")
    if not new_name:
        return

    new_name = new_name.strip()
    if not new_name:
        return

    profiles = load_all_profiles()

    if new_name in profiles:
        messagebox.showerror("Error", "A profile with that name already exists.")
        return

    profiles[new_name] = profiles.pop(page.profile_name)
    save_all_profiles(profiles)

    page.profile_name = new_name
    page.title_label.config(text=f"Profile: {new_name}")

    page.app.show_menu_page(refresh=True)
    page.app.show_profile_page(new_name)


def delete_profile_action(page):
    confirm = messagebox.askyesno(
        "Delete Profile",
        f"Are you sure you want to delete '{page.profile_name}'?"
    )
    if not confirm:
        return

    profiles = load_all_profiles()
    if page.profile_name in profiles:
        del profiles[page.profile_name]
        save_all_profiles(profiles)

    messagebox.showinfo("Deleted", f"Profile '{page.profile_name}' has been deleted.")
    page.app.show_menu_page(refresh=True)