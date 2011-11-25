#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameGerProfessorED2T

modules ={u'FrameGerProfessorED2T': [1,
                            'Main frame of Application',
                            u'FrameGerProfessorED2T.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameGerProfessorED2T.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
