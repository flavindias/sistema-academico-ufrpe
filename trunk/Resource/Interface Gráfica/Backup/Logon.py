#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import FrameLogon
modules ={u'FrameLogon': [1, 'Main frame of Application', u'FrameLogon.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameLogon.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

