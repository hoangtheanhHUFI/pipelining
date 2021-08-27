from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from funtion import math
window = Tk()
window.title("Pipelining ")
window.geometry("400x300")
 #thêm label 
lbl =tkinter.Label(window , text= 'Phần mềm mới chế ', fg="green" , font=("Arial",30))
lbl.grid(column = 0 , row = 0 )
 #thêm textbox
txt = Entry(window, width = 20)
txt.grid(column=0,row= 1)

def handlebutton():
    lbl.configure(text= 'chào, ' + txt.get() + ' đẹp trai')
    return
 #thêm button
btnHello = Button (window,text= "say hello", command=handlebutton)
btnHello.grid(column= 1,row= 1)
 #thêm combobox
combo = Combobox(window)
combo['values'] = ("Cường Thuận", "Thế Anh ", "Tâm Đoàn", " Phước Nhân")
combo.grid(column=0 , row=2)
def bubuoi():
 
   messagebox.showinfo('Ai đẹp trai nhất', 'Người đó là : ' + combo.get())
 
btn = Button(window,text='Click here', command=bubuoi)
 
btn.grid(column=1,row=2)
def clicked():
    bt = math.concho()
    messagebox.showinfo('Message title',bt)
 
btn = Button(window,text='hiện ra đi ', command=clicked)
 
btn.grid(column=2,row=3)

window.mainloop()
#from tkinter import *
 
#from tkinter import messagebox
 
#window = Tk()
 
#window.title("Welcome to LikeGeeks app")
 
#window.geometry('350x200')
 
#def clicked():
 
#    messagebox.showinfo('Message title', 'Message content')
 
#btn = Button(window,text='Click here', command=clicked)
 
#btn.grid(column=0,row=0)
 
#window.mainloop()
