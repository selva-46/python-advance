import tkinter as tk
from tkinter import messagebox

def save_info():
    # Example save function
    enrollment = entry_enroll.get()
    name = entry_name.get()
    dob = entry_dob.get()
    address = entry_address.get()
    phone = entry_phone.get()
    
    # You can customize saving (to file or DB)
    messagebox.showinfo("Saved", f"Student Info Saved:\n\nEnrollment No: {enrollment}\nName: {name}\nDOB: {dob}\nAddress: {address}\nPhone: {phone}")

def cancel_info():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("500x500")
root.config(bg="lightgray")

# ---------- Frame 1: College Address ----------
frame1 = tk.Frame(root, bg="#A7C7E7", bd=2, relief="groove")
frame1.pack(fill="x", padx=10, pady=10)

college_label = tk.Label(frame1, text="Takshashila University\nOngur, Tindivanam, Villupuram - 604305",
                         bg="#A7C7E7", font=("Arial", 12, "bold"), justify="center")
college_label.pack(pady=10)

# ---------- Frame 2: Form Title ----------
frame2 = tk.Frame(root, bg="#FFD580", bd=2, relief="groove")
frame2.pack(fill="x", padx=10, pady=10)

title_label = tk.Label(frame2, text="STUDENT INFORMATION", bg="#FFD580",
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# ---------- Frame 3: Student Details ----------
frame3 = tk.Frame(root, bg="#C1E1C1", bd=2, relief="groove")
frame3.pack(fill="both", expand=True, padx=10, pady=10)

# Labels and Entry Fields
tk.Label(frame3, text="Enrollment No:", bg="#C1E1C1", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e", pady=5, padx=5)
entry_enroll = tk.Entry(frame3, width=30)
entry_enroll.grid(row=0, column=1, pady=5, padx=5)

tk.Label(frame3, text="Name of Student:", bg="#C1E1C1", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_name = tk.Entry(frame3, width=30)
entry_name.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame3, text="Date of Birth:", bg="#C1E1C1", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_dob = tk.Entry(frame3, width=30)
entry_dob.grid(row=2, column=1, pady=5, padx=5)

tk.Label(frame3, text="Address:", bg="#C1E1C1", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_address = tk.Entry(frame3, width=30)
entry_address.grid(row=3, column=1, pady=5, padx=5)

tk.Label(frame3, text="Phone:", bg="#C1E1C1", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="e", pady=5, padx=5)
entry_phone = tk.Entry(frame3, width=30)
entry_phone.grid(row=4, column=1, pady=5, padx=5)

# Buttons
btn_frame = tk.Frame(frame3, bg="#C1E1C1")
btn_frame.grid(row=5, columnspan=2, pady=20)

btn_save = tk.Button(btn_frame, text="Save", width=12, bg="lightblue", command=save_info)
btn_save.grid(row=0, column=0, padx=10)

btn_cancel = tk.Button(btn_frame, text="Cancel", width=12, bg="lightcoral", command=cancel_info)
btn_cancel.grid(row=0, column=1, padx=10)

root.mainloop()
