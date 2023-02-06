import CustomTkinter as ctk

class slot_view:
    def __init__(self,mFrame) -> None:
        frame = ctk.CTkFrame(master = mFrame)
        frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)