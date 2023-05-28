import psutil
import win32gui as wgui
import win32process as wproc
import win32api as wapi
import win32con as wcon


class Slot:
    def __init__(self, isMain=False):
        self.win = wgui.GetForegroundWindow()
        self.thread, self.pid = wproc.GetWindowThreadProcessId(self.win)
        self.process = psutil.Process(self.pid)
        self.exeLoc = self.process.exe()
        self.title = wgui.GetWindowText(self.win)
        self.state = False
        self.isMain = isMain

    def __eq__(self, other):
        if not isinstance(other, Slot):
            return NotImplemented
        return self.process == other.process

    def suspend(self):
        if self.isMain:
            print("This is Rexume running")
            return False
        if self.state == True:
            print("Process already suspended")
            return False
        try:
            self.process.suspend()
            print(f"Suspended Process: {self.title}")
        except Exception as e:
            print("Error when Trying to Suspend Process", e)
            return False
        try:
            self.minimize()
            print(f"Minimized Process: {self.title}")
        except Exception as e:
            print(f"Error when trying to minimize", e)
            return False
        self.state = True

    def resume(self):
        if self.isMain:
            print("This is Rexume running")
            return False
        if self.state == False:
            print("Process not suspended")
            return False
        try:
            self.process.resume()
            print(f"Resumed Process: {self.title}")
        except Exception as e:
            print("Error when Trying to Resume Process",e)
            return False
        try:
            self.unminimize()
            print(f"Minimized Process: {self.title}")
        except Exception as e:
            print(f"Error when trying to un-minimize",e)
            return False
        self.state = False

    def minimize(self):
        try:
            wgui.ShowWindow(self.win, wcon.SW_HIDE)
        except Exception as e:
            raise Exception("Error while trying to Minimize")

    def unminimize(self):
        try:
            wproc.AttachThreadInput(wapi.GetCurrentThreadId(), self.thread, True)
            wgui.ShowWindow(self.win, wcon.SW_SHOW)
            wgui.SetForegroundWindow(self.win)
        except Exception as e:
            raise Exception("Error while trying to un-Minimize")

    def give(self):
        return self.title,self.exeLoc


class SlotList:
    def __init__(self, rexume, cap=8):
        self.slots = [None for i in range(cap)]
        self.max_size = cap
        self.size = 0
        self.recentStack = []
        self.rexume = rexume

    def mostRecentSlot(self):
        if len(self.recentStack) == 0:
            print("Stack is empty")
            return False
        sid = self.recentStack[-1]
        return self.slots[sid]

    def add(self, slot=None, sid=-1):
        slot = Slot()
        # pprint(slot.__dict__)
        if slot == self.rexume:
            print("This is Rexume running")
            return False

        if slot in self.slots:
            print("Process present in slots")
            return False

        if self.size >= self.max_size:
            print("Slots capacity reached")
            return False

        if sid == -1:
            for i in range(self.max_size):
                if not self.slots[i]:
                    sid = i
                    break

        elif sid not in range(self.max_size):
            print("Given slot ID not in range")
            return False

        self.slots[sid] = slot
        self.recentStack.append(sid)
        self.size += 1
        return True

    def remove(self, sid=-1):
        if self.size <= 0:
            print("No slots being used")
            return False
        if sid == -1:
            sid = self.recent[-1]
        elif sid not in range(self.max_size):
            print("Given slot ID not in range")
            return False
        elif not self.slots[sid]:
            print("Slot is already empty")
            return False
        print("Removing slot, resuming process saved in slot")
        slot = self.slots[sid]
        slot.resume()
        self.slots[sid] = None
        self.recentStack.pop()
        self.size -= 1

    def suspend(self, sid=-1):
        if sid == -1:
            if self.add():
                sid = self.recentStack[-1]
            else:
                print("Could not add slot")
                return False
        elif sid not in range(self.max_size):
            print("ID not in range")
            return False
        slot = self.slots[sid]
        if not slot:
            print("Slot is empty")
            return False

        slot.suspend()
        return True

    def resume(self, sid=-1):
        if sid == -1:
            if self.size <= 0:
                print("All slots are empty")
                return False
            else:
                sid = self.recentStack[-1]
        elif sid not in range(self.max_size):
            print("ID not in range")
            return False

        slot = self.slots[sid]
        if not slot:
            print("Slot is empty")
            return False
        if self.rexume == slot:
            print("This is Rexume running")
            return False
        slot.resume()
        return True
