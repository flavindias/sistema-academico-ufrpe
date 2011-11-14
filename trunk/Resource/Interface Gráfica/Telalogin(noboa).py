#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CONFIRMARLOGIN, wxID_FRAME1LOGIN, wxID_FRAME1PANEL1, 
 wxID_FRAME1SENHA, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICLINE2, 
] = [wx.NewId() for _init_ctrls in range(7)]

[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)

        self.menuBar1 = wx.MenuBar()

        self.menuBar2 = wx.MenuBar()

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(561, 219), size=wx.Size(782, 640),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self._init_utils()
        self.SetClientSize(wx.Size(770, 606))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(770, 606),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label=u'Login',
              name='staticBox1', parent=self.panel1, pos=wx.Point(213, 342),
              size=wx.Size(344, 192), style=0)
        self.staticBox1.Center(wx.HORIZONTAL)

        self.login = wx.TextCtrl(id=wxID_FRAME1LOGIN, name=u'login',
              parent=self.panel1, pos=wx.Point(261, 414), size=wx.Size(248, 21),
              style=0, value=u'Login')
        self.login.Center(wx.HORIZONTAL)

        self.Senha = wx.TextCtrl(id=wxID_FRAME1SENHA, name=u'Senha',
              parent=self.panel1, pos=wx.Point(262, 450), size=wx.Size(246, 21),
              style=wx.TE_PASSWORD, value=u'Senha')
        self.Senha.Center(wx.HORIZONTAL)
        self.Senha.SetToolTipString(u'textCtrl2')

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME1STATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(165, 323),
              size=wx.Size(439, 2), style=0)
        self.staticLine2.Center(wx.HORIZONTAL)

        self.confirmarLogin = wx.Button(id=wxID_FRAME1CONFIRMARLOGIN,
              label=u'Acessar', name=u'confirmarLogin', parent=self.panel1,
              pos=wx.Point(347, 499), size=wx.Size(75, 23), style=0)
        self.confirmarLogin.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
