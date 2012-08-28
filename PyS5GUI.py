#! /usr/bin/env python

from PyS5 import Slide, Head, Layout, PPT
from Tkinter import *
import tkMessageBox
import random

# http://www.tutorialspoint.com/python/python_gui_programming.htm
# http://www.pythonware.com/library/

class App(object):
    ''' PyS5 designer class '''

    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()

        # menue
        self.initMenus(master)

        # controls
        self.lbl1 = Label(self.frame,text="Slides:")
        self.lbl1.grid(row=0,column=0)

        self.SlideScroll = Scrollbar(self.frame,orient=VERTICAL)
        self.slidesList = Listbox(self.frame,selectmode=SINGLE,yscrollcommand=self.SlideScroll.set)
        # double-click and change
        # self.slidesList.bind("<Double-Button-1>", self.ShowSlide)
        self.slidesList.grid(row=1,column=0,rowspan=5,columnspan=5,sticky=W+S+E+N)

        self.btnPrev = Button(self.frame,text="Prev",name="btnPrev",command=self.Prev)
        self.btnPrev.grid(row=6,column=0, sticky=W)
        self.btnNext = Button(self.frame,text="Next",name="btnNext",command=self.Next)
        self.btnNext.grid(row=6,column=1, sticky=W)
        self.btnAdd = Button(self.frame,text="Add",name="btnAdd",command=self.AddSlide)
        self.btnAdd.grid(row=6,column=2, sticky=W)
        self.btnDel = Button(self.frame,text="Del",name="btnDel",command=self.DelSlide)
        self.btnDel.grid(row=6,column=3, sticky=W)
        self.btnClear = Button(self.frame,text="Clear",name="btnClear",command=self.Clear)
        self.btnClear.grid(row=6,column=4, sticky=W)

        self.btnGen = Button(self.frame,text="Generate",name="btnGen",fg="red",command=self.Generate)
        self.btnGen.grid(row=0,column=5)

        # data members
        self.chgFlag = False
        self.curNum = -1

    def initMenus(self,master):
        self.menus = Menu(master)
        master.config(menu=self.menus)
        # file
        mnuFile = Menu(self.menus)
        self.menus.add_cascade(label="File",menu=mnuFile)
        mnuFile.add_command(label="New",command=self.New)
        mnuFile.add_command(label="Open",command=self.Open)
        mnuFile.add_separator()
        mnuFile.add_command(label="Save",command=self.Save)
        mnuFile.add_separator()
        mnuFile.add_command(label="Quit",command=self.Quit)
        # edit
        mnuEdit = Menu(self.menus)
        self.menus.add_cascade(label="Edit",menu=mnuEdit)
        mnuEdit.add_command(label="Add slide",command=self.AddSlide)
        mnuEdit.add_command(label="Delete slide",command=self.DelSlide)
        mnuEdit.add_separator()
        mnuEdit.add_command(label="Generate S5 PPT",command=self.Generate)
        # help
        mnuHelp = Menu(self.menus)
        self.menus.add_cascade(label="Help",menu=mnuHelp)
        mnuHelp.add_command(label="Content",command=self.Help)
        mnuHelp.add_command(label="About",command=self.About)

    def New(self):
        print 'New menu item'

    def Open(self):
        print 'Open menu item'
        self.chgFlag = True

    def Save(self):
        print 'save'
        self.chgFlag = False

    def Quit(self):
        if self.chgFlag:
            if tkMessageBox.askyesno(
            "Exit?",
            "The current project is not saved.\nDo you want to EXIT?"):
                self.frame.quit()
        else:
            self.frame.quit()

    def Help(self):
        print 'Help menu item'

    def About(self):
        print 'About'

    def Prev(self):
        curind = self.slidesList.curselection()
        if len(curind)>0:
            curind = int(curind[0])
            if curind>0:
                self.slidesList.select_clear(0,END)
                self.slidesList.select_set(curind-1)

    def Next(self):
        curind = self.slidesList.curselection()
        if len(curind)>0:
            curind = int(curind[0])
            if curind<self.slidesList.size()-1:
                self.slidesList.select_clear(0,END)
                self.slidesList.select_set(curind+1)

    def AddSlide(self):
        self.slidesList.insert(END,str(random.random()))
        self.curNum += 1
        self.slidesList.select_clear(0,END)
        self.slidesList.select_set(END)
        self.slidesList.see(END) # make sure the given index can be seen

    def DelSlide(self):
        self.temp = [self.slidesList.get(0,END)[x] for x in range(self.slidesList.size()) if str(x) not in self.slidesList.curselection()]
        self.slidesList.delete(0,END)
        self.curNum = -1
        for item in self.temp:
            self.slidesList.insert(END,item)
            self.curNum += 1
        self.slidesList.select_clear(0,END)
        if len(self.slidesList.get(0,END))>0:
            self.slidesList.select_set(0)

    def Clear(self):
        self.slidesList.delete(0,END)
        self.curNum = -1

    def Generate(self):
        print 'generate'


# main entry
root = Tk()
app = App(root)
root.mainloop()
