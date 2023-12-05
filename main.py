import time
from tkinter import *


textt = "Wspolczesne technologie rewolucjonizuja dziedzine edukacji. Zastosowanie tabletow, laptopow i interaktywnych aplikacji umozliwia nauczycielom bardziej zaangazowane i efektywne nauczanie. Dzieki platformom edukacyjnym można dostosowac proces nauczania do indywidualnych potrzeb uczniow, umozliwiajac im rozwijanie własnych zainteresowan."

window = Tk()
window.title("Typing Test")
window.resizable(False, False)

def add_word():
    my_text = text.get("1.0", END).strip()
    x = len(my_text)
    if my_text != textt[:x].strip():
        canvas.itemconfig(text_canvas, fill="red")
    else:
        canvas.itemconfig(text_canvas, fill="black")
        if len(my_text) == len(textt):
            text.destroy()
            canvas.delete(text_canvas)
            canvas.create_text(300, 50, text=f"You've finished in time {round((time.time()-time_start), 1)} seconds!", font=("Arial", 20))

def display():
    global canvas
    global text
    global text_canvas
    global time_start
    time_start = time.time()
    canvas = Canvas(window, height=200, width=600)
    canvas.grid()
    text_canvas = canvas.create_text(300, 110, width=500, text=textt, font=("Arial", 15))
    text = Text(window, height=10, width=60, padx=20, pady=20)
    text.grid(pady=15)
    button.destroy()
    window.bind("<Key>", lambda event: add_word())

button = Button(window, text="Click\nStart!", height=10, width=20, font=("Arial", 50), command=display)
button.grid()



window.mainloop()