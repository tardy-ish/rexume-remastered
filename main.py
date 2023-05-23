import keyboard as k
from backend import Slot
from frontend import SingleSlot

import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.rexume = mainApp
        self.slots = []
        self.geometry("800x600")
        self.title("Rexume 2.0")
        self.cur_row = 0
        self.guide = ctk.CTkLabel(
            master=self,
            text="Put the application in foreground and press ctrl+shift+1 to add to the list",
            width=800
        )
        self.guide.grid(
                row=999,
                # padx=50,
                pady=15
        )
        
        k.add_hotkey("ctrl+shift+1", self.addSlot)
        self.rexume = Slot(isMain=True)
    
    def gridSlot(self):
        self.slots[-1].grid(
            row=self.cur_row
        )
        self.cur_row += 1
        
    def addSlot(self):
        try:
            new_slot = Slot()
            if new_slot == self.rexume:
                raise Exception("Cannot add Rexume as a slot")
            title,loc = new_slot.give()
            self.slots.append(SingleSlot(master=self,title=title,loc=loc,slot=new_slot))
            self.gridSlot()
        except Exception as e:
            print("Error Message:",e)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # k.add_hotkey("ctrl + shift + 1", app.addSlot)