import psutil
import win32gui as wgui
import win32process as wproc
import win32api as wapi
import win32con as wcon
from time import sleep



class Slot:
    def __init__(self,isMain = False):
        self.win = wgui.GetForegroundWindow()
        self.thread,self.pid = wproc.GetWindowThreadProcessId(self.win)
        self.process = psutil.Process(self.pid)
        self.title = wgui.GetWindowText(self.win)
        self.state = False
        self.isMain = isMain

    def __eq__(self, other): 
        if not isinstance(other, Slot):
            return NotImplemented

        return self.__dict__ == other.__dict__

    def suspend(self):
        if self.isMain:
            print("This is Rexume running")
            return
        if self.state == True:
            print("Process already suspended")
            return
        try:
            self.process.suspend()
            print(f"Suspended Process: {self.name}")
        except Exception as e:
            print("Error when Trying to Suspend Process")
            return
        try:
            self.minimize()
            print(f"Minimized Process: {self.name}")
        except:
            print(f"Error when trying to minimize")
            return
        self.state = True
        
    def resume(self):
        if self.isMain:
            print("This is Rexume running")
            return
        if self.state == False:
            print("Process not suspended")
            return
        try:
            self.process.resume()
            print(f"Resumed Process: {self.name}")
        except Exception as e:
            print("Error when Trying to Resume Process")
            return
        try:
            self.unminimize()
            print(f"Minimized Process: {self.name}")
        except:
            print(f"Error when trying to un-minimize")
            return
        self.state = False
        
    def minimize(self):
        wgui.ShowWindow(self.win,wcon.SW_HIDE)
    
    def unminimize(self):
        wproc.AttachThreadInput(wapi.GetCurrentThreadId(), self.thread, True)
        wgui.ShowWindow(self.win,wcon.SW_SHOW)
        wgui.SetForegroundWindow(self.win)

class SlotList:
    def __init__(self,cap = 8):
        self.slots = [None for i in range(cap)]
        self.max_size = cap
        self.size = 0

    def add(self, slot=Slot(), sid = -1):
        if slot in self.slots:
            print("Slot present in list")
            return
        if self.size >= self.max_size:
            print("Slots capacity reached")
            return
        if sid == -1:
            for i in range(self.max_size):
                if not self.slots[i]:
                    sid = i
                    break
        elif sid not in range(self.max_size):
            print("Given slot ID not in range")
            return
        self.slots[sid] = slot
        self.size += 1
    
    def remove(self, sid = -1):
        if self.size <= 0:
            print("No slots being used")
            return
        if sid == -1:
            sid = self.size - 1
        elif sid not in range(self.max_size):
            print("Given slot ID not in range")
            return
        print("Removing slot, resuming slot process")
        slot = self.slots.pop(sid)
        slot.resume()



    pass
