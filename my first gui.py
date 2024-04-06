from tkinter import *
import tkinter as tk



window = Tk()
window.title('My First Gui')
window = Canvas(window,width=450, height=450)
window.pack()


image = Tk.PhotoImage(file = 'C:\\Users\\PC\\Desktop\\picture\\sanitizer.jpg')
label = Tk.Label(win,image=image)
labe.place(x=10,y=10)


window.mainloop()
