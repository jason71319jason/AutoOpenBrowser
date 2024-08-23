import tkinter as tk
from tkinter import messagebox
import webbrowser
import configparser
import time
import os
import sys
import winshell

# Function to get the directory of the running executable
def get_executable_dir():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

# Config file path
config_file = os.path.join(get_executable_dir(), 'config.ini')

# Function to create a shortcut in the Startup folder
def create_startup_shortcut():
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, 'OpenBrowser.lnk')
    if not os.path.exists(shortcut_path):
        # Create the shortcut
        with winshell.shortcut(shortcut_path) as shortcut:
            shortcut.path = os.path.join(get_executable_dir(), 'OpenBrowser.exe')
            shortcut.description = 'OpenBrowser'
            shortcut.icon_location = (os.path.join(get_executable_dir(), 'OpenBrowser.exe'), 0)
        messagebox.showinfo("Info", "Shortcut created in Startup folder.")
    else:
        messagebox.showinfo("Info", "Shortcut already exists in Startup folder.")

# Function to save the configuration
def save_config(url, wait_time):
    config = configparser.ConfigParser()
    config['Settings'] = {
        'URL': url,
        'WaitTime': wait_time
    }
    try:
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        create_startup_shortcut()
        messagebox.showinfo("Info", "Configuration saved and shortcut created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save configuration: {e}")

# Function to load the configuration
def load_config():
    try:
        config = configparser.ConfigParser()
        if os.path.exists(config_file):
            config.read(config_file)
            url = config.get('Settings', 'URL')
            wait_time = config.getint('Settings', 'WaitTime')
            return url, wait_time
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load configuration: {e}")
    return None, None

# Function to open the URL
def open_url():
    url, wait_time = load_config()
    if url and wait_time:
        time.sleep(wait_time)
        webbrowser.open(url)
    else:
        messagebox.showerror("Error", "No configuration found. Please save the settings first.")

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("URL Opener Config")

    tk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10)
    url_entry = tk.Entry(root, width=40)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Wait Time (seconds):").grid(row=1, column=0, padx=10, pady=10)
    wait_time_entry = tk.Entry(root, width=10)
    wait_time_entry.grid(row=1, column=1, padx=10, pady=10)

    # Load existing config if available
    saved_url, saved_wait_time = load_config()
    if saved_url and saved_wait_time:
        url_entry.insert(0, saved_url)
        wait_time_entry.insert(0, str(saved_wait_time))

    save_button = tk.Button(root, text="Save", command=lambda: save_config(url_entry.get(), wait_time_entry.get()))
    save_button.grid(row=2, column=0, columnspan=2, pady=20)

    open_button = tk.Button(root, text="Open URL", command=open_url)
    open_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
