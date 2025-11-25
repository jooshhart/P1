import tkinter as tk
from .profile_rows import add_row

def build_tab(page, tab, row_list):
    # Header
    header = tk.Frame(tab)
    header.pack(pady=5)
    for h in ["Category", "Name", "Amount", "Freq", ""]:
        tk.Label(header, text=h, width=12).pack(side="left")

    # Scrollable frame
    canvas = tk.Canvas(tab)
    scrollbar = tk.Scrollbar(tab, orient="vertical", command=canvas.yview)
    row_area = tk.Frame(canvas)

    row_area.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=row_area, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tab.rows = row_list
    tab.row_area = row_area

    # Add Entry button at bottom
    add_btn_frame = tk.Frame(tab)
    add_btn_frame.pack(fill="x", pady=10)
    add_button = tk.Button(add_btn_frame, text="Add Entry", command=lambda: add_row(page, tab))
    add_button.pack()

    # Save reference so populate_profile can use it
    tab.add_button = add_button