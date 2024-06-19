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
        
    def init_frames(self):
        # Cover Frame
        self.cover_frame = tk.Frame(self.window)
        cover_label = tk.Label(self.cover_frame, text="Welcome to Calorie Tracker", font=("Helvetica", 20))
        cover_label.pack(pady=50)
        cover_continue_btn = tk.Button(self.cover_frame, text="Continue", font=("Helvetica", 14), command=lambda: self.show_frame(self.howto_frame))
        cover_continue_btn.pack(pady=20)
        cover_exit_btn = tk.Button(self.cover_frame, text="Exit", font=("Helvetica", 14), command=self.window.quit)
        cover_exit_btn.pack(pady=20)

        # How to Calculate Calories Frame
        self.howto_frame = tk.Frame(self.window)
        howto_label = tk.Label(self.howto_frame, text="How to Calculate Calories", font=("Helvetica", 20))
        howto_label.pack(pady=20)

        # Text widget for explanation
        howto_text = Text(self.howto_frame, wrap="word", font=("Helvetica", 14), height=10, width=50)
        howto_text.insert(tk.END, "Explanation on how to calculate calories...\n\n")
        howto_text.insert(tk.END, "Calories are calculated based on various factors such as weight, activity level, and basal metabolic rate (BMR). Consult a nutritionist or use a reliable online calculator for accurate results.")
        howto_text.config(state=tk.DISABLED)  # Disable editing
        howto_text.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        howto_continue_btn = tk.Button(self.howto_frame, text="Continue", font=("Helvetica", 14), command=lambda: self.show_frame(self.main_frame))
        howto_continue_btn.pack(pady=20)
        howto_exit_btn = tk.Button(self.howto_frame, text="Exit", font=("Helvetica", 14), command=self.window.quit)
        howto_exit_btn.pack(pady=20)

        # Main App Frame
        self.main_frame = tk.Frame(self.window)
        self.init_main_app(self.main_frame)

    def show_frame(self, frame):
        # Hide the current frame if it exists
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()

        # Show the new frame
        frame.pack(fill="both", expand=True)
        frame.tkraise()

        # Update the current_frame attribute
        self.current_frame = frame
