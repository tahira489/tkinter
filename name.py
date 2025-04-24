from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Tkinter window')

greeting = Label(text='this is text',fg='red',bg='black')
button = Button(text='click here', fg='green',bg='orange')
entry = Entry(fg='black', bg='blue', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=3)
frame.pack()
label = Label(master=frame, text='frame')
label.pack()

textbox = Text(fg='blue', bg='white')
textbox.pack()

window.mainloop()