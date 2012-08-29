#! /usr/bin/env python

from PyS5 import Slide, Head, Layout, PPT
import wx
import random

# ++++++++++++++++++++++++++++++++++++
# A GUI designer for PyS5 Application
# Require:  wxPython, PyS5
# Author:   libralibra
# Email:    790404545#qq.com
#           (replace # with @)
# ++++++++++++++++++++++++++++++++++++

# documentations:
# http://wxpython.org/
# http://wiki.woodpecker.org.cn/moin/WxPythonInAction

# major version number
_version_ = '0.0.1'

# ChangeLog:


class PyS5Designer(wx.Frame):
    """docstring for PyS5Designer"""
    def __init__(self, parent, title="PyS5 Designer"):
        self.frame_ = wx.Frame.__init__(self,parent,title=title+" v "+_version_,size=(400,300))
        self.SetBackgroundColour('white')
        self.Center(wx.BOTH)
        self.CreateStatusBar()
        self.title_ = title+" v "+_version_
        self.num_ = 0
        self.cur_ = 0
        self.flag_ = False

        # set file menus
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN,"&Open\tCtrl+O"," Open a saved project")
        menuNew = filemenu.Append(wx.ID_NEW,"&New\tCtrl+N"," Create a new project")
        filemenu.AppendSeparator()
        menuSave = filemenu.Append(wx.ID_SAVE,"&Save\tCtrl+S"," Save the current presentation")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"&Quit\tCtrl+Q"," Exit PyS5Designer")

        # set edit menus
        editmenu = wx.Menu()
        menuPrev = editmenu.Append(wx.ID_BACKWARD,"Previous slide\tCtrl+R"," Switch to previous slide")
        menuNext = editmenu.Append(wx.ID_FORWARD,"Nex&t slide\tCtrl+T"," Switch to next slide")
        editmenu.AppendSeparator()
        menuAdd = editmenu.Append(wx.ID_ADD,"&Add slide\tCtrl+A"," Add a new slide")
        menuDelete = editmenu.Append(wx.ID_DELETE,"&Delete slide\tCtrl+D"," Delete a slide")
        menuClear = editmenu.Append(wx.ID_CLEAR,"Cl&ear\tCtrl+E"," Clear all slides")

        # set help menus
        helpmenu = wx.Menu()
        menuHelp = helpmenu.Append(wx.ID_HELP_CONTENTS,"&Content\tCtrl+H"," Help contents")
        helpmenu.AppendSeparator()
        menuAbout = helpmenu.Append(wx.ID_ABOUT,"A&bout\tCtrl+B"," About the application")

        # set the menubar
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File")
        menubar.Append(editmenu,"&Edit")
        menubar.Append(helpmenu,"&Help")
        self.SetMenuBar(menubar)

        # set the sizer
        self.grid = wx.GridBagSizer(hgap=5,vgap=5)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        # set the controls
        self.hsizer0 = wx.BoxSizer(wx.HORIZONTAL)
        self.label0 = wx.StaticText(self,label="Slides:",style=wx.ALIGN_LEFT)
        self.label1 = wx.StaticText(self,label=str(self.cur_)+"/"+str(self.num_),style=wx.ALIGN_RIGHT)
        self.hsizer0.Add(self.label0)
        self.hsizer0.Add(self.label1)
        self.grid.Add(self.hsizer0,pos=(0,0),span=(1,4))
##        self.grid.Add(self.label0,pos=(0,0))
##        self.grid.Add(self.label1,pos=(0,1))

        self.list_ = wx.ListBox(self,style=wx.LB_EXTENDED)
        self.grid.Add(self.list_,pos=(1,0),span=(1,4))

        self.hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.btnPrev = wx.Button(self,wx.ID_ANY,"Prev")
        self.btnNext = wx.Button(self,wx.ID_ANY,"Next")
        self.btnAdd = wx.Button(self,wx.ID_ANY,"Add")
        self.btnDelete = wx.Button(self,wx.ID_ANY,"Delete")
        self.btnClear = wx.Button(self,wx.ID_ANY,"Clear")
        self.grid.Add(self.btnPrev,pos=(2,0))
        self.grid.Add(self.btnNext,pos=(2,1))
        self.grid.Add(self.btnAdd,pos=(2,2))
        self.grid.Add(self.btnDelete,pos=(2,3))
        self.grid.Add(self.btnClear,pos=(2,4))

        # set the event binding
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnPrev, menuPrev)
        self.Bind(wx.EVT_MENU, self.OnNext, menuNext)
        self.Bind(wx.EVT_MENU, self.OnAdd, menuAdd)
        self.Bind(wx.EVT_MENU, self.OnDelete, menuDelete)
        self.Bind(wx.EVT_MENU, self.OnClear, menuClear)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # set the event for button
        self.Bind(wx.EVT_BUTTON, self.OnPrev, self.btnPrev)
        self.Bind(wx.EVT_BUTTON, self.OnNext, self.btnNext)
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.btnAdd)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.btnDelete)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.btnClear)

        # show the frame
        self.vsizer.Add(self.grid,0,wx.ALL,5)
        self.SetSizer(self.vsizer)
        #self.SetSizerAndFit(self.vsizer)
        self.Show(True)

    def OnOpen(self,e):
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "PyS5 Designer", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnNew(self,e):
        pass

    def OnSave(self,e):
        pass

    def OnPrev(self,e):
        pass

    def OnNext(self,e):
        pass

    def OnAdd(self,e):
        self.list_.Append(str(random.random()))

    def OnDelete(self,e):
        pass

    def OnClear(self,e):
        self.list_.Clear()

    def OnHelp(self,e):
        pass

    def OnAbout(self,e):
        pass

# main entry
app = wx.App(False)
mainFrame = PyS5Designer(None,"PyS5 Designer")
app.MainLoop()
