import tkinter, customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("500x350")

def login():
    print("Enter login: ")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="Login system", text_font=("Robot,24"))
label.pack(pady=12,padx=10)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Login")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12,padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Pups link")
entry3.pack(pady=12,padx=15)

button = customtkinter.CTkButton(master=frame, text="Start", command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12,padx=10)

root.mainloop()