#Boa:Frame:frameLogin

import wx
import sys

lista = sys.path[0].split('\\')
temp = ''
for i in range(len(lista)-1):
    temp += lista[i]
    if i != len(lista)-1:
        temp += '\\'
sys.path[0] = temp

from Login import Login

def create(parent):
    return frameLogin(parent)

[wxID_FRAMELOGIN, wxID_FRAMELOGINBOTAOLOGAR, wxID_FRAMELOGINDIGITELOGIN, 
 wxID_FRAMELOGINDIGITESENHA, wxID_FRAMELOGINESPACOLOGIN, 
 wxID_FRAMELOGINLINHADIVISORIA, wxID_FRAMELOGINLOGOSYS, 
 wxID_FRAMELOGINNOMEERRO, wxID_FRAMELOGINNOMELOGIN, wxID_FRAMELOGINNOMESENHA, 
 wxID_FRAMELOGINTELALOGIN, 
] = [wx.NewId() for _init_ctrls in range(11)]

class frameLogin(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMELOGIN, name=u'frameLogin',
              parent=prnt, pos=wx.Point(531, 210), size=wx.Size(1378, 740),
              style=wx.MAXIMIZE_BOX | wx.MAXIMIZE | wx.DEFAULT_FRAME_STYLE,
              title=u'AcademicSYS - Gerenciamento Escolar')
        self.SetClientSize(wx.Size(1366, 706))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'../Interface Gr\xe1fica/Imagens/Icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.SetAutoLayout(True)

        self.telaLogin = wx.Window(id=wxID_FRAMELOGINTELALOGIN,
              name=u'telaLogin', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1366, 706), style=0)
        self.telaLogin.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.telaLogin.Center(wx.BOTH)
        self.telaLogin.SetThemeEnabled(False)
        self.telaLogin.SetAutoLayout(True)

        self.espacoLogin = wx.StaticBox(id=wxID_FRAMELOGINESPACOLOGIN,
              label=u'Area de Login', name=u'espacoLogin',
              parent=self.telaLogin, pos=wx.Point(468, 380), size=wx.Size(430,
              208), style=0)
        self.espacoLogin.Center(wx.HORIZONTAL)
        self.espacoLogin.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.espacoLogin.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.espacoLogin.SetAutoLayout(False)

        self.nomeLogin = wx.StaticText(id=wxID_FRAMELOGINNOMELOGIN,
              label=u'Login: ', name=u'nomeLogin', parent=self.telaLogin,
              pos=wx.Point(497, 412), size=wx.Size(33, 13), style=0)

        self.digiteLogin = wx.TextCtrl(id=wxID_FRAMELOGINDIGITELOGIN,
              name=u'digiteLogin', parent=self.telaLogin, pos=wx.Point(533,
              440), size=wx.Size(299, 24), style=0, value=u'')
        self.digiteLogin.Center(wx.HORIZONTAL)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMELOGINNOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.telaLogin,
              pos=wx.Point(496, 483), size=wx.Size(35, 13), style=0)

        self.digiteSenha = wx.TextCtrl(id=wxID_FRAMELOGINDIGITESENHA,
              name=u'digiteSenha', parent=self.telaLogin, pos=wx.Point(535,
              507), size=wx.Size(296, 24), style=wx.TE_PASSWORD, value=u'')
        self.digiteSenha.Center(wx.HORIZONTAL)

        self.botaoLogar = wx.Button(id=wxID_FRAMELOGINBOTAOLOGAR,
              label=u'Acessar', name=u'botaoLogar', parent=self.telaLogin,
              pos=wx.Point(782, 546), size=wx.Size(75, 23), style=0)
        self.botaoLogar.Bind(wx.EVT_BUTTON, self.OnBotaoLogarButton,
              id=wxID_FRAMELOGINBOTAOLOGAR)

        self.linhaDivisoria = wx.StaticLine(id=wxID_FRAMELOGINLINHADIVISORIA,
              name=u'linhaDivisoria', parent=self.telaLogin, pos=wx.Point(371,
              352), size=wx.Size(623, 2), style=0)
        self.linhaDivisoria.Center(wx.HORIZONTAL)

        self.logoSys = wx.StaticBitmap(bitmap=wx.Bitmap(u'../Interface Gr\xe1fica/Imagens/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMELOGINLOGOSYS, name=u'logoSys',
              parent=self.telaLogin, pos=wx.Point(343, 40), size=wx.Size(680,
              278), style=0)
        self.logoSys.Center(wx.HORIZONTAL)

        self.nomeErro = wx.StaticText(id=wxID_FRAMELOGINNOMEERRO, label=u'',
              name=u'nomeErro', parent=self.telaLogin, pos=wx.Point(599, 416),
              size=wx.Size(168, 13),
              style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTRE)
        self.nomeErro.SetAutoLayout(True)
        self.nomeErro.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoLogarButton(self, event):
        self.Logar = Login()
        self.valorLogin = self.digiteLogin.GetValue()
        self.valorSenha = self.digiteSenha.GetValue()
        if self.Logar.valida(self.valorLogin, self.valorSenha):
            self.nomeErro.SetLabel('Ok!')
        else:
            self.nomeErro.SetLabel('Login ou Senha Invalido!')
        event.Skip()
