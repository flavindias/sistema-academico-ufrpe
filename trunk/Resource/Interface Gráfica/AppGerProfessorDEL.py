#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import DialogoGerProfessorDEL

modules ={u'DialogoGerProfessorDEL': [1,
                             'Main frame of Application',
                             u'DialogoGerProfessorDEL.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = DialogoGerProfessorDEL.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
