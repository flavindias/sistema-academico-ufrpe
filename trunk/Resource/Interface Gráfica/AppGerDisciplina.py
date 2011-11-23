#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameGerDisciplina

modules ={u'FrameGerDisciplina': [1,
                         'Main frame of Application',
                         u'FrameGerDisciplina.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameGerDisciplina.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

def comeca():
    main()
