import tkinter
from tkinter import ttk
from tkinter import messagebox

form=tkinter.Tk()
form.geometry("700x500")

btns = ttk.Style()
btns.configure("TButton" ,font =("tahoma",30),padding =10)
def mbox():
    messagebox.showerror("error","this is error")


btn =ttk.Button(form,text ="show message",command = mbox)
btn.pack()
               
 
