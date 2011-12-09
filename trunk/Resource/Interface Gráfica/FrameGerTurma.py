#Boa:Frame:FrameGerTurma

import wx
import ponte

def create(parent):
    return FrameGerTurma(parent)

[wxID_FRAMEGERTURMA, wxID_FRAMEGERTURMABOTAOGERENCIARGRID, 
 wxID_FRAMEGERTURMABOTAOVOLTAR, wxID_FRAMEGERTURMAGERTURMABITMAPBUTTON, 
 wxID_FRAMEGERTURMANOMEGERENCIARHORARIO, wxID_FRAMEGERTURMANOMEGERENCIARTURMA, 
 wxID_FRAMEGERTURMAPAINELGERTURMA, wxID_FRAMEGERTURMASTATICBITMAP1, 
 wxID_FRAMEGERTURMASTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(9)]

class FrameGerTurma(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERTURMA, name=u'FrameGerTurma',
              parent=prnt, pos=wx.Point(48, 16), size=wx.Size(1318, 722),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciar Turma - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)

        self.painelGerTurma = wx.Panel(id=wxID_FRAMEGERTURMAPAINELGERTURMA,
              name=u'painelGerTurma', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1310, 688), style=wx.TAB_TRAVERSAL)
        self.painelGerTurma.Center(wx.BOTH)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logoTurmas.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMASTATICBITMAP1,
              name='staticBitmap1', parent=self.painelGerTurma,
              pos=wx.Point(419, 16), size=wx.Size(472, 110), style=0)
        self.staticBitmap1.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERTURMASTATICLINE1,
              name='staticLine1', parent=self.painelGerTurma, pos=wx.Point(259,
              152), size=wx.Size(791, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.GerTurmaBitmapButton = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/User-group-128.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAGERTURMABITMAPBUTTON,
              name=u'GerTurmaBitmapButton', parent=self.painelGerTurma,
              pos=wx.Point(359, 224), size=wx.Size(184, 176),
              style=wx.BU_AUTODRAW)
        self.GerTurmaBitmapButton.Bind(wx.EVT_BUTTON,
              self.OnGerTurmaBitmapButtonButton,
              id=wxID_FRAMEGERTURMAGERTURMABITMAPBUTTON)

        self.nomeGerenciarTurma = wx.StaticText(id=wxID_FRAMEGERTURMANOMEGERENCIARTURMA,
              label=u'Gerenciar Turma', name=u'nomeGerenciarTurma',
              parent=self.painelGerTurma, pos=wx.Point(412, 412),
              size=wx.Size(80, 13), style=0)

        self.botaoGerenciarGrid = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/imgHorario.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMABOTAOGERENCIARGRID,
              name=u'botaoGerenciarGrid', parent=self.painelGerTurma,
              pos=wx.Point(787, 224), size=wx.Size(184, 176),
              style=wx.BU_AUTODRAW)
        self.botaoGerenciarGrid.Bind(wx.EVT_BUTTON,
              self.OnBotaoGerenciarGridButton,
              id=wxID_FRAMEGERTURMABOTAOGERENCIARGRID)

        self.nomeGerenciarHorario = wx.StaticText(id=wxID_FRAMEGERTURMANOMEGERENCIARHORARIO,
              label=u'Gerenciar Horario', name=u'nomeGerenciarHorario',
              parent=self.painelGerTurma, pos=wx.Point(840, 414),
              size=wx.Size(85, 13), style=0)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMABOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelGerTurma, pos=wx.Point(296,
              48), size=wx.Size(48, 48), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEGERTURMABOTAOVOLTAR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGerTurmaBitmapButtonButton(self, event):
        self.Close(True)
        ponte.mainFrameGerTurmaAlunosApp()
        exit()
        event.Skip()

    def OnBotaoGerenciarGridButton(self, event):
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        self.Close(True)
        ponte.mainAcademicsFrameApp()
        exit()
        event.Skip()
