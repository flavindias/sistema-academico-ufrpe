#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameGerProfessor

modules ={u'FrameGerProfessor': [1,
                        'Main frame of Application',
                        u'FrameGerProfessor.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameGerProfessor.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def iniciarProf():
    application = BoaApp(0)
    application.MainLoop()
