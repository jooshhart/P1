import tkinter as tk
from tkinter import messagebox
from middleware import to_numpy

class DataPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.data_link = None
        self.data_array = None
        self.columns = None

        tk.Label(self, text="Data Fetched from API", font=("Arial", 16)).pack(pady=10)
        self.data_box = tk.Text(self, height=12, width=90)
        self.data_box.pack(pady=10)
        tk.Button(self, text="Run Machine Learning", width=25,
                  command=self.run_ml).pack(pady=5)
        tk.Button(self, text="Back to Start", width=25,
                  command=lambda: controller.show_frame("StartPage")).pack(pady=5)

    def set_data_link(self, link):
        self.data_link = link

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.display_data()

    def display_data(self):
        self.data_box.delete("1.0", tk.END)
        if not self.data_link:
            self.data_box.insert(tk.END, "No data link provided.")
            return
        try:
            # Use middleware to download and convert to numpy array and columns
            self.data_array, self.columns = to_numpy(self.data_link)
            # Display header and first 10 rows
            header = " | ".join(self.columns)
            self.data_box.insert(tk.END, header + "\n" + "-" * len(header) + "\n")
            for row in self.data_array[:10]:
                line = " | ".join(str(cell) for cell in row)
                self.data_box.insert(tk.END, line + "\n")
        except Exception as e:
            self.data_box.insert(tk.END, f"Error loading data: {e}")

    def run_ml(self):
        if self.data_array is None:
            messagebox.showwarning("No Data", "No data to run ML on!")
            return
        # You can pass self.data_array to your ML page or handler as needed
        self.controller.set_ml_model(self.data_array)
        self.controller.show_frame("MLPage")