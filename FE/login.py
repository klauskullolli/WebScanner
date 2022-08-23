#! /usr/bin/env python

from mailbox import linesep
import sys
import os
import yaml


sys.path.append(os.path.abspath("."))

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import base64
from  webServices.configuration import Configuration


import FE.login_support as login_support
from  FE.configPage import  ConfigPanel

class LogInPage:
    def __init__(self, top=None):
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

        top.geometry("600x450+290+166")
        top.minsize(116, 1)
        top.maxsize(1366, 746)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
    

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.083, rely=0.089, relheight=0.789
                , relwidth=0.842)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#3333ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.396, rely=0.028, height=56, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#3333ff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 18 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''LOGIN''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.059, rely=0.282, height=56, width=114)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#3333ff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 16 -weight bold -slant italic -underline 1")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.059, rely=0.451, height=56, width=114)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#3333ff")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Arial} -size 16 -weight bold -slant italic -underline 1")
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password''')

        self.usernameEntity = tk.Entry(self.Frame1)
        self.usernameEntity.place(relx=0.356, rely=0.31, height=30
                , relwidth=0.404)
        self.usernameEntity.configure(background="white")
        self.usernameEntity.configure(disabledforeground="#a3a3a3")
        self.usernameEntity.configure(font="TkFixedFont")
        self.usernameEntity.configure(foreground="#000000")
        self.usernameEntity.configure(highlightbackground="#d9d9d9")
        self.usernameEntity.configure(highlightcolor="black")
        self.usernameEntity.configure(insertbackground="black")
        self.usernameEntity.configure(selectbackground="#c4c4c4")
        self.usernameEntity.configure(selectforeground="black")

        self.passEntity = tk.Entry(self.Frame1)
        self.passEntity.place(relx=0.356, rely=0.479, height=30, relwidth=0.404)
        self.passEntity.configure(background="white")
        self.passEntity.configure(disabledforeground="#a3a3a3")
        self.passEntity.configure(font="TkFixedFont")
        self.passEntity.configure(foreground="#000000")
        self.passEntity.configure(highlightbackground="#d9d9d9")
        self.passEntity.configure(highlightcolor="black")
        self.passEntity.configure(insertbackground="black")
        self.passEntity.configure(selectbackground="#c4c4c4")
        self.passEntity.configure(selectforeground="black")
        self.passEntity.configure(show="*")


        self.var = tk.IntVar()
        self.Checkbutton1 = tk.Checkbutton(self.Frame1 , variable=self.var)
        self.Checkbutton1.place(relx=0.356, rely=0.592, relheight=0.07
                , relwidth=0.2)
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#3333ff")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 12")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(selectcolor="#d9d9d9")
        self.Checkbutton1.configure(text='''Visible''')
        # self.Checkbutton1.configure(variable=self.che55)
        self.Checkbutton1.configure(command=self.checkButtClicked)
        

        self.loginBut = tk.Button(self.Frame1)
        self.loginBut.place(relx=0.356, rely=0.761, height=34, width=127)
        self.loginBut.configure(activebackground="beige")
        self.loginBut.configure(activeforeground="#000000")
        self.loginBut.configure(background="#00d500")
        self.loginBut.configure(compound='left')
        self.loginBut.configure(disabledforeground="#a3a3a3")
        self.loginBut.configure(font="-family {Arial} -size 16 -weight bold")
        self.loginBut.configure(foreground="#000000")
        self.loginBut.configure(highlightbackground="#d9d9d9")
        self.loginBut.configure(highlightcolor="black")
        self.loginBut.configure(pady="0")
        self.loginBut.configure(text='''Log In''')
        self.loginBut.configure(command=self.login)
        
        
    def checkButtClicked(self):
            if self.passEntity.cget("show") == "*":
                self.passEntity.configure(show="")
            else:
                self.passEntity.configure(show="*")
                
                
    def login(self):
        f = open(Configuration.LOGIN_CREDENTIALS)
        lines = f.readlines()
        f.close()
        
        username = base64.b64encode(self.usernameEntity.get().encode("utf-8")).decode().strip()
        password = base64.b64encode(self.passEntity.get().encode("utf-8")).decode().strip()
        print(lines[0])
        print(lines[1])
        if username==lines[0].strip() and password==lines[1].strip():
            self.top.destroy()
            from  FE.mainPage import MainPage
            root = tk.Tk()
            root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
            _configWindow = MainPage(root)
            root.mainloop()
                 

def start_up():
    login_support.main()

if __name__ == '__main__':
    login_support.main()
    
    
    




