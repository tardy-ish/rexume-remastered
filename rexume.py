import keyboard as k
from backend import Slot, SlotList
from frontend import SingleSlot, ConfirmationBox
from pprint import pprint
from time import sleep
import sys

# rexume = Slot(isMain=True)
# pprint(rexume.__dict__)

import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.rexume = mainApp
        self.geometry("1150x600")
        self.title("Rexume 2.0")
        

        # slot = SingleSlot(master = self)
        # slot.grid(row=0,column=0,padx = 25,pady = 25)
        self.add_button = ctk.CTkButton(
                master=self,
                text="+ Add"
                )
        self.add_button.grid(
                row = 0, 
                column = 0, 
                columnspan = 5, 
                sticky = "NS",
                # command=,
                )
        
        self.rexume = Slot(isMain=True)
        pprint(self.rexume.__dict__)

    


class SingleSlot(ctk.CTkFrame):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        
        self.configure(
                width = 800, 
                height = 170,
                fg_color = "gray50"
                )
        
        self.status = ctk.CTkLabel(
                master=self,
                text="",
                width=80,
                height=80,
                # fg_color="green",
                corner_radius=7
                )

        self.status.grid(
                row = 0, 
                column = 0,
                rowspan = 3,
                padx = (15,10),
                pady = 30
                )

        self.title = tk.StringVar(value=" Title: ")
        self.tit_label = ctk.CTkLabel(
                master=self,
                width=500,
                # fg_color="darkred",
                anchor="w",
                corner_radius=3,
                textvariable=self.title
                )

        self.exe = tk.StringVar(value=" Exe Loc: ")
        self.exe_label = ctk.CTkLabel(
                master=self,
                width=500,
                # fg_color="blue",
                anchor="w",
                corner_radius=3,
                textvariable = self.exe
                )

        self.ram = tk.StringVar(value=" Ram Occupied: ")
        self.ram_label = ctk.CTkLabel(
                master=self,
                width=500,
                # fg_color="darkblue",
                anchor="w",
                corner_radius=3,
                textvariable = self.ram
                )

        self.tit_label.grid(
                row = 0, 
                column = 1,
                padx = 10,
                pady=(36,0)
                )
        self.exe_label.grid(
                row = 1, 
                column = 1,
                padx = 10,
                pady=0
                )
        self.ram_label.grid(
                row = 2, 
                column = 1,
                padx = 10,
                pady=(0,36)
                )

        self.but_size = 35

        img = Image.open("./icons/icons8-pause-squared-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.sus_but = ctk.CTkButton(
                master=self, text="",
                height=self.but_size, 
                width=self.but_size,
                image=img,
                corner_radius=5,
                command=self.suspend
                )

        img = Image.open("./icons/icons8-reset-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.res_but = ctk.CTkButton(
                master=self, text="",
                height=self.but_size, 
                width=self.but_size,
                image=img,
                corner_radius=5,
                command=self.resume
                )

        img = Image.open("./icons/icons8-remove-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.del_but = ctk.CTkButton(
                master=self, text="",
                height=self.but_size, 
                width=self.but_size, 
                corner_radius=5,
                image=img,
                fg_color="red",
                hover_color="darkred",
                command=self.del_event
                )

        self.sus_but.grid(row = 0, column = 2, padx = 10, pady = (20,0))
        self.res_but.grid(row = 1, column = 2, padx = 10)
        self.del_but.grid(row = 2, column = 2, padx = 10, pady = (0,20))
    
    def suspend(self):
        try:
            # call suspend function
            self.status.configure(
                fg_color = "red",
                text="Suspended"
            )
        except:
            print("Some error in suspending the program")
    
    def resume(self):
        try:
            # call resume function
            self.status.configure(
                fg_color = "green",
                text="Active"
            )
        except:
            print("Some error in resuming the program")
    
    def del_event(self):
        try:
            ConfirmationBox(
                __yes__=self.delete
            )
        except:
            print("Some error in deleting the slot")
    def delete(self):
        try:
            self.grid_forget()
            self.destroy()
        except:
            print("Some error in deleting the slot")

if __name__ == "__main__":
    app = App()
    app.mainloop()