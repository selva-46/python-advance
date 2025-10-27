  F1-Frame (root)

11.config(bg="red")

fl.pack(fill-BOTH, expand=True)

11-Label (f1, text="TAKSHASHILA UNIVERSITY", bg="RED", fg="YELLOW", font=("Arial",25, "bold"))

11.pack()

12-Label (f1, text="ONGUR, TINDIVANAM, VILLUPURAM DISTRICT", bg="RED", fg="YELLOW", font=("Arial", 25, "bold"))

1.2.pack()

f2-Frame (root)

12.config(bg="pink")

12.pack(fill=BOTH, expand=True)

13-Label (f2,text="STUDFENT INFORMATION")

13.pack()

14-Label (root, text="ENROLLMENT ID")

14.pack()

e-Entry (root)

e.pack()

15-Label (root, text="NAME OF THE STUDENT")

15.pack()

e-Entry (root)

e.pack()

Foot.mainloop()

from tkinter import *

root=Tk()

root.title("BCA APPS")
