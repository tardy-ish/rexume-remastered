import keyboard as k
from backend import Slot, SlotList
from pprint import pprint
from time import sleep
import sys

rexume = Slot(isMain=True)
pprint(rexume.__dict__)
slotMeUp = SlotList(rexume)
reelLife = [False]


def addSus():
    slotMeUp.add()


def susOn():
    slotMeUp.suspend()


def resOn():
    slotMeUp.resume()


def endProg():
    for slot in slotMeUp.slots:
        if slot:
            slot.resume()
    reelLife[0] = True


k.add_hotkey("ctrl+alt+k", lambda: addSus())
k.add_hotkey("ctrl+alt+p", lambda: susOn())
k.add_hotkey("ctrl+alt+r", lambda: resOn())
k.add_hotkey("ctrl+alt+[", lambda: endProg())

print("It's running")
print()
while 1:
    sleep(0.1)
    if reelLife[0]:
        break
