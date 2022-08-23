#! /usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("."))

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog
import shutil
from webServices.configuration import  Configuration
from tkinter import messagebox
import yaml
from webServices.wordGenerator import Generator
import webServices.utils as utils
from  webServices import  key_logger
from webServices.sysprox import  Proxy 
import FE.fileOpen as fileOpen
from cache.redisCache import  RedisCache

class MainPage:
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
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("803x568+250+150")
        top.minsize(116, 1)
        top.maxsize(1366, 746)
        top.resizable(FALSE,  FALSE)
        top.title("Main Page")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.MainButt = tk.Button(self.top)
        self.MainButt.place(relx=0.0, rely=0.0, height=54, width=187)
        self.MainButt.configure(activebackground="beige")
        self.MainButt.configure(activeforeground="#000000")
        self.MainButt.configure(background="#aaaaaa")
        self.MainButt.configure(compound='left')
        self.MainButt.configure(disabledforeground="#a3a3a3")
        self.MainButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.MainButt.configure(foreground="#ffffff")
        self.MainButt.configure(highlightbackground="#d9d9d9")
        self.MainButt.configure(highlightcolor="black")
        self.MainButt.configure(pady="0")
        self.MainButt.configure(text='''Main Page''')
        

        self.SitesButt = tk.Button(self.top)
        self.SitesButt.place(relx=0.258, rely=0.0, height=54, width=187)
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
        self.StatisticsBut.place(relx=0.516, rely=0.0, height=54, width=177)
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
        self.AdminButt.place(relx=0.76, rely=0.0, height=54, width=187)
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

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.selectButt = tk.Button(self.top)
        self.selectButt.place(relx=0.026, rely=0.548, height=44, width=127)
        self.selectButt.configure(activebackground="beige")
        self.selectButt.configure(activeforeground="#000000")
        self.selectButt.configure(background="#6262ff")
        self.selectButt.configure(compound='left')
        self.selectButt.configure(disabledforeground="#a3a3a3")
        self.selectButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.selectButt.configure(foreground="#ffffff")
        self.selectButt.configure(highlightbackground="#d9d9d9")
        self.selectButt.configure(highlightcolor="black")
        self.selectButt.configure(pady="0")
        self.selectButt.configure(text='''Select''')
        self.selectButt.configure(command=self.browseFiles)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.026, rely=0.319, height=21, width=222)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 13 -weight bold -slant italic -underline 1")
        self.Label1.configure(foreground="#4e58d6")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Select keywords csv file''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.026, rely=0.424, height=21, width=56)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 13 -weight bold -slant italic -underline 1")
        self.Label2.configure(foreground="#4e58d6")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Path:''')

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.486, rely=0.176,  relheight=0.6)
        self.TSeparator1.configure(orient="vertical")

        self.pathEntity = tk.Entry(self.top)
        self.pathEntity.place(relx=0.115, rely=0.407, height=30, relwidth=0.341)
        self.pathEntity.configure(background="white")
        self.pathEntity.configure(disabledforeground="#a3a3a3")
        self.pathEntity.configure(font="TkFixedFont")
        self.pathEntity.configure(foreground="#000000")
        self.pathEntity.configure(highlightbackground="#d9d9d9")
        self.pathEntity.configure(highlightcolor="black")
        self.pathEntity.configure(insertbackground="black")
        self.pathEntity.configure(selectbackground="#c4c4c4")
        self.pathEntity.configure(selectforeground="black")

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.532, rely=0.229, height=21, width=222)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 13 -weight bold -slant italic -underline 1")
        self.Label3.configure(foreground="#4e58d6")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Write keywords''')

        self.Label3_1 = tk.Label(self.top)
        self.Label3_1.place(relx=0.532, rely=0.317, height=21, width=58)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#d9d9d9")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Arial} -size 13 -weight bold -slant italic -underline 1")
        self.Label3_1.configure(foreground="#4e58d6")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Word''')

        self.wordEntry = tk.Entry(self.top)
        self.wordEntry.place(relx=0.684, rely=0.299, height=30
                , relwidth=0.242)
        self.wordEntry.configure(background="white")
        self.wordEntry.configure(disabledforeground="#a3a3a3")
        self.wordEntry.configure(font="TkFixedFont")
        self.wordEntry.configure(foreground="#000000")
        self.wordEntry.configure(highlightbackground="#d9d9d9")
        self.wordEntry.configure(highlightcolor="black")
        self.wordEntry.configure(insertbackground="black")
        self.wordEntry.configure(selectbackground="#c4c4c4")
        self.wordEntry.configure(selectforeground="black")

        self.wordsListBox = tk.Listbox(self.top)
        self.wordsListBox.place(relx=0.684, rely=0.405, relheight=0.197
                , relwidth=0.247)
        self.wordsListBox.configure(background="white")
        self.wordsListBox.configure(disabledforeground="#a3a3a3")
        self.wordsListBox.configure(font="TkFixedFont")
        self.wordsListBox.configure(foreground="#000000")
        self.wordsListBox.configure(highlightbackground="#d9d9d9")
        self.wordsListBox.configure(highlightcolor="black")
        self.wordsListBox.configure(selectbackground="#c4c4c4")
        self.wordsListBox.configure(selectforeground="black")
        self.wordsListBox.bind("<<ListboxSelect>>", self.selectWord)

        self.addButt = tk.Button(self.top)
        self.addButt.place(relx=0.519, rely=0.405, height=44, width=87)
        self.addButt.configure(activebackground="beige")
        self.addButt.configure(activeforeground="#000000")
        self.addButt.configure(background="#6262ff")
        self.addButt.configure(compound='left')
        self.addButt.configure(disabledforeground="#a3a3a3")
        self.addButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.addButt.configure(foreground="#ffffff")
        self.addButt.configure(highlightbackground="#d9d9d9")
        self.addButt.configure(highlightcolor="black")
        self.addButt.configure(pady="0")
        self.addButt.configure(text='''Add''')
        self.addButt.configure(command=self.addWordListBox)

        self.removeButt = tk.Button(self.top)
        self.removeButt.place(relx=0.519, rely=0.511, height=44, width=87)
        self.removeButt.configure(activebackground="beige")
        self.removeButt.configure(activeforeground="#000000")
        self.removeButt.configure(background="#eb0214")
        self.removeButt.configure(compound='left')
        self.removeButt.configure(disabledforeground="#a3a3a3")
        self.removeButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.removeButt.configure(foreground="#ffffff")
        self.removeButt.configure(highlightbackground="#d9d9d9")
        self.removeButt.configure(highlightcolor="black")
        self.removeButt.configure(pady="0")
        self.removeButt.configure(text='''Remove''')
        self.removeButt.configure(command=self.deleteWordListBox)

        self.generateButt = tk.Button(self.top)
        self.generateButt.place(relx=0.684, rely=0.651, height=44, width=157)
        self.generateButt.configure(activebackground="beige")
        self.generateButt.configure(activeforeground="#000000")
        self.generateButt.configure(background="#6262ff")
        self.generateButt.configure(compound='left')
        self.generateButt.configure(disabledforeground="#a3a3a3")
        self.generateButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.generateButt.configure(foreground="#ffffff")
        self.generateButt.configure(highlightbackground="#d9d9d9")
        self.generateButt.configure(highlightcolor="black")
        self.generateButt.configure(pady="0")
        self.generateButt.configure(text='''Generate CSV''')
        self.generateButt.configure(command=self.generateAction)

        self.startButt = tk.Button(self.top)
        self.startButt.place(relx=0.05, rely=0.845, height=44, width=157)
        self.startButt.configure(activebackground="beige")
        self.startButt.configure(activeforeground="#000000")
        self.startButt.configure(background="#51ff51")
        self.startButt.configure(compound='left')
        self.startButt.configure(disabledforeground="#a3a3a3")
        self.startButt.configure(font="-family {Arial} -size 16 -weight bold")
        self.startButt.configure(foreground="#ffffff")
        self.startButt.configure(highlightbackground="#d9d9d9")
        self.startButt.configure(highlightcolor="black")
        self.startButt.configure(pady="0")
        self.startButt.configure(text='''Start Scanner''')
        self.startButt.configure(command=self.startWebScanner)

        self.stopButt = tk.Button(self.top)
        self.stopButt.place(relx=0.28 , rely=0.845, height=44, width=157)
        self.stopButt.configure(activebackground="beige")
        self.stopButt.configure(activeforeground="#000000")
        self.stopButt.configure(background="#f5010a")
        self.stopButt.configure(compound='left')
        self.stopButt.configure(disabledforeground="#a3a3a3")
        self.stopButt.configure(font="-family {Arial} -size 16 -weight bold")
        self.stopButt.configure(foreground="#ffffff")
        self.stopButt.configure(highlightbackground="#d9d9d9")
        self.stopButt.configure(highlightcolor="black")
        self.stopButt.configure(pady="0")
        self.stopButt.configure(text='''Stop Scanner''')
        self.stopButt.configure(command=self.stopWebScanner)
        
        self.cleanCacheButt = tk.Button(self.top)
        self.cleanCacheButt.place(relx=0.52 , rely=0.845, height=44, width=157)
        self.cleanCacheButt.configure(activebackground="beige")
        self.cleanCacheButt.configure(activeforeground="#000000")
        self.cleanCacheButt.configure(background="#f5010a")
        self.cleanCacheButt.configure(compound='left')
        self.cleanCacheButt.configure(disabledforeground="#a3a3a3")
        self.cleanCacheButt.configure(font="-family {Arial} -size 16 -weight bold")
        self.cleanCacheButt.configure(foreground="#ffffff")
        self.cleanCacheButt.configure(highlightbackground="#d9d9d9")
        self.cleanCacheButt.configure(highlightcolor="black")
        self.cleanCacheButt.configure(pady="0")
        self.cleanCacheButt.configure(text='''Clean Cache''')
        self.cleanCacheButt.configure(command=self.cleanCache)
        
        
        self.openFileButt = tk.Button(self.top)
        self.openFileButt.place(relx=0.75, rely=0.845, height=44, width=166)
        self.openFileButt.configure(activebackground="beige")
        self.openFileButt.configure(activeforeground="#000000")
        self.openFileButt.configure(background="#6262ff")
        self.openFileButt.configure(compound='left')
        self.openFileButt.configure(disabledforeground="#a3a3a3")
        self.openFileButt.configure(font="-family {Arial} -size 14 -weight bold")
        self.openFileButt.configure(foreground="#ffffff")
        self.openFileButt.configure(highlightbackground="#d9d9d9")
        self.openFileButt.configure(highlightcolor="black")
        self.openFileButt.configure(pady="0")
        self.openFileButt.configure(text='''Check Dictionary''')
        self.openFileButt.configure(command=self.openDictFile)
        


    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                        ("all files",
                                                    "*.*")))
        if filename is not None and filename != "":
            self.pathEntity.insert(0,filename)
            shutil.copy(filename, Configuration.NLP_FILE)
    
    def adminButtonAction(self):
        from FE.editAdmin import adminEdit
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = adminEdit(root)
        root.mainloop()
        
    def sitesButtonAction(self):
        from FE.sitesPages import  SitesPage
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = SitesPage(root)
        root.mainloop()
        
    def statisticButtonAction(self):
        from FE.statisticsPage import  StatisticsPage
        self.top.destroy()
        root = tk.Tk() 
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        _configWindow = StatisticsPage(root)
        root.mainloop()
        
        
    def addWordListBox(self):
        word  =  self.wordEntry.get().lower()
        if word is None  or  word == '':
            messagebox.showerror("Error Message" ,"Word entry is empty")
        else:
            listWords = self.wordsListBox.get(0 , END)
            if word not in listWords:
                self.wordsListBox.insert(END , word)
                self.wordEntry.delete(0 , END)
    
    
    def deleteWordListBox(self):
        word = self.wordEntry.get().lower()
        
        if word is None  or  word == '':
            messagebox.showerror("Error Message" , "Word entry is empty")
        else :
            
            wordList = list(self.wordsListBox.get(0 ,END))
            if word not in wordList:
                messagebox.showerror("Error Message"  , "This word does not exist")
            else: 
                wordIndex = wordList.index(word)
                self.wordsListBox.delete(wordIndex)
                self.wordEntry.delete(0 , END)
            
                

    
    def selectWord(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.wordEntry.delete(0, END)
            self.wordEntry.insert(0 , data)
    
    
    def generateAction(self):
        wordList = self.wordsListBox.get(0 ,END)
        if len(wordList) > 0 :
            generator  =  Generator()
            generator.generateWords(set(wordList))
            open(Configuration.NLP_FILE, "w").close()
            generator.generateCSV(Configuration.NLP_FILE)
            self.wordEntry.delete(0 ,END)
            self.wordsListBox.delete(0,END)
            messagebox.showinfo("Successfull" , "Words dictionary generated successfully")
        else: 
            messagebox.showerror("Error Message"  , "Word List is empty")
    
    def startWebScanner(self):
        stream  = open(Configuration.CONFIG_RESOURCES ,"r")
        yamlData = yaml.safe_load(stream)
        stream.close()
        if yamlData["webScanner"]:
            messagebox.showerror("Error Message"  , "Web Services are currently running")
            
        else:
            if Configuration.ceckContainerRunning():
                if os.path.getsize(Configuration.NLP_FILE) > 0:
                    proxy = Proxy("127.0.0.1", 8080)
                    proxy.engage()
                    utils.startWebScanner()
                    utils.startMitmProxy()
                    utils.startKeyLogger()
                    yamlData["webScanner"] = True
                    yamlData["keylogger"] = True
                    yamlData["mproxy"] = True
                    stream  = open(Configuration.CONFIG_RESOURCES ,"w")
                    stream.write(yaml.dump(yamlData))
                    stream.close()
                else:
                    messagebox.showerror("Error Message"  , "Word Dictionary is empty")
            else : 
                messagebox.showerror("Error Message"  , "Run docker compose up inside project directory first")
    
    def stopWebScanner(self):
        stream  = open(Configuration.CONFIG_RESOURCES ,"r")
        yamlData = yaml.safe_load(stream)
        stream.close()
        if yamlData["webScanner"]:
            try:
                proxy = Proxy("127.0.0.1", 8080)
                proxy.cleanup()
                utils.stopWebScanner()
                utils.closeMitmProxy()
                key_logger.stop()
                yamlData["webScanner"] = False
                yamlData["keylogger"] = False
                yamlData["mproxy"] = False
                stream  = open(Configuration.CONFIG_RESOURCES ,"w")
                stream.write(yaml.dump(yamlData))
                stream.close()
            except :
                yamlData["webScanner"] = False
                yamlData["keylogger"] = False
                yamlData["mproxy"] = False
                stream  = open(Configuration.CONFIG_RESOURCES ,"w")
                stream.write(yaml.dump(yamlData))
                
            
         
        else:
            messagebox.showerror("Error Message"  , "Web Services have not started yet")
                
    
    def openDictFile(self):
        fileOpen.openFile(Configuration.NLP_FILE)
        pass
    
    def cleanCache(self):
        visitedCache = RedisCache("visited", host="localhost", port=Configuration.REDIS_PORT)
        statisticsCache = RedisCache("statistics", host="localhost", port=Configuration.REDIS_PORT)
        visitedCache.clear()
        statisticsCache.clear()
        visitedCache.close()
        statisticsCache.close()
        
    
if __name__ == '__main__':
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    _configWindow = MainPage(root)
    root.mainloop()
    pass




