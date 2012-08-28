#! /usr/bin/env python

from PyS5 import Slide, Head, Layout, PPT
from Tkinter import *
import tkMessageBox

class App(object):
    ''' PyS5 designer class '''

    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()

        self.initMenus(master)

        self.btnGen = Button(self.frame,text="Generate",name="btnGen",fg="red",command=self.Generate)
        self.btnGen.grid(row=0,column=2)

        self.chgFlag = False

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

    def AddSlide(self):
        print 'add'

    def DelSlide(self):
        print 'del'

    def Generate(self):
        print 'generate'


# main entry
root = Tk()
app = App(root)
root.mainloop()
