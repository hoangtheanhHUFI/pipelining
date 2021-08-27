from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
window = Tk()
window.title("Pipelining ")
window.geometry("1920x1080")
# thêm label 
lbl =tkinter.Label(window , text= 'Phần mềm mới chế ', fg="green" , font=("Arial",100))
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
combo = Combobox(window)
combo['values'] = ("Cường Thuận", "Thế Anh ", "Tâm Đoàn", " Phước Nhân")
combo.grid(column=0 , row=2)
def handlebutton1():
    lbl.configure(text= 'chào, ' + combo.get() + ' đẹp trai')
    #messagebox.showinfo = (" Ai là người đẹp trai ", "Chào" + combo.get())
    return
# thêm button
btnHello1 = Button (window,text= "Chọn ", command=handlebutton1)
btnHello1.grid(column= 1,row= 2)

window.mainloop()
