import tkinter, customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("300x300")
image = Image.open("interface/latech.png")
resize_image = image.resize((300,300),resample=3)

def login():
    input("Enter login: ")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=True)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Login")
entry1.pack(pady=10, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=15,padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Pups link")
entry3.pack(pady=10,padx=10)

button = customtkinter.CTkButton(master=frame, text="Start", command=login)
button.pack(pady=10,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=10,padx=10)

root.mainloop()
