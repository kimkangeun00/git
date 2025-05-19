from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    key = "눌린 키 : "

    if event.state & 0x0001:
        key += "Shift + "

    if event.keycode == 37:
        key += "왼쪽 화살표"

    elif event.keycode == 38:
        key += "윗쪽 화살표"

    elif event.keycode == 39:
        key += "오른쪽 화살표"

    elif event.keycode == 40:
        key += "아래쪽 화살표"

    if key == "눌린 키 : ":
        return
    
    if key == "눌린 키 : Shift  ":
        pass

    messagebox.showinfo("키 이벤트", key)
    
window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()

    
    
