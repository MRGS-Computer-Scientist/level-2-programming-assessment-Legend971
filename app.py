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

    def init_main_app(self, frame):
        # Create a frame for the header and progress bar
        self.header_frame = tk.Frame(frame)
        self.header_frame.pack(fill="x", pady=10, padx=10)

        # Get current date
        self.current_date = datetime.now().strftime("%a, %b %d, %Y")

        # Create header with current date
        self.header = tk.Label(self.header_frame, text=self.current_date, font=("Helvetica", 16))
        self.header.pack()

        # Label for daily calories required
        self.daily_cal_label = tk.Label(self.header_frame, text="Daily CALORIES Required", font=("Helvetica", 12))
        self.daily_cal_label.pack()

        # Frame and canvas for progress bar
        self.progress_frame = tk.Frame(self.header_frame)
        self.progress_frame.pack(fill="x", pady=5)
        self.progress_bar = Canvas(self.progress_frame, height=20, bg='white')
        self.progress_bar.pack(fill="x")
        # Text on the progress bar
        self.progress_text = self.progress_bar.create_text(150, 10, text="3/2000", anchor="e", font=("Helvetica", 10))

        # Initial meal calorie data and limits
        self.meal_calories = [1, 1, 1]  # Breakfast, Lunch, Dinner (Dinner waiting for input)
        self.colors = ["#9dc3e6", "#ffc000", "#00b0f0"]  # Corresponding colors
        self.meal_labels = ["Breakfast", "Lunch", "Dinner"]
        self.calorie_limits = [500, 700, 800]  # Example calorie limits for each meal

        # Create pie chart canvas
        self.chart_frame = tk.Frame(frame)
        self.chart_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.chart_canvas = Canvas(self.chart_frame)
        self.chart_canvas.pack(fill="both", expand=True)
        self.arcs = self.draw_pie_chart(self.chart_canvas, self.meal_calories, self.colors, self.meal_labels)

        # Bind click events to the pie chart segments
        self.chart_canvas.bind("<Button-1>", self.on_pie_click)

        # Create input fields and bars for each meal
        self.create_meal_inputs(frame)

        # Home button
        self.home_button = tk.Button(frame, text="Home", font=("Helvetica", 12), command=lambda: self.show_frame(self.cover_frame))
        self.home_button.pack(pady=20)

    def draw_pie_chart(self, canvas, data, colors, labels):
        """
        Draws a pie chart on the given canvas.
        """
        canvas.delete("all")  # Clear the canvas
        total = sum(data)  # Calculate total calories
        start_angle = 0  # Starting angle for the first segment
        arcs = []
        for i, value in enumerate(data):
            extent = (value / total) * 360  # Calculate the extent of the segment
            arc = canvas.create_arc((50, 50, 350, 350), start=start_angle, extent=extent, fill=colors[i], tags=labels[i])
            arcs.append(arc)
            start_angle += extent  # Update starting angle for the next segment
        return arcs
    
    def on_pie_click(self, event):
        """
        Handles click events on the pie chart segments.
        """
        item = self.chart_canvas.find_closest(event.x, event.y)  # Find the item closest to the click
        tags = self.chart_canvas.gettags(item)  # Get the tags of the item
        if tags:
            label = tags[0]  # Get the first tag (the label)
            for meal, calories in zip(self.meal_labels, self.meal_calories):
                if meal == label:
                    messagebox.showinfo("Meal Info", f"{meal}: {calories} CALORIES")  # Show meal info in a message box
