import tkinter as tk
from tkinter import Canvas, messagebox, Text
from datetime import datetime

class App():
    def __init__(self, window):
        # Initialize main window
        self.window = window
        self.window.title("Calorie Tracker")
        self.window.geometry("400x800")

        # Initialize frames
        self.init_frames()

        # Show the cover page initially
        self.show_frame(self.cover_frame)
