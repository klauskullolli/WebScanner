#! /usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("."))

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from webServices.configuration import Configuration
from cache.redisCache import  RedisCache
from tkinter import messagebox
import webbrowser
import math 
from webServices.UrlMod import urlModifyer
from cache.webCacheStatus import  Status
import validators 

class SitesPage:
    def __init__(self, top: tk.Tk):
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

        top.geometry("970x645+150+80")
        top.minsize(116, 1)
        top.maxsize(1366, 746)
        top.resizable(False,  False)
        top.title("Sites")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.MainButt = tk.Button(self.top)
        self.MainButt.place(relx=0.0, rely=0.0, height=54, width=187)
        self.MainButt.configure(activebackground="beige")
        self.MainButt.configure(activeforeground="#000000")
        self.MainButt.configure(background="#877ed6")
        self.MainButt.configure(compound='left')
        self.MainButt.configure(disabledforeground="#a3a3a3")
        self.MainButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.MainButt.configure(foreground="#ffffff")
        self.MainButt.configure(highlightbackground="#d9d9d9")
        self.MainButt.configure(highlightcolor="black")
        self.MainButt.configure(pady="0")
        self.MainButt.configure(text='''Main Page''')
        self.MainButt.configure(command=self.mainButtAction)

        self.SitesButt = tk.Button(self.top)
        self.SitesButt.place(relx=0.262, rely=0.0, height=54, width=187)
        self.SitesButt.configure(activebackground="beige")
        self.SitesButt.configure(activeforeground="#000000")
        self.SitesButt.configure(background="#aaaaaa")
        self.SitesButt.configure(compound='left')
        self.SitesButt.configure(disabledforeground="#a3a3a3")
        self.SitesButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.SitesButt.configure(foreground="#ffffff")
        self.SitesButt.configure(highlightbackground="#d9d9d9")
        self.SitesButt.configure(highlightcolor="black")
        self.SitesButt.configure(pady="0")
        self.SitesButt.configure(text='''Sites''')

        self.StatisticsBut = tk.Button(self.top)
        self.StatisticsBut.place(relx=0.528, rely=0.0, height=54, width=177)
        self.StatisticsBut.configure(activebackground="beige")
        self.StatisticsBut.configure(activeforeground="#000000")
        self.StatisticsBut.configure(background="#877ed6")
        self.StatisticsBut.configure(compound='left')
        self.StatisticsBut.configure(disabledforeground="#a3a3a3")
        self.StatisticsBut.configure(font="-family {Arial} -size 14 -weight bold")
        self.StatisticsBut.configure(foreground="#ffffff")
        self.StatisticsBut.configure(highlightbackground="#d9d9d9")
        self.StatisticsBut.configure(highlightcolor="black")
        self.StatisticsBut.configure(pady="0")
        self.StatisticsBut.configure(text='''Statistics''')
        self.StatisticsBut.configure(command=self.statisticButtonAction)

        self.AdminButt = tk.Button(self.top)
        self.AdminButt.place(relx=0.772, rely=0.0, height=54, width=187)
        self.AdminButt.configure(activebackground="beige")
        self.AdminButt.configure(activeforeground="#000000")
        self.AdminButt.configure(background="#877ed6")
        self.AdminButt.configure(compound='left')
        self.AdminButt.configure(disabledforeground="#a3a3a3")
        self.AdminButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.AdminButt.configure(foreground="#ffffff")
        self.AdminButt.configure(highlightbackground="#d9d9d9")
        self.AdminButt.configure(highlightcolor="black")
        self.AdminButt.configure(pady="0")
        self.AdminButt.configure(text='''Edit Admin''')
        self.AdminButt.configure(command=self.adminButtonAction)


        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.133, rely=0.14, height=21, width=155)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 14 -weight bold -slant italic")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Excepted Site''')

        self.siteExceptEntry = tk.Entry(self.top)
        self.siteExceptEntry.place(relx=0.321, rely=0.13, height=30, relwidth=0.425)
        self.siteExceptEntry.configure(background="white")
        self.siteExceptEntry.configure(disabledforeground="#a3a3a3")
        self.siteExceptEntry.configure(font="TkFixedFont")
        self.siteExceptEntry.configure(foreground="#000000")
        self.siteExceptEntry.configure(highlightbackground="#d9d9d9")
        self.siteExceptEntry.configure(highlightcolor="black")
        self.siteExceptEntry.configure(insertbackground="black")
        self.siteExceptEntry.configure(selectbackground="#c4c4c4")
        self.siteExceptEntry.configure(selectforeground="black")

        self.addButt = tk.Button(self.top)
        self.addButt.place(relx=0.797, rely=0.12, height=40, width=87)
        self.addButt.configure(activebackground="beige")
        self.addButt.configure(activeforeground="#000000")
        self.addButt.configure(background="#68df53")
        self.addButt.configure(compound='left')
        self.addButt.configure(disabledforeground="#a3a3a3")
        self.addButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.addButt.configure(foreground="#ffffff")
        self.addButt.configure(highlightbackground="#d9d9d9")
        self.addButt.configure(highlightcolor="black")
        self.addButt.configure(pady="0")
        self.addButt.configure(text='''Add''')
        self.addButt.configure(command=self.addExceptionSite)
        
        
        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.133, rely=0.20, height=21, width=155)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 14 -weight bold -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Blocked Site''')
        
        self.siteBlockedEntry = tk.Entry(self.top)
        self.siteBlockedEntry.place(relx=0.321, rely=0.20, height=30, relwidth=0.425)
        self.siteBlockedEntry.configure(background="white")
        self.siteBlockedEntry.configure(disabledforeground="#a3a3a3")
        self.siteBlockedEntry.configure(font="TkFixedFont")
        self.siteBlockedEntry.configure(foreground="#000000")
        self.siteBlockedEntry.configure(highlightbackground="#d9d9d9")
        self.siteBlockedEntry.configure(highlightcolor="black")
        self.siteBlockedEntry.configure(insertbackground="black")
        self.siteBlockedEntry.configure(selectbackground="#c4c4c4")
        self.siteBlockedEntry.configure(selectforeground="black")
        
        self.addButt2 = tk.Button(self.top)
        self.addButt2.place(relx=0.797, rely=0.20, height=40, width=87)
        self.addButt2.configure(activebackground="beige")
        self.addButt2.configure(activeforeground="#000000")
        self.addButt2.configure(background="#68df53")
        self.addButt2.configure(compound='left')
        self.addButt2.configure(disabledforeground="#a3a3a3")
        self.addButt2.configure(font="-family {Arial} -size 14 -weight bold")
        self.addButt2.configure(foreground="#ffffff")
        self.addButt2.configure(highlightbackground="#d9d9d9")
        self.addButt2.configure(highlightcolor="black")
        self.addButt2.configure(pady="0")
        self.addButt2.configure(text='''Add''')
        self.addButt2.configure(command=self.addBlockedSite)

        self.offset = 10
        self.index = 0
        visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
        self.redisData = visitedCache.getAll()
        self.allKeys = visitedCache.getAllKeys()
        self.nrPages = math.ceil(len(self.allKeys)/float(self.offset))
        keyData = self.allKeys[0:self.offset]
        visitedCache.close()
        
        self.tableFrame = tk.Frame(self.top)
        self.tableFrame.place(relx=0.133, rely=0.37, relheight=0.53
                , relwidth=0.77)
        self.tableFrame.configure(relief='groove')
        self.tableFrame.configure(borderwidth="4")
        self.tableFrame.configure(relief="groove")
        self.tableFrame.configure(background="#d9d9d9")
        self.tableFrame.configure(highlightbackground="#d9d9d9")
        self.tableFrame.configure(highlightcolor="black")

        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        statusEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        actionEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        idEntry.grid(row=0,column=0, padx=(0,2))
        siteEntry.grid(row=0,column=1, padx=(0,2))
        statusEntry.grid(row=0,column=2 , padx=(0,2))
        actionEntry.grid(row=0,column=3, padx=(0,2))
        
        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        
        siteEntry.insert(END, "SITE")
        siteEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        statusEntry.insert(END, "STATUS")
        statusEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        actionEntry.insert(END, "ACTION")
        actionEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
       
        i = 1
        
        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            statusEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            updateButton = tk.Button(self.tableFrame, width=15,background="#6262ff",
                                     font="-family {Arial} -size 12 -weight bold -slant italic",
                                     foreground="#000000",highlightbackground="#d9d9d9", highlightcolor="black", 
                                     text="Update")
            idEntry.grid(row=i,column=0, padx=(0,2))
            siteEntry.grid(row=i,column=1, padx=(0,2))
            statusEntry.grid(row=i,column=2, padx=(0,2))
            updateButton.grid(row=i,column=3, padx=(0,2))
            
        
            
            idEntry.insert(END, f"{i}")
            idEntry.configure(state=DISABLED , disabledforeground='blue')
            
            siteEntry.insert(END, f"{key.decode()}")
            # siteEntry.configure(state=DISABLED , disabledforeground='blue')
            siteEntry.bind("<Double-Button-1>" , lambda event, site= key.decode() : self.siteEntryClick(event , site))
            statusEntry.insert(END, f"{self.redisData.get(key).decode()}")
            updateButton.configure(command=lambda a=i : self.update(a))
            
            i += 1
        
  

        self.findButt = tk.Button(self.top)
        self.findButt.place(relx=0.133, rely=0.29, height=34, width=87)
        self.findButt.configure(activebackground="beige")
        self.findButt.configure(activeforeground="#000000")
        self.findButt.configure(background="#6262ff")
        self.findButt.configure(compound='left')
        self.findButt.configure(disabledforeground="#a3a3a3")
        self.findButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.findButt.configure(foreground="#ffffff")
        self.findButt.configure(highlightbackground="#d9d9d9")
        self.findButt.configure(highlightcolor="black")
        self.findButt.configure(pady="0")
        self.findButt.configure(text='''Find''')
        self.findButt.configure(command=self.find)

        self.siteFindEntry = tk.Entry(self.top)
        self.siteFindEntry.place(relx=0.266, rely=0.29, height=30, relwidth=0.625)

        self.siteFindEntry.configure(background="white")
        self.siteFindEntry.configure(disabledforeground="#a3a3a3")
        self.siteFindEntry.configure(font="TkFixedFont")
        self.siteFindEntry.configure(foreground="#000000")
        self.siteFindEntry.configure(highlightbackground="#d9d9d9")
        self.siteFindEntry.configure(highlightcolor="black")
        self.siteFindEntry.configure(insertbackground="black")
        self.siteFindEntry.configure(selectbackground="#c4c4c4")
        self.siteFindEntry.configure(selectforeground="black")
        
        self.backButt = tk.Button(self.top)
        self.backButt.place(relx=0.332, rely=0.919, height=24, width=67)
        self.backButt.configure(activebackground="beige")
        self.backButt.configure(activeforeground="#000000")
        self.backButt.configure(background="#a2e2ea")
        self.backButt.configure(compound='left')
        self.backButt.configure(disabledforeground="#a3a3a3")
        self.backButt.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.backButt.configure(foreground="#000000")
        self.backButt.configure(highlightbackground="#d9d9d9")
        self.backButt.configure(highlightcolor="black")
        self.backButt.configure(pady="0")
        self.backButt.configure(text='''Back''')
        self.backButt.configure(command=self.back)
        if ( self.index ==0):
            self.backButt.configure(state=DISABLED)

        self.pageLabel = tk.Label(self.top)
        self.pageLabel.place(relx=0.45, rely=0.919, height=21, width=74)
        self.pageLabel.configure(activebackground="#f9f9f9")
        self.pageLabel.configure(anchor='w')
        self.pageLabel.configure(background="#d9d9d9")
        self.pageLabel.configure(compound='left')
        self.pageLabel.configure(disabledforeground="#a3a3a3")
        self.pageLabel.configure(font="-family {Segoe UI} -size 10")
        self.pageLabel.configure(foreground="#000000")
        self.pageLabel.configure(highlightbackground="#d9d9d9")
        self.pageLabel.configure(highlightcolor="black")
        self.pageLabel.configure(text=f'page {self.index + 1}')

        self.nextButt = tk.Button(self.top)
        self.nextButt.place(relx=0.55, rely=0.919, height=24, width=67)
        self.nextButt.configure(activebackground="beige")
        self.nextButt.configure(activeforeground="#000000")
        self.nextButt.configure(background="#a2e2ea")
        self.nextButt.configure(compound='left')
        self.nextButt.configure(disabledforeground="#a3a3a3")
        self.nextButt.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.nextButt.configure(foreground="#000000")
        self.nextButt.configure(highlightbackground="#d9d9d9")
        self.nextButt.configure(highlightcolor="black")
        self.nextButt.configure(pady="0")
        self.nextButt.configure(text='''Next''')
        self.nextButt.configure(command=self.next)
        
        if self.index >= self.nrPages-1:
            self.nextButt.configure(state=DISABLED)
        
        
        self.refreshButt = tk.Button(self.top)
        self.refreshButt.place(relx=0.8, rely=0.919, height=34, width=87)
        self.refreshButt.configure(activebackground="beige")
        self.refreshButt.configure(activeforeground="#000000")
        self.refreshButt.configure(background="#6262ff")
        self.refreshButt.configure(compound='left')
        self.refreshButt.configure(disabledforeground="#a3a3a3")
        self.refreshButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.refreshButt.configure(foreground="#ffffff")
        self.refreshButt.configure(highlightbackground="#d9d9d9")
        self.refreshButt.configure(highlightcolor="black")
        self.refreshButt.configure(pady="0")
        self.refreshButt.configure(text='''Refresh''')
        self.refreshButt.configure(command=self.refreshPage)


    def adminButtonAction(self):
        from FE.editAdmin import adminEdit
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = adminEdit(root)
        root.mainloop()
            
    def mainButtAction(self):
        from FE.mainPage import MainPage
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = MainPage(root)
        root.mainloop()
    
    def statisticButtonAction(self):
        from FE.statisticsPage import  StatisticsPage
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = StatisticsPage(root)
        root.mainloop()
    
    def refreshPage(self):
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = SitesPage(root)
        root.mainloop()
        
    def update(self, i):
        print(i)
        element = self.tableFrame.grid_slaves(i, 2)[0]
        website = self.tableFrame.grid_slaves(i, 1)[0].get()
        print(website)
        status  = element.get()
        if status.lower() in ["visited","blocked", "exception"]:
            visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
            visitedCache.add(website, status)
            visitedCache.close()
        else:
            messagebox.showerror("Error Message" ,"Status should be [\"visited\",\"blocked\", \"exception\"]")
            
    def siteEntryClick(self,event, site):
        webbrowser.open_new_tab(site)
    
    def _cleanFrame(self):
        for widget in self.tableFrame.winfo_children():
            widget.destroy()
    
    def next(self):
        self.index = self.index + 1
        start = self.index * self.offset 
        end = start + self.offset
        keyData = self.allKeys[start:end]
        self._cleanFrame()
        
        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        statusEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        actionEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        idEntry.grid(row=0,column=0, padx=(0,2))
        siteEntry.grid(row=0,column=1, padx=(0,2))
        statusEntry.grid(row=0,column=2 , padx=(0,2))
        actionEntry.grid(row=0,column=3, padx=(0,2))
        
        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        
        siteEntry.insert(END, "SITE")
        siteEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        statusEntry.insert(END, "STATUS")
        statusEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        actionEntry.insert(END, "ACTION")
        actionEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
       
        i = 1
        id = start + 1
        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            statusEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            updateButton = tk.Button(self.tableFrame, width=15,background="#6262ff",
                                     font="-family {Arial} -size 12 -weight bold -slant italic",
                                     foreground="#000000",highlightbackground="#d9d9d9", highlightcolor="black", 
                                     text="Update")
            idEntry.grid(row=i,column=0, padx=(0,2))
            siteEntry.grid(row=i,column=1, padx=(0,2))
            statusEntry.grid(row=i,column=2, padx=(0,2))
            updateButton.grid(row=i,column=3, padx=(0,2))
            
        
            
            idEntry.insert(END, f"{id}")
            idEntry.configure(state=DISABLED , disabledforeground='blue')
            
            siteEntry.insert(END, f"{key.decode()}")
            siteEntry.bind("<Double-Button-1>" , lambda event, site= key.decode() : self.siteEntryClick(event , site))
            statusEntry.insert(END, f"{self.redisData.get(key).decode()}")
            updateButton.configure(command=lambda a=i : self.update(a))
            
            i += 1
            id +=1 
        
        if self.index >= self.nrPages - 1:
            self.nextButt.configure(state=DISABLED)
        
        self.backButt.configure(state=NORMAL) 
        self.pageLabel.configure(text=f'page {self.index + 1}')
    
    def back(self):
        self.index = self.index - 1
        start = self.index * self.offset 
        end = start + self.offset
        keyData = self.allKeys[start:end]
        self._cleanFrame()
        
        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        statusEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        actionEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
        idEntry.grid(row=0,column=0, padx=(0,2))
        siteEntry.grid(row=0,column=1, padx=(0,2))
        statusEntry.grid(row=0,column=2 , padx=(0,2))
        actionEntry.grid(row=0,column=3, padx=(0,2))
        
        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        
        siteEntry.insert(END, "SITE")
        siteEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        statusEntry.insert(END, "STATUS")
        statusEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
        actionEntry.insert(END, "ACTION")
        actionEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
       
        i = 1
        id = start + 1
        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            statusEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            updateButton = tk.Button(self.tableFrame, width=15,background="#6262ff",
                                     font="-family {Arial} -size 12 -weight bold -slant italic",
                                     foreground="#000000",highlightbackground="#d9d9d9", highlightcolor="black", 
                                     text="Update")
            idEntry.grid(row=i,column=0, padx=(0,2))
            siteEntry.grid(row=i,column=1, padx=(0,2))
            statusEntry.grid(row=i,column=2, padx=(0,2))
            updateButton.grid(row=i,column=3, padx=(0,2))
            
        
            
            idEntry.insert(END, f"{id}")
            idEntry.configure(state=DISABLED , disabledforeground='blue')
            
            siteEntry.insert(END, f"{key.decode()}")
            siteEntry.bind("<Double-Button-1>" , lambda event, site= key.decode() : self.siteEntryClick(event , site))
            statusEntry.insert(END, f"{self.redisData.get(key).decode()}")
            updateButton.configure(command=lambda a=i : self.update(a))
            
            i += 1
            id +=1 
        
        if self.index == 0:
            self.backButt.configure(state=DISABLED)
        
        self.nextButt.configure(state=NORMAL)
        self.pageLabel.configure(text=f'page {self.index + 1}') 
    
    
    def find(self):
        site = self.siteFindEntry.get()
        if site is None or site == "":
            messagebox.showerror("Error message", "Entry is empty")
        else:
            sitesDict = {}
            contain = False
            
            for i in range(0, len(self.allKeys)):
                val =  self.allKeys[i].decode()
                if site in  val:
                    sitesDict[i+1] = val
                    contain = True            
            
            if contain:
                    
                self._cleanFrame()
                
                idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                            font=('Arial', 16, 'bold'))
                siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                            font=('Arial', 16, 'bold'))
                statusEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                            font=('Arial', 16, 'bold'))
                actionEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue',fg='Black',
                                            font=('Arial', 16, 'bold'))
                idEntry.grid(row=0,column=0, padx=(0,2))
                siteEntry.grid(row=0,column=1, padx=(0,2))
                statusEntry.grid(row=0,column=2 , padx=(0,2))
                actionEntry.grid(row=0,column=3, padx=(0,2))
                
                idEntry.insert(END, "ID")
                idEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
                
                siteEntry.insert(END, "SITE")
                siteEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
                statusEntry.insert(END, "STATUS")
                statusEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
                actionEntry.insert(END, "ACTION")
                actionEntry.configure(state=DISABLED , disabledforeground='Black', disabledbackground='LightSteelBlue')
                
                i = 1
                for id in sitesDict.keys():
                    idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))
                    siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))
                    statusEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))
                    updateButton = tk.Button(self.tableFrame, width=15,background="#6262ff",
                                            font="-family {Arial} -size 12 -weight bold -slant italic",
                                            foreground="#000000",highlightbackground="#d9d9d9", highlightcolor="black", 
                                            text="Update")
                    idEntry.grid(row=i,column=0, padx=(0,2))
                    siteEntry.grid(row=i,column=1, padx=(0,2))
                    statusEntry.grid(row=i,column=2, padx=(0,2))
                    updateButton.grid(row=i,column=3, padx=(0,2))
                    
                    siteName = sitesDict[id]
                    
                    idEntry.insert(END, f"{id}")
                    idEntry.configure(state=DISABLED , disabledforeground='blue')
                    
                    siteEntry.insert(END, f"{siteName}")
                    siteEntry.bind("<Double-Button-1>" , lambda event, site= siteName: self.siteEntryClick(event , site))
                    statusEntry.insert(END, f"{self.redisData.get(siteName.encode()).decode()}")
                    updateButton.configure(command=lambda a=i : self.update(a))
                    
                    i += 1
                    
                self.pageLabel.configure(text=f'page --') 
            
            else:
                messagebox.showerror("Error message", "This site does not exist in table")
               
    def addExceptionSite(self):
        site = self.siteExceptEntry.get()
        if site is None or site == "":
            messagebox.showerror("Error message", "Entry is empty")
        else:
            
            if validators.url(site):
                urlmod = urlModifyer(site)
                visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
                print(urlmod.getBaseUrl())
                baseURL = urlmod.getBaseUrl()
                visitedCache.add(baseURL, Status.EXCEPTION)
                visitedCache.close()
                self.siteExceptEntry.delete(0, END)
                pass
            else:
                messagebox.showerror("Error message", "This website is not valid or type the entire website correctly")
                
    def addBlockedSite(self):
        site = self.siteBlockedEntry.get()
        if site is None or site == "":
            messagebox.showerror("Error message", "Entry is empty")
        else:
            
            if validators.url(site):
                urlmod = urlModifyer(site)
                visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
                print(urlmod.getBaseUrl())
                baseURL = urlmod.getBaseUrl()
                visitedCache.add(baseURL, Status.BLOCKED)
                visitedCache.close()
                self.siteBlockedEntry.delete(0, END)
                pass
            else:
                messagebox.showerror("Error message", "This website is not valid or type the entire website correctly")        
        

if __name__ == '__main__':
    root = tk.Tk()    
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    _configWindow = SitesPage(root)
    root.mainloop()
    pass





