from tkinter import *
import tkinter

window = Tk()
window.title("Pipelining ")
window.geometry("1920x1080")
# thêm label 
lbl = Label(window , text= 'Phần mềm mới chế ', fg="green" , font=("Arial",100))
lbl.grid(column = 0 , row = 0 )
# thêm textbox
txt = Entry(window, width = 20)
txt.grid(column=0,row= 1)

def handlebutton():
    lbl.configure(text= 'chào, ' + txt.get() + ' đẹp trai')
    return
# thêm button
btnHello = Button (window,text= "say hello", command=handlebutton)
btnHello.grid(column= 1,row= 1)
# thêm combobox
combo = combobox(window)


window.mainloop()