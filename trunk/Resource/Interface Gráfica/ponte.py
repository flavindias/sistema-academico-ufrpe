#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import FrameGerAluno
import FrameGerProfessor
import FrameLogon
import FrameGerDisciplina
import academicsFrame

class FrameGerAlunoApp(wx.App):
    def OnInit(self):
        self.main = FrameGerAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainFrameGerAlunoApp():
    global modules
    modules ={u'FrameGerAluno': [1, 'Main frame of Application', u'FrameGerAluno.py']}
    application = FrameGerAlunoApp(0)
    application.MainLoop()

class FrameGerProfessorApp(wx.App):
    def OnInit(self):
        self.main = FrameGerProfessor.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainFrameGerProfessorApp():
    global modules
    modules ={u'FrameGerProfessor': [1, 'Main frame of Application', u'FrameGerProfessor.py']}
    application = FrameGerProfessorApp(0)
    application.MainLoop()

class FrameLogonApp(wx.App):
    def OnInit(self):
        self.main = FrameLogon.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainFrameLogonApp():
    global modules
    modules ={u'FrameLogon': [1, 'Main frame of Application', u'FrameLogon.py']}
    application = FrameLogonApp(0)
    application.MainLoop()

class FrameGerDisciplinaApp(wx.App):
    def OnInit(self):
        self.main = FrameGerDisciplina.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainFrameGerDisciplinaApp():
    global modules
    modules ={u'FrameGerDisciplina': [1,'Main frame of Application',u'FrameGerDisciplina.py']}
    application = FrameGerDisciplinaApp(0)
    application.MainLoop()

class academicsFrameApp(wx.App):
    def OnInit(self):
        self.main = academicsFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainAcademicsFrameApp():
    global modules
    modules ={u'academicsFrame': [1, 'Main frame of Application', u'academicsFrame.py']}
    application = academicsFrameApp(0)
    application.MainLoop()
