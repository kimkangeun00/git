from tkinter import *

fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif"]
photoList = [None] * 8
num = 0

def clickNext():
    global num
    num +=1
    if num > 8:
        num = 0
    photo = PhotoImage(file="SelfStudy10-3/" + fnameList[num])
    label.config(image=photo)
    label.image = photo
    namelabel.config (text=fnameList[num])

def clickPrev():
    global num
    num -=1
    if num < 0:
        num = 8
    photo = PhotoImage(file="SelfStudy10-3/" + fnameList[num])
    label.config(image=photo)
    label.image = photo
    namelabel.config (text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="이전", command=clickPrev)
btnNext = Button(window, text="다음", command=clickNext)

photo = PhotoImage(file="SelfStudy10-3/" + fnameList[0])
label = Label(window, image=photo)
namelabel = Label(window, text=fnameList[0])

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=15)
label.place(x=15, y=50)
namelabel.place(x=330, y=15)

window.mainloop()