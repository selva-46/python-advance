from tkinter import *

root = Tk()
root.title("ARITHMETIC OPERATION")
root.geometry("500x400")


f1 = Frame(root)
f1.config(bg="purple")
f1.pack(fill=BOTH, expand=0)

l1 = Label(f1, text="ARITHMETIC OPERATION", bg="purple", fg="white", font=("Arial", 20, "bold"))
l1.pack(pady=10)

l2 = Label(root, text="MARK SHEET",bg="pink",fg="white",font=("Arial", 16, "bold"))
l2.pack()

l3= Label(root, text="Enter the name")
l3.pack()  
e= Entry(root)
e.pack()

l4 = Label(root,text="Enter Reg No:")
l4.pack()
e= Entry(root)
e.pack()


l5= Label(root, text="Python mark")
l5.pack()  
e1= Entry(root)
e1.pack()


l6= Label(root, text="Data base mark")
l6.pack()
e2= Entry(root)
e2.pack()

l7= Label(root, text="Accounts mark")
l7.pack()  
e3= Entry(root)
e3.pack()


l8= Label(root, text="Total")
l8.pack()  
e4= Entry(root)
e4.pack()


l9= Label(root, text="Average")
l9.pack()  
e5= Entry(root)
e5.pack()


l10= Label(root, text="calculate")
l10.pack()  
e6= Entry(root)
e6.pack()




root.mainloop()
