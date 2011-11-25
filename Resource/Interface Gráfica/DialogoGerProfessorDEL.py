#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BOTAOBUSCAR, wxID_DIALOG1BOTAOCONFIRMA, 
 wxID_DIALOG1CAMPOCPF, wxID_DIALOG1NOMEEXCLUIDO, wxID_DIALOG1NOMEUSUARIO, 
 wxID_DIALOG1TEXTOAVISO, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(825, 409), size=wx.Size(400, 250),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Excluir Professor - AcademicSys')
        self.SetClientSize(wx.Size(388, 216))

        self.textoAviso = wx.StaticText(id=wxID_DIALOG1TEXTOAVISO,
              label=u'Insira o CPF para excluir e clique em confirmar:',
              name=u'textoAviso', parent=self, pos=wx.Point(81, 35),
              size=wx.Size(226, 13), style=0)
        self.textoAviso.Center(wx.HORIZONTAL)

        self.campoCPF = wx.TextCtrl(id=wxID_DIALOG1CAMPOCPF, name=u'campoCPF',
              parent=self, pos=wx.Point(51, 64), size=wx.Size(176, 21), style=0,
              value=u'')

        self.botaoConfirma = wx.Button(id=wxID_DIALOG1BOTAOCONFIRMA,
              label=u'CONFIRMAR', name=u'botaoConfirma', parent=self,
              pos=wx.Point(156, 151), size=wx.Size(75, 23), style=0)
        self.botaoConfirma.Center(wx.HORIZONTAL)

        self.nomeExcluido = wx.StaticText(id=wxID_DIALOG1NOMEEXCLUIDO,
              label=u'Nome:', name=u'nomeExcluido', parent=self,
              pos=wx.Point(92, 102), size=wx.Size(32, 13), style=0)

        self.botaoBuscar = wx.Button(id=wxID_DIALOG1BOTAOBUSCAR,
              label=u'Buscar CPF', name=u'botaoBuscar', parent=self,
              pos=wx.Point(251, 62), size=wx.Size(75, 23), style=0)

        self.nomeUsuario = wx.StaticText(id=wxID_DIALOG1NOMEUSUARIO, label=u'',
              name=u'nomeUsuario', parent=self, pos=wx.Point(160, 104),
              size=wx.Size(0, 13), style=wx.ALIGN_CENTRE)
        self.nomeUsuario.SetAutoLayout(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
