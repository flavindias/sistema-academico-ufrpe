#Boa:Frame:FrameGerenciarHorario

import wx
import wx.lib.buttons
import wx.grid

def create(parent):
    return FrameGerenciarHorario(parent)

[wxID_FRAMEGERENCIARHORARIO, wxID_FRAMEGERENCIARHORARIOBOTAOAPLICAR, 
 wxID_FRAMEGERENCIARHORARIOBOTAOCANCELAR, 
 wxID_FRAMEGERENCIARHORARIOBOTAOSALVAR, wxID_FRAMEGERENCIARHORARIOBOTAOVOLTAR, 
 wxID_FRAMEGERENCIARHORARIOCAIXAPROFESSOR, 
 wxID_FRAMEGERENCIARHORARIOCAIXASERIE, wxID_FRAMEGERENCIARHORARIOCAMPOQUA1, 
 wxID_FRAMEGERENCIARHORARIOCAMPOQUA2, wxID_FRAMEGERENCIARHORARIOCAMPOQUA3, 
 wxID_FRAMEGERENCIARHORARIOCAMPOQUA4, wxID_FRAMEGERENCIARHORARIOCAMPOQUA5, 
 wxID_FRAMEGERENCIARHORARIOCAMPOQUI1, wxID_FRAMEGERENCIARHORARIOCAMPOQUI2, 
 wxID_FRAMEGERENCIARHORARIOCAMPOQUI3, wxID_FRAMEGERENCIARHORARIOCAMPOQUI4, 
 wxID_FRAMEGERENCIARHORARIOCAMPOQUI5, wxID_FRAMEGERENCIARHORARIOCAMPOSEG1, 
 wxID_FRAMEGERENCIARHORARIOCAMPOSEG2, wxID_FRAMEGERENCIARHORARIOCAMPOSEG3, 
 wxID_FRAMEGERENCIARHORARIOCAMPOSEG4, wxID_FRAMEGERENCIARHORARIOCAMPOSEG5, 
 wxID_FRAMEGERENCIARHORARIOCAMPOSEX1, wxID_FRAMEGERENCIARHORARIOCAMPOSEX2, 
 wxID_FRAMEGERENCIARHORARIOCAMPOSEX3, wxID_FRAMEGERENCIARHORARIOCAMPOSEX4, 
 wxID_FRAMEGERENCIARHORARIOCAMPOSEX5, wxID_FRAMEGERENCIARHORARIOCAMPOTER1, 
 wxID_FRAMEGERENCIARHORARIOCAMPOTER2, wxID_FRAMEGERENCIARHORARIOCAMPOTER3, 
 wxID_FRAMEGERENCIARHORARIOCAMPOTER4, wxID_FRAMEGERENCIARHORARIOCAMPOTER5, 
 wxID_FRAMEGERENCIARHORARIOGRADENOITE, 
 wxID_FRAMEGERENCIARHORARIOLISTAPROFESSORES, 
 wxID_FRAMEGERENCIARHORARIOLOGOGERENCIAR, 
 wxID_FRAMEGERENCIARHORARIONOMESELECINEDIA, 
 wxID_FRAMEGERENCIARHORARIONOMESELECIONEAULA, 
 wxID_FRAMEGERENCIARHORARIONOMESERIE, wxID_FRAMEGERENCIARHORARIONOMETURMA, 
 wxID_FRAMEGERENCIARHORARIONOMETURNO, 
 wxID_FRAMEGERENCIARHORARIOPANELGERENCIARGRADEHORARIO, 
 wxID_FRAMEGERENCIARHORARIOPROFESSORESDISPONIVEIS, 
 wxID_FRAMEGERENCIARHORARIOSELECIONADORDIA, 
 wxID_FRAMEGERENCIARHORARIOSELECIONARAULA, 
 wxID_FRAMEGERENCIARHORARIOSELECIONASERIE, 
 wxID_FRAMEGERENCIARHORARIOSELECIONATURMA, 
 wxID_FRAMEGERENCIARHORARIOSELECIONATURNO, 
 wxID_FRAMEGERENCIARHORARIOSTATICLINE1, wxID_FRAMEGERENCIARHORARIOTABELATARDE, 
 wxID_FRAMEGERENCIARHORARIOTEBELAMANHA, 
] = [wx.NewId() for _init_ctrls in range(50)]

