# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
import serial





print(serial.__file__)

x=serial.Serial('COM4', baudrate=9600)
x.readline().decode()

# Create an instance of tkinter window
win = Tk()


# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=700, height=500)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)




# Create an object of tkinter ImageTk
img= ImageTk.PhotoImage(Image.open("C:\\Users\\PC\\Desktop\\hand\\image7.jpg"))

if img=="C:\\Users\\PC\\Desktop\\hand\\image7.jpg":    
    x.readline().decode()=='Selerio'


# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()
