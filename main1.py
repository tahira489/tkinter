from tkinter import *

window = Tk()

for i in range(4):
    for j in range(3):
        frame = Frame(master=window,relief=RAISED,borderwidt=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Label(master=frame, text=f"Row {i}\ncolumn {j}")
        label.pack()

window.mainloop()