from asyncio import streams
import sys
import os
sys.path.append(os.path.abspath("."))

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import  time
from tkinter import messagebox

from webServices.configuration import Configuration
import yaml

 
class ConfigPanel:
    def __init__(self, top:tk.Tk):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = 'gray40' # X11 color: #666666
            _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
            _ana2color = 'beige' # X11 color: #f5f5dc
            _tabfg1 = 'black' 
            _tabfg2 = 'black' 
            _tabbg1 = 'grey75' 
            _tabbg2 = 'grey89' 
            _bgmode = 'light' 
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.map('.',background=
                [('selected', _compcolor), ('active',_ana2color)])
    
            top.geometry("600x346+383+106")
            top.minsize(116, 1)
            top.maxsize(1366, 746)
            top.resizable(1,  1)
            top.title("Configuration")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")
    
            self.top = top
    
            self.Frame1 = tk.Frame(self.top)
            self.Frame1.place(relx=0.067, rely=0.116, relheight=0.766
                    , relwidth=0.892)
            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#5072fa")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")
    
            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.168, rely=0.189, height=31, width=344)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(anchor='s')
            self.Label1.configure(background="#5072fa")
            self.Label1.configure(compound='center')
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Arial} -size 16 -weight bold")
            self.Label1.configure(foreground="#ffffff")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''CONFIGURATION''')

            self.PBar= ttk.Progressbar(self.Frame1)
            self.PBar.place(relx=0.112, rely=0.453, relwidth=0.748
                , relheight=0.0, height=22)
            self.PBar.configure(length="400")
            # self.PBar.start(10)
            self.top.after(1000, lambda: self.progressAction())
            
    
    def progressAction(self):
            if  self.PBar["value"] < 100:
                self.PBar["value"] += 10
                self.top.after(1000, lambda: self.progressAction())
            else:
                conf = Configuration()
                conf.createConfigDirsAndFiles()
                # conf.updateDockerFile()
                self.Label2 =tk.Label(self.Frame1)
                self.Label2.place(relx=0.112, rely=0.573, relwidth=0.748
                , relheight=0.0, height=22)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(anchor='s')
                self.Label2.configure(background="#5072fa")
                self.Label2.configure(compound='center')
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Arial} -size 12 -weight bold")
                self.Label2.configure(foreground="#ffffff")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2["text"] = "Proccess finished"
                time.sleep(1)
                res = messagebox.askquestion("Confirm", "Want to continue?")
                if res =="yes":
                    
                    stream = open(Configuration.CONFIG_RESOURCES, "r")
                    loadData = yaml.safe_load(stream)
                    stream.close()
                    
                    loadData["config"] = True
                    
                    stream = open(Configuration.CONFIG_RESOURCES, "w")
                    stream.write(yaml.dump(loadData))
                    stream.close()
                    
                    from  FE.login import LogInPage
                    self.top.destroy()
                    root = tk.Tk()
                    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
                    _configWindow = LogInPage(root)
                    root.mainloop()
                    
                else:
                    self.top.destroy()
    

def start():
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    _configWindow = ConfigPanel(root)
    root.mainloop()    
                


if __name__ == '__main__':
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    _configWindow = ConfigPanel(root)
    root.mainloop()
    pass
    
   
