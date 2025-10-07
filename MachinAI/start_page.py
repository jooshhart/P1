import tkinter as tk
from tkinter import messagebox
import os

LINKS_FILE = "saved_links.txt"

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Welcome to MachinAI!", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Enter the link to your data file (CSV, XLSX, or ZIP):").pack(pady=5)

        self.link_var = tk.StringVar()
        tk.Entry(self, textvariable=self.link_var, width=60).pack(pady=5)

        tk.Button(self, text="Use Link", width=25, command=self.use_link).pack(pady=10)
        tk.Button(self, text="Save Link", width=25, command=self.save_link).pack(pady=2)
        tk.Button(self, text="Saved Links", width=25, command=self.show_saved_links_canvas).pack(pady=2)
        tk.Button(self, text="Exit", width=25, command=controller.quit).pack(pady=10)

        self.saved_links_canvas = None  # Will hold the overlay canvas

    def use_link(self):
        link = self.link_var.get().strip()
        if not link:
            messagebox.showwarning("Input Needed", "Please enter a data file link.")
            return
        self.controller.frames["DataPage"].set_data_link(link)
        self.controller.show_frame("DataPage")

    def save_link(self):
        link = self.link_var.get().strip()
        if not link:
            messagebox.showwarning("Input Needed", "Please enter a link to save.")
            return
        links = self.get_links()
        if link in links:
            messagebox.showinfo("Already Saved", "This link is already saved.")
            return
        with open(LINKS_FILE, "a", encoding="utf-8") as f:
            f.write(link + "\n")
        messagebox.showinfo("Saved", "Link saved successfully.")

    def show_saved_links_canvas(self):
        if self.saved_links_canvas is not None:
            return  # Already open

        # Overlay frame to block interaction with the rest of the page
        self.saved_links_canvas = tk.Frame(self, bg="#eeeeee", bd=2, relief="ridge")
        self.saved_links_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        tk.Label(self.saved_links_canvas, text="Saved Links", font=("Arial", 16), bg="#eeeeee").pack(pady=10)

        btn_frame = tk.Frame(self.saved_links_canvas, bg="#eeeeee")
        btn_frame.pack(pady=5)
        load_btn = tk.Button(btn_frame, text="Load Link", width=15, command=lambda: self.load_selected_link(listbox))
        load_btn.pack(side="left", padx=5)
        delete_btn = tk.Button(btn_frame, text="Delete Link", width=15, command=lambda: self.delete_selected_link(listbox))
        delete_btn.pack(side="left", padx=5)

        listbox = tk.Listbox(self.saved_links_canvas, width=80, height=10)
        listbox.pack(pady=10)
        for link in self.get_links():
            listbox.insert(tk.END, link)

        tk.Button(self.saved_links_canvas, text="Cancel", width=20, command=self.hide_saved_links_canvas).pack(pady=10)

        self.saved_links_listbox = listbox  # For reference in other methods

    def hide_saved_links_canvas(self):
        if self.saved_links_canvas is not None:
            self.saved_links_canvas.destroy()
            self.saved_links_canvas = None

    def load_selected_link(self, listbox):
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a link to load.")
            return
        link = listbox.get(selection[0])
        self.link_var.set(link)
        self.hide_saved_links_canvas()

    def delete_selected_link(self, listbox):
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a link to delete.")
            return
        index = selection[0]
        links = self.get_links()
        del links[index]
        with open(LINKS_FILE, "w", encoding="utf-8") as f:
            for l in links:
                f.write(l + "\n")
        # Refresh listbox
        listbox.delete(0, tk.END)
        for link in links:
            listbox.insert(tk.END, link)

    def get_links(self):
        if not os.path.exists(LINKS_FILE):
            return []
        with open(LINKS_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]