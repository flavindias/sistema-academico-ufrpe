#Boa:Frame:telaGerente

import wx

def create(parent):
    return telaGerente(parent)

[wxID_TELAGERENTE, wxID_TELAGERENTEBOTAOADICIONAR, 
 wxID_TELAGERENTEBOTAOEDITAR, wxID_TELAGERENTEBOTAOEXCLUIR, 
 wxID_TELAGERENTEBOTAOVOLTAR, wxID_TELAGERENTELINHADIVISORIA, 
 wxID_TELAGERENTELOGOPROFESSOR, wxID_TELAGERENTENOMEADICIONAR, 
 wxID_TELAGERENTENOMEEDITAR, wxID_TELAGERENTEPAINELPROFESSOR, 
 wxID_TELAGERENTESTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(11)]

class telaGerente(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_TELAGERENTE, name=u'telaGerente',
              parent=prnt, pos=wx.Point(40, 2), size=wx.Size(1326, 726),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciamento de Professores - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))

        self.painelProfessor = wx.Panel(id=wxID_TELAGERENTEPAINELPROFESSOR,
              name=u'painelProfessor', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1310, 688), style=wx.TAB_TRAVERSAL)

        self.botaoAdicionar = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_TELAGERENTEBOTAOADICIONAR, name=u'botaoAdicionar',
              parent=self.painelProfessor, pos=wx.Point(182, 303),
              size=wx.Size(230, 230), style=wx.BU_AUTODRAW)
        self.botaoAdicionar.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programacao/Gerenciamento Academico/Resource/Interface Gr\xe1fica/Imagens/bot\xe3o adicionar.png',
              wx.BITMAP_TYPE_PNG))

        self.botaoEditar = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_TELAGERENTEBOTAOEDITAR, name=u'botaoEditar',
              parent=self.painelProfessor, pos=wx.Point(530, 303),
              size=wx.Size(230, 230), style=wx.BU_AUTODRAW)
        self.botaoEditar.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programacao/Gerenciamento Academico/Resource/Interface Gr\xe1fica/Imagens/bot\xe3o editar.png',
              wx.BITMAP_TYPE_PNG))

        self.botaoExcluir = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_TELAGERENTEBOTAOEXCLUIR, name=u'botaoExcluir',
              parent=self.painelProfessor, pos=wx.Point(885, 303),
              size=wx.Size(230, 230), style=wx.BU_AUTODRAW)
        self.botaoExcluir.SetBitmapLabel(wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programacao/Gerenciamento Academico/Resource/Interface Gr\xe1fica/Imagens/botao excluir.png',
              wx.BITMAP_TYPE_PNG))

        self.linhaDivisoria = wx.StaticLine(id=wxID_TELAGERENTELINHADIVISORIA,
              name=u'linhaDivisoria', parent=self.painelProfessor,
              pos=wx.Point(115, 245), size=wx.Size(1079, 2), style=0)

        self.logoProfessor = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programacao/Gerenciamento Academico/Resource/Interface Gr\xe1fica/Imagens/logo professor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_TELAGERENTELOGOPROFESSOR,
              name=u'logoProfessor', parent=self.painelProfessor,
              pos=wx.Point(272, 6), size=wx.Size(710, 218), style=0)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programacao/Gerenciamento Academico/Resource/Interface Gr\xe1fica/Imagens/botao voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_TELAGERENTEBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelProfessor, pos=wx.Point(8,
              8), size=wx.Size(32, 32), style=wx.BU_AUTODRAW)

        self.nomeAdicionar = wx.StaticText(id=wxID_TELAGERENTENOMEADICIONAR,
              label=u'Adicionar Professor', name=u'nomeAdicionar',
              parent=self.painelProfessor, pos=wx.Point(249, 546),
              size=wx.Size(94, 13), style=0)

        self.nomeEditar = wx.StaticText(id=wxID_TELAGERENTENOMEEDITAR,
              label=u'Editar Professor', name=u'nomeEditar',
              parent=self.painelProfessor, pos=wx.Point(616, 552),
              size=wx.Size(78, 13), style=0)

        self.nomeExcluir = wx.StaticText(id=wxID_TELAGERENTENOMEEXCLUIR,
              label=u'Excluir Professor', name=u'nomeExcluir',
              parent=self.painelProfessor, pos=wx.Point(968, 552),
              size=wx.Size(81, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
