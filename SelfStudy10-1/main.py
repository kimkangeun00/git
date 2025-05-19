from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:SelfStudy10-1\\cat1.gif")
label1 = Label(window, image = photo1)
label1.pack(side=LEFT)

photo2 = PhotoImage(file = "C:SelfStudy10-1\\cat2.gif")
label2 = Label(window, image = photo2)
label2.pack(side=LEFT)

window.mainloop()