import tkinter as tk
from pages.menu import MenuPage
from pages.profile import ProfilePage
import json
import sys
import os


# ----------------------
# PyInstaller Resource Helper
# ----------------------
def resource_path(relative_path):
    """
    Get absolute path to resource.
    Works for development and for PyInstaller (onefile).
    """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


# ----------------------
# Settings + Icon Files (NOW USING resource_path)
# ----------------------
SETTINGS_FILE = resource_path("settings.txt")
ICON_FILE = resource_path("ProfitCalculator.ico")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Profit Calculator")

        # icon (safe for PyInstaller)
        try:
            self.iconbitmap(ICON_FILE)
        except Exception:
            pass

        # --- Minimum allowable window size ---
        self.minsize(500, 440)

        # last known normal geometry
        self.normal_geometry = None

        # bind AFTER initialization
        self.bind("<Configure>", self._remember_normal_geometry)

        # Load previous window position/size
        self.load_window_settings()

        # Set close protocol
        self.protocol("WM_DELETE_WINDOW", self.exit_app)

        # Current page
        self.current_page = None

        # Start with menu
        self.show_menu_page()

    # ----------------------
    # Window Settings
    # ----------------------
    def _remember_normal_geometry(self, event=None):
        """Record geometry ONLY when window is normal (restored)."""
        try:
            if self.state() == "normal":
                self.normal_geometry = (
                    self.winfo_width(),
                    self.winfo_height(),
                    self.winfo_x(),
                    self.winfo_y(),
                )
        except tk.TclError:
            pass

    def save_window_settings(self):
        """Save normal window geometry + maximized state."""
        if self.normal_geometry is None:
            try:
                width = max(self.winfo_width(), 500)
                height = max(self.winfo_height(), 440)
                x = self.winfo_x()
                y = self.winfo_y()
            except tk.TclError:
                width, height, x, y = 800, 600, 100, 100
        else:
            width, height, x, y = self.normal_geometry
            width = max(width, 500)
            height = max(height, 440)

        data = {
            "width": width,
            "height": height,
            "x": x,
            "y": y,
            "maximized": (self.state() == "zoomed"),
        }

        try:
            with open(SETTINGS_FILE, "w") as f:
                json.dump(data, f)
        except Exception:
            pass

    def load_window_settings(self):
        """Load saved window geometry and restore maximized state."""
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    data = json.load(f)

                width = max(data.get("width", 800), 500)
                height = max(data.get("height", 600), 440)
                x = data.get("x", 100)
                y = data.get("y", 100)
                maximized = data.get("maximized", False)

                self.geometry(f"{width}x{height}+{x}+{y}")
                self.normal_geometry = (width, height, x, y)

                if maximized:
                    self.after(50, lambda: self.state("zoomed"))

            except Exception:
                self.geometry("800x600+100+100")
                self.normal_geometry = (800, 600, 100, 100)
        else:
            self.geometry("800x600+100+100")
            self.normal_geometry = (800, 600, 100, 100)

    # ----------------------
    # Exit
    # ----------------------
    def exit_app(self):
        """Auto-save profile and window settings on exit."""
        if isinstance(self.current_page, ProfilePage):
            try:
                self.current_page.save()
            except Exception:
                pass

        if isinstance(self.current_page, MenuPage):
            try:
                self.current_page.unbind_scrollwheel()
            except Exception:
                pass

        self.save_window_settings()

        try:
            self.destroy()
        except Exception:
            pass

    # ----------------------
    # Page Management
    # ----------------------
    def show_menu_page(self, refresh=False):
        if self.current_page:

            if isinstance(self.current_page, MenuPage):
                try:
                    self.current_page.unbind_scrollwheel()
                except Exception:
                    pass

            if isinstance(self.current_page, ProfilePage):
                try:
                    self.current_page.save()
                except Exception:
                    pass

            try:
                self.current_page.destroy()
            except Exception:
                pass

        self.current_page = MenuPage(self)
        self.current_page.pack(fill="both", expand=True)

        if hasattr(self.current_page, "_initial_layout"):
            self.current_page.after_idle(self.current_page._initial_layout)

    def show_profile_page(self, profile_name):
        if self.current_page:

            if isinstance(self.current_page, ProfilePage):
                try:
                    self.current_page.save()
                except Exception:
                    pass

            if isinstance(self.current_page, MenuPage):
                try:
                    self.current_page.unbind_scrollwheel()
                except Exception:
                    pass

            try:
                self.current_page.destroy()
            except Exception:
                pass

        self.current_page = ProfilePage(self, profile_name)
        self.current_page.pack(fill="both", expand=True)


# ----------------------
# Run App
# ----------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()