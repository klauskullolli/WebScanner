#! /usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("."))

import FE.fileOpen as fileOpen
from tkinter import messagebox
import webbrowser
import math
from cache.redisCache import RedisCache
from webServices.configuration import Configuration
from tkinter.constants import *
import tkinter.ttk as ttk
import tkinter as tk
from multiprocessing import set_forkserver_preload

import matplotlib.pyplot as plt
from webServices.UrlMod import urlModifyer 


class StatisticsPage:
    def __init__(self, top=tk.Tk):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40'  # X11 color: #666666
        _ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
        _ana2color = 'beige'  # X11 color: #f5f5dc
        _tabfg1 = 'black'
        _tabfg2 = 'black'
        _tabbg1 = 'grey75'
        _tabbg2 = 'grey89'
        _bgmode = 'light'

        top.geometry("903x642+133+144")
        # top.minsize(116, 1)
        # top.maxsize(1366, 746)
        top.resizable(FALSE,  False)
        top.title("Statistics")
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
        self.SitesButt.configure(background="#877ed6")
        self.SitesButt.configure(compound='left')
        self.SitesButt.configure(disabledforeground="#a3a3a3")
        self.SitesButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.SitesButt.configure(foreground="#ffffff")
        self.SitesButt.configure(highlightbackground="#d9d9d9")
        self.SitesButt.configure(highlightcolor="black")
        self.SitesButt.configure(pady="0")
        self.SitesButt.configure(text='''Sites''')
        self.SitesButt.configure(command=self.sitesButtonAction)

        self.StatisticsBut = tk.Button(self.top)
        self.StatisticsBut.place(relx=0.543, rely=0.0, height=54, width=177)
        self.StatisticsBut.configure(activebackground="beige")
        self.StatisticsBut.configure(activeforeground="#000000")
        self.StatisticsBut.configure(background="#aaaaaa")
        self.StatisticsBut.configure(compound='left')
        self.StatisticsBut.configure(disabledforeground="#a3a3a3")
        self.StatisticsBut.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.StatisticsBut.configure(foreground="#ffffff")
        self.StatisticsBut.configure(highlightbackground="#d9d9d9")
        self.StatisticsBut.configure(highlightcolor="black")
        self.StatisticsBut.configure(pady="0")
        self.StatisticsBut.configure(text='''Statistics''')

        self.AdminButt = tk.Button(self.top)
        self.AdminButt.place(relx=0.797, rely=0.0, height=54, width=187)
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

        self.offset = 12
        self.index = 0
        statisticsCache = RedisCache(
            "statistics", host="localhost", port=Configuration.REDIS_PORT)
        self.redisData = statisticsCache.getAll()
        self.allKeys = statisticsCache.getAllKeys()
        self.nrPages = math.ceil(len(self.allKeys)/float(self.offset))
        keyData = self.allKeys[0:self.offset]
        statisticsCache.close()

        self.tableFrame = tk.Frame(self.top)
        self.tableFrame.place(relx=0.044, rely=0.23,
                              relheight=0.65, relwidth=0.625)
        self.tableFrame.configure(relief='groove')
        self.tableFrame.configure(borderwidth="4")
        self.tableFrame.configure(relief="groove")
        self.tableFrame.configure(background="#d9d9d9")
        self.tableFrame.configure(highlightbackground="#d9d9d9")
        self.tableFrame.configure(highlightcolor="black")

        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                           font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                             font=('Arial', 16, 'bold'))
        nrTimesEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                font=('Arial', 16, 'bold'))

        idEntry.grid(row=0, column=0, padx=(0, 2))
        siteEntry.grid(row=0, column=1, padx=(0, 2))
        nrTimesEntry.grid(row=0, column=2, padx=(0, 2))

        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED, disabledforeground='Black',
                          disabledbackground='LightSteelBlue')

        siteEntry.insert(END, "SITE")
        siteEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')
        nrTimesEntry.insert(END, "TIME VISITED")
        nrTimesEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')

        i = 1

        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                 font=('Arial', 16, ''))
            nrTimesEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))

            idEntry.grid(row=i, column=0, padx=(0, 2))
            siteEntry.grid(row=i, column=1, padx=(0, 2))
            nrTimesEntry.grid(row=i, column=2, padx=(0, 2))

            idEntry.insert(END, f"{i}")
            idEntry.configure(state=DISABLED, disabledforeground='blue')

            siteEntry.insert(END, f"{key.decode()}")
            # siteEntry.configure(state=DISABLED , disabledforeground='blue')
            siteEntry.bind("<Double-Button-1>", lambda event,
                           site=key.decode(): self.siteEntryClick(event, site))
            nrTimesEntry.insert(END, f"{self.redisData.get(key).decode()}")

            i += 1

        self.findButt = tk.Button(self.top)
        self.findButt.place(relx=0.044, rely=0.15, height=34, width=87)
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
        self.siteFindEntry.place(
            relx=0.166, rely=0.15, height=30, relwidth=0.47)
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
        self.backButt.place(relx=0.155, rely=0.92, height=24, width=67)
        self.backButt.configure(activebackground="beige")
        self.backButt.configure(activeforeground="#000000")
        self.backButt.configure(background="#a2e2ea")
        self.backButt.configure(compound='left')
        self.backButt.configure(disabledforeground="#a3a3a3")
        self.backButt.configure(
            font="-family {Segoe UI} -size 10 -weight bold")
        self.backButt.configure(foreground="#000000")
        self.backButt.configure(highlightbackground="#d9d9d9")
        self.backButt.configure(highlightcolor="black")
        self.backButt.configure(pady="0")
        self.backButt.configure(text='''Back''')
        self.backButt.configure(command=self.back)

        if (self.index == 0):
            self.backButt.configure(state=DISABLED)

        self.pageLabel = tk.Label(self.top)
        self.pageLabel.place(relx=0.277, rely=0.92, height=21, width=74)
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
        self.nextButt.place(relx=0.377, rely=0.92, height=24, width=67)
        self.nextButt.configure(activebackground="beige")
        self.nextButt.configure(activeforeground="#000000")
        self.nextButt.configure(background="#a2e2ea")
        self.nextButt.configure(compound='left')
        self.nextButt.configure(disabledforeground="#a3a3a3")
        self.nextButt.configure(
            font="-family {Segoe UI} -size 10 -weight bold")
        self.nextButt.configure(foreground="#000000")
        self.nextButt.configure(highlightbackground="#d9d9d9")
        self.nextButt.configure(highlightcolor="black")
        self.nextButt.configure(pady="0")
        self.nextButt.configure(text='''Next''')
        self.nextButt.configure(command=self.next)

        if self.index >= self.nrPages-1:
            self.nextButt.configure(state=DISABLED)

        self.keyLoggButt = tk.Button(self.top)
        self.keyLoggButt.place(relx=0.797, rely=0.187, height=54, width=187)
        self.keyLoggButt.configure(activebackground="beige")
        self.keyLoggButt.configure(activeforeground="#000000")
        self.keyLoggButt.configure(background="#a3d773")
        self.keyLoggButt.configure(compound='left')
        self.keyLoggButt.configure(disabledforeground="#a3a3a3")
        self.keyLoggButt.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.keyLoggButt.configure(foreground="#ffffff")
        self.keyLoggButt.configure(highlightbackground="#d9d9d9")
        self.keyLoggButt.configure(highlightcolor="black")
        self.keyLoggButt.configure(pady="0")
        self.keyLoggButt.configure(text='''Key Loggs''')
        self.keyLoggButt.configure(command=self.openKeyLoggFile)

        self.similarSearchButt = tk.Button(self.top)
        self.similarSearchButt.place(
            relx=0.797, rely=0.312, height=54, width=187)
        self.similarSearchButt.configure(activebackground="beige")
        self.similarSearchButt.configure(activeforeground="#000000")
        self.similarSearchButt.configure(background="#a3d773")
        self.similarSearchButt.configure(compound='left')
        self.similarSearchButt.configure(disabledforeground="#a3a3a3")
        self.similarSearchButt.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.similarSearchButt.configure(foreground="#ffffff")
        self.similarSearchButt.configure(highlightbackground="#d9d9d9")
        self.similarSearchButt.configure(highlightcolor="black")
        self.similarSearchButt.configure(pady="0")
        self.similarSearchButt.configure(text='''Similar Search''')
        self.similarSearchButt.configure(command=self.openSimilarSearchFile)

        self.mproxyLoggButt = tk.Button(self.top)
        self.mproxyLoggButt.place(relx=0.797, rely=0.436, height=54, width=187)
        self.mproxyLoggButt.configure(activebackground="beige")
        self.mproxyLoggButt.configure(activeforeground="#000000")
        self.mproxyLoggButt.configure(background="#a3d773")
        self.mproxyLoggButt.configure(compound='left')
        self.mproxyLoggButt.configure(disabledforeground="#a3a3a3")
        self.mproxyLoggButt.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.mproxyLoggButt.configure(foreground="#ffffff")
        self.mproxyLoggButt.configure(highlightbackground="#d9d9d9")
        self.mproxyLoggButt.configure(highlightcolor="black")
        self.mproxyLoggButt.configure(pady="0")
        self.mproxyLoggButt.configure(text='''Mproxy Loggs''')
        self.mproxyLoggButt.configure(command=self.openMproxyLoggFile)

        self.webScanButt = tk.Button(self.top)
        self.webScanButt.place(relx=0.797, rely=0.561, height=54, width=187)
        self.webScanButt.configure(activebackground="beige")
        self.webScanButt.configure(activeforeground="#000000")
        self.webScanButt.configure(background="#a3d773")
        self.webScanButt.configure(compound='left')
        self.webScanButt.configure(disabledforeground="#a3a3a3")
        self.webScanButt.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.webScanButt.configure(foreground="#ffffff")
        self.webScanButt.configure(highlightbackground="#d9d9d9")
        self.webScanButt.configure(highlightcolor="black")
        self.webScanButt.configure(pady="0")
        self.webScanButt.configure(text='''WebScan Loggs''')
        self.webScanButt.configure(command=self.openWebScanLoggFile)

        self.statisticGraphButt = tk.Button(self.top)
        self.statisticGraphButt.place(
            relx=0.797, rely=0.685, height=54, width=187)
        self.statisticGraphButt.configure(activebackground="beige")
        self.statisticGraphButt.configure(activeforeground="#000000")
        self.statisticGraphButt.configure(background="#a3d773")
        self.statisticGraphButt.configure(compound='left')
        self.statisticGraphButt.configure(disabledforeground="#a3a3a3")
        self.statisticGraphButt.configure(
            font="-family {Arial} -size 14 -weight bold")
        self.statisticGraphButt.configure(foreground="#ffffff")
        self.statisticGraphButt.configure(highlightbackground="#d9d9d9")
        self.statisticGraphButt.configure(highlightcolor="black")
        self.statisticGraphButt.configure(pady="0")
        self.statisticGraphButt.configure(text='''Statistics Graph''')
        self.statisticGraphButt.configure(command=self.generateStatisticsGraph)

        self.refreshBut = tk.Button(self.top)
        self.refreshBut.place(relx=0.698, rely=0.872, height=44, width=117)
        self.refreshBut.configure(activebackground="beige")
        self.refreshBut.configure(activeforeground="#000000")
        self.refreshBut.configure(background="#6262ff")
        self.refreshBut.configure(compound='left')
        self.refreshBut.configure(disabledforeground="#a3a3a3")
        self.refreshBut.configure(font="-family {Arial} -size 14 -weight bold")
        self.refreshBut.configure(foreground="#ffffff")
        self.refreshBut.configure(highlightbackground="#d9d9d9")
        self.refreshBut.configure(highlightcolor="black")
        self.refreshBut.configure(pady="0")
        self.refreshBut.configure(text='''Refresh''')
        self.refreshBut.configure(command=self.refreshPage)

    def adminButtonAction(self):
        from FE.editAdmin import adminEdit
        self.top.destroy()
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        _configWindow = adminEdit(root)
        root.mainloop()

    def mainButtAction(self):
        from FE.mainPage import MainPage
        self.top.destroy()
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        _configWindow = MainPage(root)
        root.mainloop()

    def sitesButtonAction(self):
        from FE.sitesPages import SitesPage
        self.top.destroy()
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        _configWindow = SitesPage(root)
        root.mainloop()

    def refreshPage(self):
        self.top.destroy()
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        _configWindow = StatisticsPage(root)
        root.mainloop()

    def openKeyLoggFile(self):
        fileOpen.openFile(Configuration.KEY_LOGGER_KEY_FILE)

    def openSimilarSearchFile(self):
        fileOpen.openFile(Configuration.KEY_LOGGER_WEB_LOG)

    def openMproxyLoggFile(self):
        fileOpen.openFile(Configuration.MPROXY_LOG_FILE)

    def openWebScanLoggFile(self):
        fileOpen.openFile(Configuration.WEB_SCANNER_LOG_FILE)

    def siteEntryClick(self, event, site):
        webbrowser.open_new_tab(site)

    def _cleanFrame(self):
        for widget in self.tableFrame.winfo_children():
            widget.destroy()

    def back(self):
        self.index = self.index - 1
        start = self.index * self.offset
        end = start + self.offset
        keyData = self.allKeys[start:end]
        self._cleanFrame()

        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                           font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                             font=('Arial', 16, 'bold'))
        nrTimesEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                font=('Arial', 16, 'bold'))

        idEntry.grid(row=0, column=0, padx=(0, 2))
        siteEntry.grid(row=0, column=1, padx=(0, 2))
        nrTimesEntry.grid(row=0, column=2, padx=(0, 2))

        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED, disabledforeground='Black',
                          disabledbackground='LightSteelBlue')

        siteEntry.insert(END, "SITE")
        siteEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')
        nrTimesEntry.insert(END, "STATUS")
        nrTimesEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')

        i = 1
        id = start + 1
        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                 font=('Arial', 16, ''))
            nrTimesEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))

            idEntry.grid(row=i, column=0, padx=(0, 2))
            siteEntry.grid(row=i, column=1, padx=(0, 2))
            nrTimesEntry.grid(row=i, column=2, padx=(0, 2))

            idEntry.insert(END, f"{id}")
            idEntry.configure(state=DISABLED, disabledforeground='blue')

            siteEntry.insert(END, f"{key.decode()}")
            siteEntry.bind("<Double-Button-1>", lambda event,
                           site=key.decode(): self.siteEntryClick(event, site))
            nrTimesEntry.insert(END, f"{self.redisData.get(key).decode()}")

            i += 1
            id += 1

        if self.index == 0:
            self.backButt.configure(state=DISABLED)

        self.nextButt.configure(state=NORMAL)
        self.pageLabel.configure(text=f'page {self.index + 1}')

    def next(self):
        self.index = self.index + 1
        start = self.index * self.offset
        end = start + self.offset
        keyData = self.allKeys[start:end]
        self._cleanFrame()

        idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                           font=('Arial', 16, 'bold'))
        siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                             font=('Arial', 16, 'bold'))
        nrTimesEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                font=('Arial', 16, 'bold'))

        idEntry.grid(row=0, column=0, padx=(0, 2))
        siteEntry.grid(row=0, column=1, padx=(0, 2))
        nrTimesEntry.grid(row=0, column=2, padx=(0, 2))

        idEntry.insert(END, "ID")
        idEntry.configure(state=DISABLED, disabledforeground='Black',
                          disabledbackground='LightSteelBlue')

        siteEntry.insert(END, "SITE")
        siteEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')
        nrTimesEntry.insert(END, "STATUS")
        nrTimesEntry.configure(
            state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')

        i = 1
        id = start + 1
        for key in keyData:
            idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                               font=('Arial', 16, ''))
            siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                 font=('Arial', 16, ''))
            nrTimesEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                    font=('Arial', 16, ''))

            idEntry.grid(row=i, column=0, padx=(0, 2))
            siteEntry.grid(row=i, column=1, padx=(0, 2))
            nrTimesEntry.grid(row=i, column=2, padx=(0, 2))

            idEntry.insert(END, f"{id}")
            idEntry.configure(state=DISABLED, disabledforeground='blue')

            siteEntry.insert(END, f"{key.decode()}")
            siteEntry.bind("<Double-Button-1>", lambda event,
                           site=key.decode(): self.siteEntryClick(event, site))
            nrTimesEntry.insert(END, f"{self.redisData.get(key).decode()}")

            i += 1
            id += 1

        if self.index >= self.nrPages - 1:
            self.nextButt.configure(state=DISABLED)

        self.backButt.configure(state=NORMAL)
        self.pageLabel.configure(text=f'page {self.index + 1}')

    def find(self):
        site = self.siteFindEntry.get()
        if site is None or site == "":
            messagebox.showerror("Error message", "Entry is empty")
        else:
            sitesDict = {}
            contain = False

            for i in range(0, len(self.allKeys)):
                val = self.allKeys[i].decode()
                if site in val:
                    sitesDict[i+1] = val
                contain = True

            if contain:

                self._cleanFrame()

                idEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                   font=('Arial', 16, 'bold'))
                siteEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                     font=('Arial', 16, 'bold'))
                nrTimesEntry = tk.Entry(self.tableFrame, width=15, bg='LightSteelBlue', fg='Black',
                                        font=('Arial', 16, 'bold'))

                idEntry.grid(row=0, column=0, padx=(0, 2))
                siteEntry.grid(row=0, column=1, padx=(0, 2))
                nrTimesEntry.grid(row=0, column=2, padx=(0, 2))

                idEntry.insert(END, "ID")
                idEntry.configure(
                    state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')

                siteEntry.insert(END, "SITE")
                siteEntry.configure(
                    state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')
                nrTimesEntry.insert(END, "STATUS")
                nrTimesEntry.configure(
                    state=DISABLED, disabledforeground='Black', disabledbackground='LightSteelBlue')

                i = 1

                for id in sitesDict.keys():
                    idEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                       font=('Arial', 16, ''))
                    siteEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                         font=('Arial', 16, ''))
                    nrTimesEntry = tk.Entry(self.tableFrame, width=15, fg='blue',
                                            font=('Arial', 16, ''))

                    idEntry.grid(row=i, column=0, padx=(0, 2))
                    siteEntry.grid(row=i, column=1, padx=(0, 2))
                    nrTimesEntry.grid(row=i, column=2, padx=(0, 2))

                    siteName = sitesDict[id]

                    idEntry.insert(END, f"{id}")
                    idEntry.configure(
                        state=DISABLED, disabledforeground='blue')

                    siteEntry.insert(END, f"{siteName}")
                    siteEntry.bind("<Double-Button-1>", lambda event,
                                   site=siteName: self.siteEntryClick(event, site))
                    nrTimesEntry.insert(
                        END, f"{self.redisData.get(siteName.encode()).decode()}")

                    i += 1

                self.pageLabel.configure(text=f'page --')

            else:
                messagebox.showerror(
                    "Error message", "This site does not exist in table")


    def generateStatisticsGraph(self):
        statisticsCache = RedisCache("statistics", host="localhost", port=Configuration.REDIS_PORT)
        
        
        # heights of bars
        height = [int (x.decode()) for x in statisticsCache.getAllValues()]
        
        # labels for bars
        tick_label = [x.decode() for x in statisticsCache.getAllKeys()]
        
        left = [ x for x in range(1, len(tick_label)+1)]
        
 
        plt.bar(left, height, tick_label = tick_label,
                width = 0.2, color = ['red', 'green'])
        
        plt.xlabel('Sites')
 
        plt.ylabel('Time Visited')
        
        plt.xticks(rotation = 90)

        plt.title('Websites Statistics')
        
        plt.show() 
        pass




if __name__ == '__main__':
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    _configWindow = StatisticsPage(root)
    root.mainloop()
