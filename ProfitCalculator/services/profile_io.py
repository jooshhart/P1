import os
import json
import sys


def app_data_path(filename):
    """
    Always return a path next to the EXE (PyInstaller) or next to app.py (development).
    This is a writable directory.
    """
    if hasattr(sys, '_MEIPASS'):
        # Running as a PyInstaller EXE
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as normal python
        base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, filename)


PROFILES_FILE = app_data_path("profiles.txt")


def ensure_profiles_file():
    """Create the profiles file if missing."""
    if not os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, "w") as f:
            json.dump({}, f, indent=4)


def load_all_profiles() -> dict:
    """Load profiles from profiles.txt"""
    ensure_profiles_file()

    with open(PROFILES_FILE, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {}  # corrupted file fallback


def save_all_profiles(profiles: dict):
    """Write all profiles to file."""
    with open(PROFILES_FILE, "w") as f:
        json.dump(profiles, f, indent=4)


def load_profile(profile_name: str) -> dict:
    """Load a single profile"""
    profiles = load_all_profiles()

    if profile_name not in profiles:
        profiles[profile_name] = {"income": [], "expenses": []}

    return profiles[profile_name]


def save_profile(profile_name: str, profile_data: dict):
    """Save a single profile"""
    profiles = load_all_profiles()
    profiles[profile_name] = profile_data
    save_all_profiles(profiles)