class FrameGerenciarHorario(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERENCIARHORARIO,
              name=u'FrameGerenciarHorario', parent=prnt, pos=wx.Point(527,
              190), size=wx.Size(1326, 726), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciar Grade de Horario - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))

        self.panelGerenciarGradeHorario = wx.Panel(id=wxID_FRAMEGERENCIARHORARIOPANELGERENCIARGRADEHORARIO,
              name=u'panelGerenciarGradeHorario', parent=self, pos=wx.Point(0,
              0), size=wx.Size(1310, 688), style=wx.TAB_TRAVERSAL)
        self.panelGerenciarGradeHorario.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Tahoma'))

        self.logoGerenciar = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/logoTurmas.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOLOGOGERENCIAR,
              name=u'logoGerenciar', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(419, 15), size=wx.Size(472, 110), style=0)
        self.logoGerenciar.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERENCIARHORARIOSTATICLINE1,
              name='staticLine1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(295, 147), size=wx.Size(720, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(312, 32), size=wx.Size(48, 48),
              style=wx.BU_AUTODRAW)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMESERIE,
              label=u'Serie:', name=u'nomeSerie',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(21, 199),
              size=wx.Size(41, 19), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMETURNO,
              label=u'Turno:', name=u'nomeTurno',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(193, 199),
              size=wx.Size(49, 19), style=0)

        self.nomeTurma = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMETURMA,
              label=u'Turma:', name=u'nomeTurma',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(359, 200),
              size=wx.Size(53, 19), style=0)

        self.selecionaSerie = wx.Choice(choices=['Selecione a serie',
              'Fundamental I', '          1 Ano', '          2 Ano',
              '          3 Ano', '          4 Ano', '          5 Ano',
              'Fundamental II', '          6 Ano', '          7 Ano',
              '          8 Ano', '          9 Ano', 'Ensino Medio',
              '          1 Ano', '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONASERIE,
              name=u'selecionaSerie', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(33, 229), size=wx.Size(140, 27), style=0)
        self.selecionaSerie.SetStringSelection(u"'Selecione a serie'")
        self.selecionaSerie.SetToolTipString(u'selecionaSerie')

        self.selecionaTurno = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURNO,
              name=u'selecionaTurno', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(202, 228), size=wx.Size(140, 27), style=0)
        self.selecionaTurno.Bind(wx.EVT_CHOICE, self.OnSelecionaTurnoChoice,
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURNO)

        self.selecionaTurma = wx.Choice(choices=["A", "B", "C", "D"],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURMA,
              name=u'selecionaTurma', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(373, 229), size=wx.Size(140, 27), style=0)
        self.selecionaTurma.SetStringSelection(u'"A"')
        self.selecionaTurma.SetThemeEnabled(True)
        self.selecionaTurma.Bind(wx.EVT_CHOICE, self.OnSelecionaTurmaChoice,
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURMA)

        self.caixaSerie = wx.StaticBox(id=wxID_FRAMEGERENCIARHORARIOCAIXASERIE,
              label=u'Selecione a turma', name=u'caixaSerie',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(8, 173),
              size=wx.Size(520, 120), style=0)

        self.caixaProfessor = wx.StaticBox(id=wxID_FRAMEGERENCIARHORARIOCAIXAPROFESSOR,
              label=u'Professores', name=u'caixaProfessor',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(8, 301),
              size=wx.Size(520, 267), style=0)

        self.professoresDisponiveis = wx.StaticBox(id=wxID_FRAMEGERENCIARHORARIOPROFESSORESDISPONIVEIS,
              label=u'Disponiveis', name=u'professoresDisponiveis',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(16, 328),
              size=wx.Size(208, 216), style=0)

        self.listaProfessores = wx.ListBox(choices=[],
              id=wxID_FRAMEGERENCIARHORARIOLISTAPROFESSORES,
              name=u'listaProfessores', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(24, 352), size=wx.Size(192, 184),
              style=wx.NO_BORDER)

        self.nomeSelecineDia = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMESELECINEDIA,
              label=u'Selecione o Dia:', name=u'nomeSelecineDia',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(295, 327),
              size=wx.Size(114, 19), style=0)

        self.nomeSelecioneAula = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMESELECIONEAULA,
              label=u'Selecione a Aula:', name=u'nomeSelecioneAula',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(305, 408),
              size=wx.Size(122, 19), style=0)

        self.botaoAplicar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOAPLICAR,
              label=u' Aplicar ', name=u'botaoAplicar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(414, 519),
              size=wx.Size(88, 30), style=0)

        self.botaoSalvar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOSALVAR,
              label=u'   Salvar   ', name=u'botaoSalvar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(1168, 632),
              size=wx.Size(112, 30), style=0)

        self.botaoCancelar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOCANCELAR,
              label=u' Cancelar ', name=u'botaoCancelar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(304, 520),
              size=wx.Size(92, 30), style=0)

        self.selecionarAula = wx.Choice(choices=["1", "2", "3", "4", "5"],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONARAULA,
              name=u'selecionarAula', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(306, 432), size=wx.Size(140, 27), style=0)

        self.selecionadorDia = wx.Choice(choices=["Segunda", "Terca", "Quarta",
              "Quinta", "Sexta"], id=wxID_FRAMEGERENCIARHORARIOSELECIONADORDIA,
              name=u'selecionadorDia', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(303, 359), size=wx.Size(140, 27), style=0)

        self.campoSex5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX5,
              name=u'campoSex5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 528), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoSex4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX4,
              name=u'campoSex4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 468), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoSex3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX3,
              name=u'campoSex3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 419), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoSex2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX2,
              name=u'campoSex2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 364), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoSex1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX1,
              name=u'campoSex1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 313), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQui4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI4,
              name=u'campoQui4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 468), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQui3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI3,
              name=u'campoQui3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 419), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQui2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI2,
              name=u'campoQui2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 364), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQui1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI1,
              name=u'campoQui1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 313), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQui5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI5,
              name=u'campoQui5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 528), size=wx.Size(100, 27),
              style=wx.NO_BORDER, value=u'')

        self.campoQua5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA5,
              name=u'campoQua5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 528), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoQua4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA4,
              name=u'campoQua4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 468), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoQua3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA3,
              name=u'campoQua3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 419), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoQua2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA2,
              name=u'campoQua2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 364), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoQua1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA1,
              name=u'campoQua1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 313), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoTer1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER1,
              name=u'campoTer1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 313), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoTer2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER2,
              name=u'campoTer2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 364), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoTer3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER3,
              name=u'campoTer3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 419), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoTer4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER4,
              name=u'campoTer4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 468), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoTer5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER5,
              name=u'campoTer5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 528), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoSeg5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG5,
              name=u'campoSeg5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 528), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoSeg4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG4,
              name=u'campoSeg4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 468), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoSeg3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG3,
              name=u'campoSeg3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 419), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoSeg2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG2,
              name=u'campoSeg2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 364), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.campoSeg1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG1,
              name=u'campoSeg1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 313), size=wx.Size(100, 27), style=wx.NO_BORDER,
              value=u'')

        self.tebelaManha = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/gradeManha.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOTEBELAMANHA,
              name=u'tebelaManha', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(568, 240), size=wx.Size(722, 332), style=0)

        self.tabelaTarde = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/gradeTarde.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOTABELATARDE,
              name=u'tabelaTarde', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(570, 240), size=wx.Size(719, 336), style=0)

        self.gradeNoite = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/gradeNoite.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOGRADENOITE,
              name=u'gradeNoite', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(570, 240), size=wx.Size(719, 336), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGrid1GridRowSize(self, event):
        event.Skip()

    def OnSelecionaTurmaChoice(self, event):
        event.Skip()

    def OnSelecionaTurnoChoice(self, event):
        event.Skip()
