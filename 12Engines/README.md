# Using Engines to Build Applications in Python

## What Is an Engine?

An **engine** is a library or framework that helps you build applications with windows, graphics, and user interfaces. Engines make it much easier to create games or apps that users can interact with, instead of just using the terminal.

---

## Why Use an Engine?

- **Easier UI:** Engines provide tools to create windows, buttons, text boxes, and more.
- **Graphics:** You can display images, shapes, and animations.
- **Events:** Engines help you handle user actions like clicks and key presses.
- **Professional Look:** Your app can look and feel like real software!

---

## Safe and Effective Python Engines

Here are some popular, safe, and effective engines for beginners:

### 1. **Tkinter** (Standard Library)
- **What:** Built-in with Python, great for simple windows and forms.
- **Best for:** Forms, simple apps, basic GUIs.

### 2. **Pygame**
- **What:** Popular for making 2D games.
- **Best for:** Games, interactive graphics.

### 3. **PyQt** or **PySide**
- **What:** Advanced, professional-looking windows and widgets.
- **Best for:** Complex apps, professional UIs.

---

## Customizing the Tkinter Window

You can change the window’s title, size, icon, and even add images or colors to make your app stand out.

### Example: Advanced Customization

Below are some common customizations, with explanations:

```python
import tkinter as tk
from PIL import Image, ImageTk  # For advanced image support

window = tk.Tk()

# Set window title
window.title("My Custom App")

# Set window size (width x height)
window.geometry("700x750")

# Make window resizable
window.resizable(True, True)

# Set window to a specific size or full screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# window.geometry(f"{screen_width}x{screen_height}")  # Uncomment for full screen

# Set window icon (try .ico first, fallback to image if needed)
try:
    window.iconbitmap("resources/myicon.ico")
except Exception as e:
    print("ICO icon not found or failed to load:", e)
    icon_img = Image.open("resources/myicon.jpg")
    icon_photo = ImageTk.PhotoImage(icon_img)
    window.iconphoto(False, icon_photo)

# Add a button that shows a message
def say_good_job():
    tk.messagebox.showinfo("Message", "Good job!")

button = tk.Button(window, text="Click Me!", command=say_good_job)
button.pack(pady=20)

window.mainloop()
```

**Why do these things?**
- **window.title()**: Makes your app look professional and easy to identify.
- **window.geometry()**: Controls the size so your app fits the screen or your needs.
- **window.resizable()**: Lets users resize the window if you want.
- **window.iconbitmap() / window.iconphoto()**: Sets a custom icon for your app window and taskbar.
- **ImageTk.PhotoImage**: Lets you use more image formats (like JPG or PNG) for icons or display.
- **messagebox.showinfo()**: Gives feedback to the user in a popup.

---

## Organizing Your Code

For bigger projects, split your code into multiple files:
- `main.py` — Starts the app and sets up the main window.
- `gui/main_window.py` — Contains your main window class or functions.
- `utils.py` — Utility functions, like `resource_path()` for finding files.

**Example: Importing and Using Custom Modules**

```python
from utils import resource_path
from gui.main_window import MainWindow

app = tk.Tk()
# ... set up window ...
main_frame = MainWindow(app)
main_frame.pack(fill="both", expand=True)
```

---

## Why Is the `.ico` Icon Important?

The `.ico` file is the standard icon format for Windows applications.  
When you set a window icon in Tkinter (or when you build an `.exe`), Windows expects an `.ico` file.  
A good `.ico` file makes your app look professional in the taskbar, window, and when sharing your `.exe`.

### Why Use `.ico` Instead of `.png` or `.jpg`?

- Windows uses `.ico` for app and shortcut icons.
- `.ico` files can contain multiple sizes in one file (16x16, 32x32, 48x48, 64x64, 128x128, 256x256).
- This ensures your icon looks sharp at any size, from the taskbar to the desktop.

---

## How to Make a Multi-Size `.ico` File

1. **Design Your Icon:**  
   - Use a graphics editor like [GIMP](https://www.gimp.org/), [Paint.NET](https://www.getpaint.net/), or an online tool like [favicon.io](https://favicon.io/) or [icoconvert.com](https://icoconvert.com/).
   - Make sure your icon is square and looks good at small sizes.

2. **Export or Convert to `.ico`:**  
   - Many editors let you export directly to `.ico`.
   - For best results, export your icon at several sizes (e.g., 16x16, 32x32, 64x64, 128x128, 256x256) and combine them into one `.ico` file using an online converter.

3. **Test Your Icon:**  
   - Place the `.ico` file in your project (e.g., `resources/myicon.ico`).
   - Use it in your Tkinter app:
     ```python
     window.iconbitmap("resources/myicon.ico")
     ```
   - When you build your `.exe` with PyInstaller, use the same `.ico` file for the `--icon` option.

---

**Tip:**  
A multi-size `.ico` ensures your app's icon always looks crisp, whether it's in the taskbar, Alt+Tab menu, or on the desktop.

---

## How to Turn Your App Into an `.exe` File

You can use a tool called **PyInstaller** to convert your Python script into a standalone Windows executable.

### Steps:

1. **Install PyInstaller**  
   ```
   pip install pyinstaller
   ```

2. **Navigate to Your Project Folder**  
   Use `cd` to change to the folder with your main Python file.

3. **Run PyInstaller**  
   ```
   pyinstaller --onefile --windowed --icon=resources/myicon.ico main.py
   ```
   - `--onefile` puts everything in a single `.exe`.
   - `--windowed` hides the terminal window (for GUI apps).
   - `--icon` sets your custom icon.

4. **Find Your `.exe`**  
   Look in the new `dist` folder for your `.exe` file.

5. **Share Your App!**  
   You can now share the `.exe` and your `resources` folder (if needed) with others.

---

## Homework

**Create a Tkinter application that:**
- Has a custom window title, size, and icon.
- Loads an image and displays it in the window.
- Has a button that, when clicked, shows a message saying “Good job!”
- Turn your app into an `.exe` file using PyInstaller.