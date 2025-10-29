from tkinter import *

root = Tk()
root.title("Student Mark List")
root.geometry("500x400")

l = Label(root, text="Enter Number")
l.pack()

e = Entry(root)
e.pack()

b = Button(root, text="Submit")
b.pack()

root.mainloop()
