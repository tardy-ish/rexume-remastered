import keyboard as k
from backend import Slot, SlotList
from pprint import pprint
from time import sleep
import sys

rexume = Slot(isMain=True)
pprint(rexume.__dict__)

import customtkinter as ctk
import tkinter as tk
from utils import contTuple
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x600")
        self.title("Rexume 2.0")

        slot = SlotElement(master = self)
        slot.grid(row=0,column=0,padx = 25,pady = 25)


class SlotElement(ctk.CTkFrame):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width = 800, height = 170)
        self.icon_label = ctk.CTkLabel(master=self,
                                    width=120,
                                    height=120,
                                    # bg_color="gray95"
                                    )
        self.icon_label.grid(row = 0, column = 0,rowspan = 3,padx = (15,10),pady = 30)

        self.title = tk.StringVar(value="  Title: ")
        self.title_label = ctk.CTkLabel(master=self,
                                        width=500,
                                        fg_color="darkred",
                                        anchor="w",
                                        corner_radius=3,
                                        textvariable=self.title)

        self.exe = tk.StringVar(value="  Exe Loc: ")
        self.exe_label = ctk.CTkLabel(master=self,
                                    width=500,
                                    bg_color="blue",
                                    anchor="w",
                                    corner_radius=3,
                                    textvariable = self.exe)

        self.ram = tk.StringVar(value="  Ram Occupied: ")
        self.ram_label = ctk.CTkLabel(master=self,
                                    width=500,
                                    # fg_color="darkblue",
                                    anchor="w",
                                    corner_radius=3,
                                    textvariable = self.ram)

        self.title_label.grid(row = 0, column = 1,padx = 10,pady=(36,0))
        self.exe_label.grid(row = 1, column = 1,padx = 10,pady=0)
        self.ram_label.grid(row = 2, column = 1,padx = 10,pady=(0,36))

        self.but_size = 35

        img = Image.open("./icons/icons8-pause-squared-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.sus_but = ctk.CTkButton(master=self, text="",
                                    height=self.but_size, 
                                    width=self.but_size,
                                    image=img,
                                    corner_radius=5)

        img = Image.open("./icons/icons8-reset-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.res_but = ctk.CTkButton(master=self, text="",
                                    height=self.but_size, 
                                    width=self.but_size,
                                    image=img,
                                    corner_radius=5)

        img = Image.open("./icons/icons8-remove-24.png")
        img = ctk.CTkImage(light_image=img,dark_image=img)
        self.del_but = ctk.CTkButton(master=self, text="",
                                    height=self.but_size, 
                                    width=self.but_size, 
                                    corner_radius=5,
                                    image=img,
                                    fg_color="red",
                                    hover_color="darkred")

        

        self.sus_but.grid(row = 0, column = 2, padx = 10, pady = (20,0))
        self.res_but.grid(row = 1, column = 2, padx = 10)
        self.del_but.grid(row = 2, column = 2, padx = 10, pady = (0,20))

if __name__ == "__main__":
    app = App()
    app.mainloop()