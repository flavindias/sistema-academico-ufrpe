#Boa:Frame:FrameGerenciarHorario

import wx
import wx.lib.buttons
import wx.grid
import sys
import ponte

original = sys.path[0]
lista = sys.path[0].split('\\')
temp = ''
for i in range(len(lista)):
    if i != len(lista)-1:
        temp += lista[i]
        temp += '\\'
    else:
        temp += 'Modules'
sys.path[0] = temp

from newTurma import Turma
from newProfessor import Professor
from newDisciplina import Disciplina
sys.path[0] = original

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
 wxID_FRAMEGERENCIARHORARIOERROTEXT, wxID_FRAMEGERENCIARHORARIOHORARIOCOBRIR, 
 wxID_FRAMEGERENCIARHORARIOHORARIOMANHA, 
 wxID_FRAMEGERENCIARHORARIOHORARIONOITE, 
 wxID_FRAMEGERENCIARHORARIOHORARIOTARDE, 
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
 wxID_FRAMEGERENCIARHORARIOSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(52)]

class FrameGerenciarHorario(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERENCIARHORARIO,
              name=u'FrameGerenciarHorario', parent=prnt, pos=wx.Point(40, 2),
              size=wx.Size(1326, 726), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciar Grade de Horario - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)

        self.panelGerenciarGradeHorario = wx.Panel(id=wxID_FRAMEGERENCIARHORARIOPANELGERENCIARGRADEHORARIO,
              name=u'panelGerenciarGradeHorario', parent=self, pos=wx.Point(0,
              0), size=wx.Size(1310, 688), style=wx.TAB_TRAVERSAL)
        self.panelGerenciarGradeHorario.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Tahoma'))
        self.panelGerenciarGradeHorario.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.panelGerenciarGradeHorario.SetBackgroundColour(wx.Colour(255, 255,
              255))

        self.horarioCobrir = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/horarioCobrir.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOHORARIOCOBRIR,
              name=u'horarioCobrir', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(566, 235), size=wx.Size(719, 336), style=0)

        self.logoGerenciar = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logoTurmas.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOLOGOGERENCIAR,
              name=u'logoGerenciar', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(419, 15), size=wx.Size(472, 110), style=0)
        self.logoGerenciar.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERENCIARHORARIOSTATICLINE1,
              name='staticLine1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(295, 147), size=wx.Size(720, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
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
        self.selecionaSerie.SetStringSelection(u'Selecione a serie')
        self.selecionaSerie.SetToolTipString(u'selecionaSerie')
        self.selecionaSerie.Bind(wx.EVT_CHOICE, self.OnSelecionaSerieChoice,
              id=wxID_FRAMEGERENCIARHORARIOSELECIONASERIE)

        self.selecionaTurno = wx.Choice(choices=["Selecione o Turno", "Manha",
              "Tarde", "Noite"], id=wxID_FRAMEGERENCIARHORARIOSELECIONATURNO,
              name=u'selecionaTurno', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(202, 228), size=wx.Size(140, 27), style=0)
        self.selecionaTurno.SetStringSelection(u'Selecione o Turno')
        self.selecionaTurno.Bind(wx.EVT_CHOICE, self.OnSelecionaTurnoChoice,
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURNO)

        self.selecionaTurma = wx.Choice(choices=["A", "B", "C", "D", "E"],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONATURMA,
              name=u'selecionaTurma', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(373, 229), size=wx.Size(140, 27), style=0)
        self.selecionaTurma.SetStringSelection(u'A')
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
        self.listaProfessores.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.nomeSelecineDia = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMESELECINEDIA,
              label=u'Selecione o Dia:', name=u'nomeSelecineDia',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(295, 327),
              size=wx.Size(114, 19), style=0)

        self.nomeSelecioneAula = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIONOMESELECIONEAULA,
              label=u'Selecione a Aula:', name=u'nomeSelecioneAula',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(298, 408),
              size=wx.Size(122, 19), style=0)

        self.botaoAplicar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOAPLICAR,
              label=u' Aplicar ', name=u'botaoAplicar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(414, 519),
              size=wx.Size(88, 30), style=0)
        self.botaoAplicar.Bind(wx.EVT_BUTTON, self.OnBotaoAplicarButton,
              id=wxID_FRAMEGERENCIARHORARIOBOTAOAPLICAR)

        self.botaoSalvar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOSALVAR,
              label=u'   Salvar   ', name=u'botaoSalvar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(1168, 632),
              size=wx.Size(112, 30), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMEGERENCIARHORARIOBOTAOSALVAR)

        self.botaoCancelar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOBOTAOCANCELAR,
              label=u' Cancelar ', name=u'botaoCancelar',
              parent=self.panelGerenciarGradeHorario, pos=wx.Point(304, 520),
              size=wx.Size(92, 30), style=0)
        self.botaoCancelar.Bind(wx.EVT_BUTTON, self.OnBotaoCancelarButton,
              id=wxID_FRAMEGERENCIARHORARIOBOTAOCANCELAR)

        self.selecionarAula = wx.Choice(choices=["1", "2", "3", "4", "5"],
              id=wxID_FRAMEGERENCIARHORARIOSELECIONARAULA,
              name=u'selecionarAula', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(306, 432), size=wx.Size(140, 27), style=0)
        self.selecionarAula.SetStringSelection(u'1')

        self.selecionadorDia = wx.Choice(choices=["Segunda", "Terca", "Quarta",
              "Quinta", "Sexta"], id=wxID_FRAMEGERENCIARHORARIOSELECIONADORDIA,
              name=u'selecionadorDia', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(303, 359), size=wx.Size(140, 27), style=0)
        self.selecionadorDia.SetStringSelection(u'Segunda')

        self.campoSex5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX5,
              name=u'campoSex5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 515), size=wx.Size(100, 44),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSex5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSex4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX4,
              name=u'campoSex4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 462), size=wx.Size(100, 47),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSex4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSex3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX3,
              name=u'campoSex3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 408), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSex3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSex2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX2,
              name=u'campoSex2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 353), size=wx.Size(100, 47),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSex2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSex1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEX1,
              name=u'campoSex1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1169, 299), size=wx.Size(100, 45),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSex1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQui4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI4,
              name=u'campoQui4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 461), size=wx.Size(100, 50),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQui4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQui3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI3,
              name=u'campoQui3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 408), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQui3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQui2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI2,
              name=u'campoQui2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 352), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQui2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQui1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI1,
              name=u'campoQui1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 300), size=wx.Size(100, 45),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQui1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQui5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUI5,
              name=u'campoQui5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(1053, 516), size=wx.Size(100, 46),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQui5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQua5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA5,
              name=u'campoQua5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 516), size=wx.Size(100, 44),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQua5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQua4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA4,
              name=u'campoQua4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 461), size=wx.Size(100, 44),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQua4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.campoQua4.SetToolTipString(u'campoQua4')

        self.campoQua3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA3,
              name=u'campoQua3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 408), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQua3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQua2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA2,
              name=u'campoQua2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 353), size=wx.Size(100, 47),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQua2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoQua1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOQUA1,
              name=u'campoQua1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(937, 301), size=wx.Size(100, 45),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoQua1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoTer1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER1,
              name=u'campoTer1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 299), size=wx.Size(100, 45),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoTer1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoTer2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER2,
              name=u'campoTer2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 352), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoTer2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoTer3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER3,
              name=u'campoTer3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 408), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoTer3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoTer4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER4,
              name=u'campoTer4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 460), size=wx.Size(100, 52),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoTer4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoTer5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOTER5,
              name=u'campoTer5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(819, 516), size=wx.Size(100, 46),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoTer5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSeg5 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG5,
              name=u'campoSeg5', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(701, 514), size=wx.Size(100, 46),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSeg5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSeg4 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG4,
              name=u'campoSeg4', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(702, 464), size=wx.Size(100, 45),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSeg4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSeg3 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG3,
              name=u'campoSeg3', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(703, 408), size=wx.Size(100, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSeg3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSeg2 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG2,
              name=u'campoSeg2', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(699, 352), size=wx.Size(105, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSeg2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.campoSeg1 = wx.TextCtrl(id=wxID_FRAMEGERENCIARHORARIOCAMPOSEG1,
              name=u'campoSeg1', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(699, 303), size=wx.Size(105, 41),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, value=u'')
        self.campoSeg1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.horarioManha = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/gradeManha.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOHORARIOMANHA,
              name=u'horarioManha', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(568, 240), size=wx.Size(722, 332), style=0)
        self.horarioManha.Show(False)

        self.horarioTarde = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/gradeTarde.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOHORARIOTARDE,
              name=u'horarioTarde', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(570, 240), size=wx.Size(719, 336), style=0)
        self.horarioTarde.Show(False)

        self.horarioNoite = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/gradeNoite.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIARHORARIOHORARIONOITE,
              name=u'horarioNoite', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(570, 240), size=wx.Size(719, 336), style=0)
        self.horarioNoite.Show(False)

        self.erroText = wx.StaticText(id=wxID_FRAMEGERENCIARHORARIOERROTEXT,
              label=u'                                                                                                              ',
              name=u'erroText', parent=self.panelGerenciarGradeHorario,
              pos=wx.Point(435, 608), size=wx.Size(440, 18),
              style=wx.ALIGN_CENTRE)
        self.erroText.Center(wx.HORIZONTAL)
        self.erroText.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGrid1GridRowSize(self, event):
        event.Skip()
        
    def OnSelecionaSerieChoice(self, event):
        self.menuEsquerda()
        event.Skip()

    def OnSelecionaTurmaChoice(self, event):
        self.menuEsquerda()
        event.Skip()

    def OnSelecionaTurnoChoice(self, event):
        self.menuEsquerda()
        if self.selecionaTurno.GetSelection()  == 1:
            self.horarioManha.Show(True)
            self.horarioNoite.Show(False)
            self.horarioTarde.Show(False)

        elif self.selecionaTurno.GetSelection()  == 2:
            self.horarioManha.Show(False)
            self.horarioNoite.Show(False)
            self.horarioTarde.Show(True)

        elif self.selecionaTurno.GetSelection()  == 3:
            self.horarioManha.Show(False)
            self.horarioNoite.Show(True)
            self.horarioTarde.Show(False)
        else:
            self.horarioCobrir.Show(True)
            self.horarioManha.Show(False)
            self.horarioTarde.Show(False)
            self.horarioNoite.Show(False)
        event.Skip()

    def OnBotaoAplicarButton(self, event):
        if self.listaProfessores.GetSelection()!=-1:
            self.__aula = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
            self.__aula = self.__aula[self.selecionadorDia.GetSelection()]
            self.__aula = self.__aula[self.selecionarAula.GetSelection()]
            self.__valor = lista[self.listaProfessores.GetSelection()].split('-')
            if turma.editarHorario(turma.getTurma(), self.__aula, valor[0]):
                turma.carregar(turma.getTurma())
                for self.__i in range(len(listaGrid)):
                    listaGrid[self.__i].SetLabel('')
        event.Skip()

    def OnBotaoSalvarButton(self, event):
        event.Skip()

    def OnBotaoCancelarButton(self, event):
        event.Skip()

    def menuEsquerda(self):
        turma = Turma()
        disciplina = Disciplina()
        professor = Professor()
        self.__turma = ['A','B','C','D','E']
        self.__turma = self.__turma[self.selecionaTurma.GetSelection()]
        self.__serie = [None,None,'F1','F2','F3','F4','F5',None,'F6','F7','F8','F9',None,'M1','M2','M3']
        self.__serie = self.__serie[self.selecionaSerie.GetSelection()]
        self.__turno = ['M','T','N']
        listaGrid = [self.campoSeg1, self.campoSeg2, self.campoSeg3, self.campoSeg4, self.campoSeg5, self.campoTer1, self.campoTer2, self.campoTer3, self.campoTer4, self.campoTer5, self.campoQua1, self.campoQua2, self.campoQua3, self.campoQua4, self.campoQua5, self.campoQui1, self.campoQui2, self.campoQui3, self.campoQui4, self.campoQui5, self.campoSex1, self.campoSex2, self.campoSex3, self.campoSex4, self.campoSex5]
        if self.__serie != None:
            if turma.carregar(self.__serie+self.__turma):
                self.__turno = self.__turno.index(turma.getTurno())
                if self.selecionaTurno.GetSelection() == self.__turno+1:
                    lista=[]
                    if turma.getDisciplina1() != 'None':
                        lista.append(turma.getDisciplina1())
                    if turma.getDisciplina2() != 'None':
                        lista.append(turma.getDisciplina2())
                    if turma.getDisciplina3() != 'None':
                        lista.append(turma.getDisciplina3())
                    if turma.getDisciplina4() != 'None':
                        lista.append(turma.getDisciplina4())
                    if turma.getDisciplina5() != 'None':
                        lista.append(turma.getDisciplina5())
                    if turma.getDisciplina6() != 'None':
                        lista.append(turma.getDisciplina6())
                    for self.__i in range(len(lista)):
                        disciplina.carregar(lista[self.__i])
                        professor.carregar(disciplina.getProfessor())
                        lista[self.__i] += '-'+professor.getNome()
                    self.listaProfessores.Set(lista)
                    self.__a = turma.addHorario(turma.getTurma())
                    if self.__a:
                        self.erroText.SetLabel('Carregado com sucesso. Sem horario definido.')
                    else:
                        self.__result = turma.getHorario()
                        for self.__i in range(len(self.__result)-1):
                            if self.__result[self.__i+1] != None:
                                listaGrid[self.__i].SetLabel(self.__result[self.__i+1])                                
                        self.erroText.SetLabel('Carregado com sucesso')
                else:
                    self.erroText.SetLabel('Selecione o turno correto')
                    self.listaProfessores.Set([])
                    for self.__i in range(len(listaGrid)):
                        listaGrid[self.__i].SetLabel('')
            else:
                self.erroText.SetLabel('Turma nao encontrada')
                self.listaProfessores.Set([])
                for self.__i in range(len(listaGrid)):
                    listaGrid[self.__i].SetLabel('')
        else:
            self.erroText.SetLabel('')
            self.listaProfessores.Set([])
            for self.__i in range(len(listaGrid)):
                listaGrid[self.__i].SetLabel('')
