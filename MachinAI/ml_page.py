import tkinter as tk

class MLPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Machine Learning Results", font=("Arial", 16)).pack(pady=10)
        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        tk.Button(self, text="Back to Data", width=25,
                  command=lambda: controller.show_frame("DataPage")).pack(pady=5)
        tk.Button(self, text="Back to Start", width=25,
                  command=lambda: controller.show_frame("StartPage")).pack(pady=5)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.display_results()

    def display_results(self):
        model = self.controller.ml_model
        if model is None:
            self.result_label.config(text="No ML model found.")
            return
        coef = model.coef_[0]
        intercept = model.intercept_
        self.result_label.config(
            text=f"ML Model: Predict title length from body length\n"
                 f"Formula: title_length = {coef:.2f} * body_length + {intercept:.2f}"
        )