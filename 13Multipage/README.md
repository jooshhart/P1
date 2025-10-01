# Building a Multi-Page Tkinter Application with Multiple Files

As your applications grow, it's important to keep your code organized. In Tkinter, you can separate your app into multiple files and pages (screens), making it easier to manage and expand.

---

## Why Separate GUI and Data Handling?

- **Organization:** Keeps your code clean and easy to read.
- **Reusability:** You can reuse data handling code in other projects.
- **Maintainability:** Easier to fix bugs or add features.

---

## Typical Structure

```
your_project/
│
├── main.py            # Starts the app
├── gui/
│   ├── __init__.py
│   ├── main_page.py   # Main menu/page
│   ├── page_one.py    # Another page
│   └── page_two.py    # Another page
└── data/
    ├── __init__.py
    └── handler.py     # Data loading/saving logic
```

---

## How to Separate GUI and Data Handling

- **GUI files** (in `gui/`): Contain Tkinter frames, widgets, and page-switching logic.
- **Data files** (in `data/`): Contain functions or classes for saving, loading, or processing data (like reading/writing a `.txt` file).

---

## Example: Switching Between Pages

You can use `tk.Frame` for each page and raise the frame you want to show:

```python
# main.py
import tkinter as tk
from gui.main_page import MainPage
from gui.page_one import PageOne

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page App")
        self.geometry("400x300")

        self.frames = {}
        for F in (MainPage, PageOne):
            page = F(self)
            self.frames[F] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
```

```python
# gui/main_page.py
import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Main Page").pack()
        tk.Button(self, text="Go to Page One", command=lambda: master.show_frame(PageOne)).pack()
```

```python
# gui/page_one.py
import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Page One").pack()
        tk.Button(self, text="Back to Main", command=lambda: master.show_frame(MainPage)).pack()
```

---

## Example: Data Handling in a Separate File

```python
# data/handler.py
def save_data(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def load_data(filename):
    with open(filename, "r") as f:
        return f.read()
```

You can import and use these functions in your GUI files:

```python
from data.handler import save_data, load_data
```

---

## Summary

- Use separate files for each page and for data handling.
- Use frames and a controller (like `App`) to switch between pages.
- Import data functions where needed, keeping logic and interface separate.

This structure makes your Tkinter apps easier to build, test, and expand!

---

## Homework

**Build a Multi-Page Tkinter Application:**

1. Create an app with at least two pages (for example, a main menu and a settings page), each in its own file.
2. Use a separate file for data handling (saving and loading a simple setting or note to a `.txt` file).
3. Add buttons to switch between pages.
4. On one page, let the user enter and save some text. On another page, display the saved text.
5. Organize your code into folders as shown above.

*Bonus: Add a third page or more advanced data handling!*