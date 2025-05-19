from tkinter import *
from random import *

window = Tk()
window.geometry("810x810")


btnList = [None] * 9
fnameList = ["SelfStudy10-2\\1.gif", "SelfStudy10-2\\2.gif", "SelfStudy10-2\\3.gif", "SelfStudy10-2\\4.gif", "SelfStudy10-2\\5.gif", "SelfStudy10-2\\6.gif", "SelfStudy10-2\\7.gif", "SelfStudy10-2\\8.gif", "SelfStudy10-2\\9.gif"]

photoList = [PhotoImage(file=fnameList[i]) for i in range(9)]
shuffle(photoList)

i, k = 0, 0
xPos, yPos = 0, 0
num = 0

for i in range(0,3):
    for k in range(0,3):
        btnList[num] = Button(window, image=photoList[num], width=270, height=270)
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 270
    xPos = 0
    yPos += 270

window.mainloop()
