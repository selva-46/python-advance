from tkinter import *

root = Tk()
root.title("BCA APP")
root.geometry("500x700")

f1 = Frame(root)
f1.config(bg="red")
f1.pack(fill=BOTH, expand=0)

l0 = Label(f1, text="TAKSHASHILA UNIVERSITY", bg="red", fg="yellow", font=("Arial", 25, "bold"))
l0.pack(pady=10)

l1 = Label(f1, text="ongur(po),tindivanam taluk, villipuram district, tamal nadu, india -604305", bg="red", fg="yellow", font=("Arial", 10, "bold"))
l1.pack(pady=10)


f2 = Frame(root)
f2.config(bg="pink")
f2.pack(fill=BOTH, expand=0)

l2 = Label(f2, text="STUDENT INFORMATION RECORD", bg="pink", fg="black", font=("Arial", 16))
l2.pack(pady=10)


l1 = Label(root, text="ENTROL NO")  
l1.pack()

e2 = Entry(root)
e2.pack()

l3 = Label(root, text="NAME OF THE STUDENT")  
l3.pack()

e4 = Entry(root)
e4.pack()

 
l5 = Label(root, text="PYTHON MARK")  
l5.pack()

e6 = Entry(root)
e6.pack()

l7 = Label(root, text="DBMS MARK")  
l7.pack()

e8 = Entry(root)
e8.pack()

l9= Label(root, text="XEBIA MARK")  
l9.pack()

e0 = Entry(root)
e0.pack()

l9= Label(root, text="TOTAL MARK")  
l9.pack()

e0 = Entry(root)
e0.pack()
l9= Label(root, text="AVERAGE")  
l9.pack()

e0 = Entry(root)
e0.pack()

b2= Button(root, text="CALCULATE") 
b2.pack()



root.mainloop()
