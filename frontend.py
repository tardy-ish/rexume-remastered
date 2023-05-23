import customtkinter as ctk
import tkinter as tk
from PIL import Image

class ConfirmationBox(ctk.CTkToplevel):
    def __init__(self,__yes__,__no__ = lambda: print("Pressed No"), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x180")
        self.title("Confirm Slot Deletion")
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(10, self._create_widgets)  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable
        self._yes = __yes__
        self._no = __no__

    def _create_widgets(self):

        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = ctk.CTkLabel(
                master=self,
                width=300,
                wraplength=300,
                fg_color="transparent",
                text="Are you sure?"
                )
        self._label.grid(
                row=0, 
                column=0, 
                columnspan=2, 
                padx=20, 
                pady=20, 
                sticky="ew"
                )

        self._yes_button = ctk.CTkButton(
                master=self,
                width=100,
                border_width=0,
                text='Yes',
                command=self._yes_event
                )
        self._yes_button.grid(
                row=2, 
                column=0, 
                columnspan=1, 
                padx=(20, 10), 
                pady=(0, 20), 
                sticky="ew"
                )

        self._no_button = ctk.CTkButton(
                master=self,
                width=100,
                border_width=0,
                text='No',
                command=self._no_event,
                )
        self._no_button.grid(
                row=2, 
                column=1, 
                columnspan=1, 
                padx=(10, 20), 
                pady=(0, 20), 
                sticky="ew"
                )

    def _yes_event(self):
        self._yes()
        self.grab_release()
        self.destroy()

    def _no_event(self):
        self._no()
        self.grab_release()
        self.destroy()

    def _on_closing(self):
        self._no()
        self.grab_release()
        self.destroy()

class ErrorDialog(ctk.CTkToplevel):
    def __init__(self,msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x180")
        self.title("Some Error Occurred")
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(10, self._create_widgets)  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable
        self.msg = msg

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = ctk.CTkLabel(
                master=self,
                width=300,
                wraplength=300,
                fg_color="transparent",
                text=f"Error Message: {self.msg}"
                )
        self._label.grid(
                row=0, 
                column=0, 
                columnspan=2, 
                padx=20, 
                pady=20, 
                sticky="ew"
                )


    def _on_closing(self):
        self.grab_release()
        self.destroy()

class SingleSlot(ctk.CTkFrame):
    def __init__(self, title,loc,slot, *args,**kwargs):
        super().__init__(*args, **kwargs)
        
        self.slot = slot

        self.configure(
                width = 800, 
                height = 170,
                fg_color = "black"
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

        self.title = tk.StringVar(value=f" Title: {title}")
        self.tit_label = ctk.CTkLabel(
                master=self,
                width=500,
                # fg_color="darkred",
                anchor="w",
                corner_radius=3,
                textvariable=self.title
                )

        self.exe = tk.StringVar(value=f" Exe Loc: {loc}")
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
        # self.ram_label.grid(
        #         row = 2, 
        #         column = 1,
        #         padx = 10,
        #         pady=(0,36)
        #         )

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
        self.del_but.grid(row = 2, column = 2, padx = 10, pady = (5,20))
    
    def suspend(self):
        try:
            # call suspend function
            self.slot.suspend()
            self.status.configure(
                fg_color = "red",
                text="Suspended"
            )
            self.slot.minimize()
        except Exception as e:
            print("Some error in suspending the program",e)
    
    def resume(self):
        try:
            # call resume function
            self.slot.resume()
            self.status.configure(
                fg_color = "green",
                text="Active"
            )
            self.slot.unminimize()
        except Exception as e:
            print("Some error in resuming the program",e)
    
    def del_event(self):
        try:
            ConfirmationBox(
                __yes__=self.delete
            )
        except Exception as e:
            print("Some error in deleting the slot",e)
    
    def delete(self):
        try:
            self.resume()
            self.grid_forget()
            self.destroy()
        except Exception as e:
            print("Some error in deleting the slot",e)
 