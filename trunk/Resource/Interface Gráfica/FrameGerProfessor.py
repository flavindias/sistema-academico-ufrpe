#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BOTAOCADASTRAR, wxID_FRAME1BOTAOEDITAR, 
 wxID_FRAME1BOTAOEXCLUIR, wxID_FRAME1BOTAOVOLTAR, wxID_FRAME1LOGO, 
 wxID_FRAME1LOGOACADEMICSYS, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1TEXTOCADASTRAR, wxID_FRAME1TEXTOEDITAR, wxID_FRAME1TEXTOEXCLUIR, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(559, 219), size=wx.Size(1322, 722),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciamento de Professores - AcademicSYS')
        self.SetClientSize(wx.Size(1310, 688))

        self.logo = wx.Panel(id=wxID_FRAME1LOGO, name=u'logo', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1310, 688),
              style=wx.TAB_TRAVERSAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.logo, pos=wx.Point(159, 265),
              size=wx.Size(991, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)
        self.staticLine1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)

        self.botaoEditar = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1BOTAOEDITAR, name=u'botaoEditar', parent=self.logo,
              pos=wx.Point(553, 296), size=wx.Size(216, 208),
              style=wx.BU_AUTODRAW)
        self.botaoEditar.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/Icone Editar.png',
              wx.BITMAP_TYPE_PNG))
        self.botaoEditar.Center(wx.HORIZONTAL)
        self.botaoEditar.Bind(wx.EVT_BUTTON, self.OnBotaoEditarButton,
              id=wxID_FRAME1BOTAOEDITAR)

        self.botaoCadastrar = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1BOTAOCADASTRAR, name=u'botaoCadastrar',
              parent=self.logo, pos=wx.Point(209, 295), size=wx.Size(216, 208),
              style=wx.BU_AUTODRAW)
        self.botaoCadastrar.SetBitmapDisabled(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/Icone Adiconar.png',
              wx.BITMAP_TYPE_PNG))
        self.botaoCadastrar.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/Icone Adiconar.png',
              wx.BITMAP_TYPE_PNG))
        self.botaoCadastrar.Bind(wx.EVT_BUTTON, self.OnBotaoCadastrarButton,
              id=wxID_FRAME1BOTAOCADASTRAR)

        self.botaoExcluir = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1BOTAOEXCLUIR, name=u'botaoExcluir',
              parent=self.logo, pos=wx.Point(884, 297), size=wx.Size(216, 208),
              style=wx.BU_AUTODRAW)
        self.botaoExcluir.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/Icone deletar.png',
              wx.BITMAP_TYPE_PNG))
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAME1BOTAOEXCLUIR)

        self.textoCadastrar = wx.StaticText(id=wxID_FRAME1TEXTOCADASTRAR,
              label=u'Cadastrar', name=u'textoCadastrar', parent=self.logo,
              pos=wx.Point(295, 519), size=wx.Size(49, 13), style=0)

        self.textoEditar = wx.StaticText(id=wxID_FRAME1TEXTOEDITAR,
              label=u'Editar', name=u'textoEditar', parent=self.logo,
              pos=wx.Point(646, 522), size=wx.Size(29, 13), style=0)
        self.textoEditar.Center(wx.HORIZONTAL)

        self.textoExcluir = wx.StaticText(id=wxID_FRAME1TEXTOEXCLUIR,
              label=u'Excluir', name=u'textoExcluir', parent=self.logo,
              pos=wx.Point(984, 521), size=wx.Size(32, 13), style=0)

        self.logoAcademicSys = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/logo professor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1LOGOACADEMICSYS,
              name=u'logoAcademicSys', parent=self.logo, pos=wx.Point(305, 17),
              size=wx.Size(712, 216), style=0)
        self.logoAcademicSys.Center(wx.HORIZONTAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.logo, pos=wx.Point(8, 8),
              size=wx.Size(48, 48), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBitmapButton1Button(self, event):
        event.Skip()

    def OnBotaoCadastrarButton(self, event):
        event.Skip()

    def OnBotaoEditarButton(self, event):
        event.Skip()

    def OnBotaoExcluirButton(self, event):
        event.Skip()
