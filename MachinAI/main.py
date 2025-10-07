import tkinter as tk
from start_page import StartPage
from data_page import DataPage
from ml_page import MLPage

class MachinAIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MachinAI Example Project")
        self.geometry("600x400")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, DataPage, MLPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        # Shared data (only for ML model or other app-wide info)
        self.ml_model = None

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_ml_model(self, model):
        self.ml_model = model

if __name__ == "__main__":
    app = MachinAIApp()
    app.mainloop()