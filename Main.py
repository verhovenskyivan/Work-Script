from tkinter import *
import tkinter.messagebox
import customtkinter


customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")  


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pups Helper")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Вводи паки сюда:", width=100, height=300)
        self.entry.grid(row=1, column=1, columnspan=1, padx=(0, 500), pady=(200, 0), sticky="nsew")
        
        self.button = customtkinter.CTkButton(self, text="Удалить паки")
        self.button.grid(row=3, column=1, columnspan=1, padx=(500,0), pady=(20, 20), sticky="nsew")
         
        self.button = customtkinter.CTkButton(self, text="Пометить паки недопоставкой")
        self.button.grid(row=4, column=1, columnspan=1, padx=(500,0), pady=(20, 20), sticky="nsew")
        
        self.button = customtkinter.CTkButton(self, text="Перенести паки в зону ДВ")
        self.button.grid(row=5, column=1, columnspan=1, padx=(500,0), pady=(20, 20), sticky="nsew")
        

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pups Helper", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"])
        
        
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "100%"])
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
       
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()