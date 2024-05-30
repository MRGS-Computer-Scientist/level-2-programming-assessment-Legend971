from tkinter import *
from app_settings import *
from os import *

class App():

    
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        self.top_frame = Frame(background='red', width=w_width, height=100)
        self.top_frame.pack()

        self.main_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))
        self.main_frame.pack()

        self.bottom_frame = Frame(background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green')
        self.home_button.place(x=0,y=0)

        self.exit_button = Button(self.bottom_frame, text="Exit", height=2, width=5, bg='green', command=exit)
        self.exit_button.place(x=100,y=0)

        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("The path is", self.filename)

        self.window.mainloop()


    def exit(self):
        self.window.destroy()