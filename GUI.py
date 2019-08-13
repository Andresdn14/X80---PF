from tkinter import *
window = Tk()
window.title("First Try")
window.geometry('350x200')
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
def clicked():
 
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me",bg="black",fg="red",command=clicked)
btn.grid(column=1, row=0)



window.mainloop()