from tkinter import *

window = Tk()
w_width = 500
w_height = 500
    
bg_color = "grey"
window.title("Calorie Intake")
window.geometry(str(w_width) + "x" + str(w_height))

main_frame = Frame(background="white", width=w_width, height=w_height)
main_frame.pack()

hello_label = Label(text="Hello, World!")
hello_label.place(x=300, y=300)


window.mainloop()