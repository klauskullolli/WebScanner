import sys
import os
import tkinter
sys.path.append(os.path.abspath("."))

from tkinter import *
from tkinter import filedialog
from  webServices.configuration import  Configuration
def openFile(path: str):
    ws = Tk()
    ws.title("File Window")
    ws.geometry("700x700")
    ws['bg']='#708090'
    
    Label2 = tkinter.Label(ws)
    Label2.place(relx=0.1, rely=0.01, height=30, relwidth=0.1)
    Label2.configure(activebackground="#f9f9f9")
    Label2.configure(anchor='w')
    Label2.configure(background="#d9d9d9")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Arial} -size 13 -weight bold -slant italic -underline 1")
    Label2.configure(foreground="#4e58d6")
    Label2.configure(highlightbackground="#d9d9d9")
    Label2.configure(highlightcolor="black")
    Label2.configure(text='''Path:''')
    
    pathEntity = tkinter.Entry(ws)
    pathEntity.place(relx=0.3, rely=0.01, height=30, relwidth=0.6)
    pathEntity.configure(background="white")
    pathEntity.configure(disabledforeground="#a3a3a3")
    pathEntity.configure(font="TkFixedFont")
    pathEntity.configure(foreground="#000000")
    pathEntity.configure(highlightbackground="#d9d9d9")
    pathEntity.configure(highlightcolor="black")
    pathEntity.configure(insertbackground="black")
    pathEntity.configure(selectbackground="#c4c4c4")
    pathEntity.configure(selectforeground="black")
    
    txtarea = Text(ws , width=70, height=40)
    
    txtarea.place(relx=0.1, rely=0.07)
    file = open(path)  
    data = file.read()
    txtarea.insert(END, data)
    pathEntity.insert(END, path)
    file.close()
    
    ws.mainloop()
   

if __name__ == '__main__':
    openFile(Configuration.NLP_FILE)