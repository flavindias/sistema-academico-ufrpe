#Boa:Frame:FrameGerTurma

import wx

def create(parent):
    return FrameGerTurma(parent)

[wxID_FRAMEGERTURMA, wxID_FRAMEGERTURMABITMAPBUTTON1, 
 wxID_FRAMEGERTURMABOTAOVOLTAR, wxID_FRAMEGERTURMANOMEGERENCIARHORARIO, 
 wxID_FRAMEGERTURMANOMEGERENCIARTURMA, wxID_FRAMEGERTURMANOTAOGERENCIARGRID, 
 wxID_FRAMEGERTURMAPAINELGERTURMA, wxID_FRAMEGERTURMASTATICBITMAP1, 
 wxID_FRAMEGERTURMASTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(9)]

class FrameGerTurma(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERTURMA, name=u'FrameGerTurma',
              parent=prnt, pos=wx.Point(527, 190), size=wx.Size(1326, 726),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciar Turma - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetIcon(wx.Icon(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/Icone.ico',
              wx.BITMAP_TYPE_ICO))

        self.painelGerTurma = wx.Panel(id=wxID_FRAMEGERTURMAPAINELGERTURMA,
              name=u'painelGerTurma', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1310, 688), style=wx.TAB_TRAVERSAL)
        self.painelGerTurma.Center(wx.BOTH)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/logoTurmas.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMASTATICBITMAP1,
              name='staticBitmap1', parent=self.painelGerTurma,
              pos=wx.Point(428, 16), size=wx.Size(472, 110), style=0)
        self.staticBitmap1.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERTURMASTATICLINE1,
              name='staticLine1', parent=self.painelGerTurma, pos=wx.Point(268,
              152), size=wx.Size(791, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/User-group-128.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMABITMAPBUTTON1,
              name='bitmapButton1', parent=self.painelGerTurma,
              pos=wx.Point(359, 224), size=wx.Size(184, 176),
              style=wx.BU_AUTODRAW)

        self.nomeGerenciarTurma = wx.StaticText(id=wxID_FRAMEGERTURMANOMEGERENCIARTURMA,
              label=u'Gerenciar Turma', name=u'nomeGerenciarTurma',
              parent=self.painelGerTurma, pos=wx.Point(412, 412),
              size=wx.Size(80, 13), style=0)

        self.notaoGerenciarGrid = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/imgHorario.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMANOTAOGERENCIARGRID,
              name=u'notaoGerenciarGrid', parent=self.painelGerTurma,
              pos=wx.Point(787, 224), size=wx.Size(184, 176),
              style=wx.BU_AUTODRAW)

        self.nomeGerenciarHorario = wx.StaticText(id=wxID_FRAMEGERTURMANOMEGERENCIARHORARIO,
              label=u'Gerenciar Horario', name=u'nomeGerenciarHorario',
              parent=self.painelGerTurma, pos=wx.Point(840, 414),
              size=wx.Size(85, 13), style=0)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMABOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelGerTurma, pos=wx.Point(296,
              48), size=wx.Size(48, 48), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
