from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("FirstLine Helper")
root.geometry("300x300")

first_frame = Frame(root, width=200, height=300)
first_frame.grid(row= 0, column= 0, padx=5, pady=5)

style = Style()

style.map('TButton', foreground = ([('active', 'black')]))
                     

style.configure("TButton", font=("Arial", 10),bold=True, borderwidth=2)

Label(first_frame, text="EXPRESS_PUPS", relief=RAISED).grid(row=0, column=0, padx=100, pady=3)

DB= Button(root, text="Удалить паки", command = NONE)
DB.grid(row=1, column=0, padx=10, pady=5,  sticky="nsew")
NDB =Button(first_frame, text="Пометить недопоставкой", command = NONE)
NDB.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
DVB = Button(first_frame, text="Переместить в зону ДВ", command = NONE)
DVB.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")


Link_entry = Entry(root, width=20)
Link_entry.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")


Pack_entry = Entry(root, width=20)
Pack_entry.grid(row=5, column=0, padx=(10,10), pady=(0,5))


root.mainloop()