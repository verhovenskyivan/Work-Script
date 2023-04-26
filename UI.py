import customtkinter
import tkinter
import Secret


root = tkinter.Tk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("500X350")

label = tkinter.Label(root, )
label.pack

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12,padx=10)

