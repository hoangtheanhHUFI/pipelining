
from tkinter import *
import funtion 
root = Tk()
root.geometry("400x300")
root.title(" KỸ THUẬT PIPELINING ")
  
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.insert(END, funtion.step_by_step(float(INPUT)))
    Output.insert(END, funtion.pipelining(float(INPUT)))
      
l = Label(text = " Nhập số lệnh ")
inputtxt = Text(root, height = 1,
                width = 15)
                
  
Output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")
  
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())
  
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
  
mainloop()

