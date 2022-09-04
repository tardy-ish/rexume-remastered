import psutil

class WindowManager:
    def __init__(self):
        
        pass

class Slot:
    def __init__(self,pid,slotID,name):
        self.process = psutil.Process(pid)
        self.slotID = slotID
        self.name = name
        self.state = False

    def changeID(self,slotID):
        self.slotID = slotID

    def suspend(self):
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
        

