#Boa:Frame:FrameGerTurmaAlunos

import wx
import wx.lib.buttons
import sys

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

from newAluno import Aluno
from newTurma import Turma
sys.path[0] = original

def create(parent):
    return FrameGerTurmaAlunos(parent)

[wxID_FRAMEGERTURMAALUNOS, wxID_FRAMEGERTURMAALUNOSBOTAOADDDISCIPLINA, 
 wxID_FRAMEGERTURMAALUNOSBOTAOADICIONARALUNO, 
 wxID_FRAMEGERTURMAALUNOSBOTAODELDISCIPLINA, 
 wxID_FRAMEGERTURMAALUNOSBOTAOEXCLUIRTURMA, 
 wxID_FRAMEGERTURMAALUNOSBOTAOREMOVERALUNO, 
 wxID_FRAMEGERTURMAALUNOSBOTAOSALVARTURMA, 
 wxID_FRAMEGERTURMAALUNOSBOTAOVOLTAR, wxID_FRAMEGERTURMAALUNOSCAIXAALUNOS, 
 wxID_FRAMEGERTURMAALUNOSCAIXAALUNOSTODOS, 
 wxID_FRAMEGERTURMAALUNOSCAIXAALUNOSTURMA, 
 wxID_FRAMEGERTURMAALUNOSCAIXADISCIPLINAS, 
 wxID_FRAMEGERTURMAALUNOSCAIXADISCIPLINASSELECIONADAS, 
 wxID_FRAMEGERTURMAALUNOSCAIXATODASDISCIPLINAS, 
 wxID_FRAMEGERTURMAALUNOSCHOICESERIE, wxID_FRAMEGERTURMAALUNOSCHOICETURMA, 
 wxID_FRAMEGERTURMAALUNOSCHOICETURNO, wxID_FRAMEGERTURMAALUNOSERROTEXT, 
 wxID_FRAMEGERTURMAALUNOSLISTAALUNOSSELECIONADOS, 
 wxID_FRAMEGERTURMAALUNOSLISTAALUNOSTODOS, 
 wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASSELECIONADAS, 
 wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASTODAS, 
 wxID_FRAMEGERTURMAALUNOSLOGOACADEMIC, wxID_FRAMEGERTURMAALUNOSNOMESERIE, 
 wxID_FRAMEGERTURMAALUNOSNOMETURMA, wxID_FRAMEGERTURMAALUNOSNOMETURNO, 
 wxID_FRAMEGERTURMAALUNOSPANEL1, wxID_FRAMEGERTURMAALUNOSSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(28)]

class FrameGerTurmaAlunos(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERTURMAALUNOS,
              name=u'FrameGerTurmaAlunos', parent=prnt, pos=wx.Point(138, 7),
              size=wx.Size(1318, 722), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gereciamento de Turmas - Alunos')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetHelpText(u'')
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGERTURMAALUNOSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1310, 688),
              style=wx.TAB_TRAVERSAL)

        self.caixaAlunosTurma = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXAALUNOSTURMA,
              label=u'Alunos Na Turma:', name=u'caixaAlunosTurma',
              parent=self.panel1, pos=wx.Point(782, 216), size=wx.Size(256,
              184), style=0)

        self.choiceSerie = wx.Choice(choices=['Selecione a serie',
              'Fundamental I', '          1 Ano', '          2 Ano',
              '          3 Ano', '          4 Ano', '          5 Ano',
              'Fundamental II', '          6 Ano', '          7 Ano',
              '          8 Ano', '          9 Ano', 'Ensino Medio',
              '          1 Ano', '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERTURMAALUNOSCHOICESERIE, name=u'choiceSerie',
              parent=self.panel1, pos=wx.Point(432, 173), size=wx.Size(130, 21),
              style=0)
        self.choiceSerie.SetStringSelection(u'Selecione a serie')
        self.choiceSerie.Bind(wx.EVT_CHOICE, self.OnChoiceSerie,
              id=wxID_FRAMEGERTURMAALUNOSCHOICESERIE)

        self.choiceTurno = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERTURMAALUNOSCHOICETURNO, name=u'choiceTurno',
              parent=self.panel1, pos=wx.Point(600, 173), size=wx.Size(130, 21),
              style=0)
        self.choiceTurno.SetStringSelection(u'Manha')
        self.choiceTurno.Bind(wx.EVT_CHOICE, self.OnChoiceTurnoChoice,
              id=wxID_FRAMEGERTURMAALUNOSCHOICETURNO)

        self.nomeTurma = wx.StaticText(id=wxID_FRAMEGERTURMAALUNOSNOMETURMA,
              label=u'Turma:', name=u'nomeTurma', parent=self.panel1,
              pos=wx.Point(752, 156), size=wx.Size(35, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERTURMAALUNOSNOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.panel1,
              pos=wx.Point(432, 157), size=wx.Size(29, 13), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERTURMAALUNOSNOMETURNO,
              label=u'Turno:', name=u'nomeTurno', parent=self.panel1,
              pos=wx.Point(602, 157), size=wx.Size(33, 13), style=0)

        self.listaDisciplinasSelecionadas = wx.ListBox(choices=[],
              id=wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASSELECIONADAS,
              name=u'listaDisciplinasSelecionadas', parent=self.panel1,
              pos=wx.Point(791, 475), size=wx.Size(244, 136),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaDisciplinasSelecionadas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnDiscNaTurmaListboxDclick,
              id=wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASSELECIONADAS)

        self.listaAlunosSelecionados = wx.ListBox(choices=[],
              id=wxID_FRAMEGERTURMAALUNOSLISTAALUNOSSELECIONADOS,
              name=u'listaAlunosSelecionados', parent=self.panel1,
              pos=wx.Point(789, 234), size=wx.Size(241, 160),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaAlunosSelecionados.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnAlunosNaTurmaListboxDclick,
              id=wxID_FRAMEGERTURMAALUNOSLISTAALUNOSSELECIONADOS)

        self.caixaAlunosTodos = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXAALUNOSTODOS,
              label=u'Alunos Matriculados', name=u'caixaAlunosTodos',
              parent=self.panel1, pos=wx.Point(285, 216), size=wx.Size(256,
              184), style=0)

        self.botaoAdicionarAluno = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/add_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMAALUNOSBOTAOADICIONARALUNO,
              name=u'botaoAdicionarAluno', parent=self.panel1, pos=wx.Point(635,
              254), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoAdicionarAluno.Center(wx.HORIZONTAL)
        self.botaoAdicionarAluno.Bind(wx.EVT_BUTTON,
              self.OnBotaoAdicionarAlunoButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOADICIONARALUNO)

        self.botaoRemoverAluno = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/del_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSBOTAOREMOVERALUNO,
              name=u'botaoRemoverAluno', parent=self.panel1, pos=wx.Point(635,
              332), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoRemoverAluno.Center(wx.HORIZONTAL)
        self.botaoRemoverAluno.Bind(wx.EVT_BUTTON,
              self.OnBotaoRemoverAlunoButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOREMOVERALUNO)

        self.botaoSalvarTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSBOTAOSALVARTURMA,
              label=u'    Salvar   ', name=u'botaoSalvarTurma',
              parent=self.panel1, pos=wx.Point(1204, 643), size=wx.Size(76, 30),
              style=0)

        self.botaoExcluirTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSBOTAOEXCLUIRTURMA,
              label=u'   Excluir    ', name=u'botaoExcluirTurma',
              parent=self.panel1, pos=wx.Point(1112, 644), size=wx.Size(76, 30),
              style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERTURMAALUNOSSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(251, 144),
              size=wx.Size(808, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.logoAcademic = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pqueno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSLOGOACADEMIC,
              name=u'logoAcademic', parent=self.panel1, pos=wx.Point(518, 16),
              size=wx.Size(274, 112), style=0)
        self.logoAcademic.Center(wx.HORIZONTAL)

        self.choiceTurma = wx.Choice(choices=["A", "B", "C", "D", "E"],
              id=wxID_FRAMEGERTURMAALUNOSCHOICETURMA, name=u'choiceTurma',
              parent=self.panel1, pos=wx.Point(754, 173), size=wx.Size(130, 21),
              style=0)
        self.choiceTurma.Bind(wx.EVT_CHOICE, self.OnChoiceTurmaChoice,
              id=wxID_FRAMEGERTURMAALUNOSCHOICETURMA)

        self.caixaDisciplinasSelecionadas = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXADISCIPLINASSELECIONADAS,
              label=u'Disciplinas Na Turma',
              name=u'caixaDisciplinasSelecionadas', parent=self.panel1,
              pos=wx.Point(781, 457), size=wx.Size(264, 160), style=0)

        self.listaAlunosTodos = wx.ListBox(choices=[],
              id=wxID_FRAMEGERTURMAALUNOSLISTAALUNOSTODOS,
              name=u'listaAlunosTodos', parent=self.panel1, pos=wx.Point(290,
              234), size=wx.Size(244, 160), style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaAlunosTodos.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnAlunosMatriculadosListboxDclick,
              id=wxID_FRAMEGERTURMAALUNOSLISTAALUNOSTODOS)

        self.caixaTodasDisciplinas = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXATODASDISCIPLINAS,
              label=u'Disciplinas Cadastradas', name=u'caixaTodasDisciplinas',
              parent=self.panel1, pos=wx.Point(280, 457), size=wx.Size(264,
              160), style=0)

        self.listaDisciplinasTodas = wx.ListBox(choices=[],
              id=wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASTODAS,
              name=u'listaDisciplinasTodas', parent=self.panel1,
              pos=wx.Point(290, 475), size=wx.Size(244, 136),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaDisciplinasTodas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnDiscCadastradasListboxDclick,
              id=wxID_FRAMEGERTURMAALUNOSLISTADISCIPLINASTODAS)

        self.botaoAddDisciplina = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/add_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMAALUNOSBOTAOADDDISCIPLINA,
              name=u'botaoAddDisciplina', parent=self.panel1, pos=wx.Point(635,
              481), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoAddDisciplina.Center(wx.HORIZONTAL)
        self.botaoAddDisciplina.Bind(wx.EVT_BUTTON,
              self.OnBotaoAddDisciplinaButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOADDDISCIPLINA)

        self.botaoDelDisciplina = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/del_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMAALUNOSBOTAODELDISCIPLINA,
              name=u'botaoDelDisciplina', parent=self.panel1, pos=wx.Point(635,
              559), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoDelDisciplina.Center(wx.HORIZONTAL)
        self.botaoDelDisciplina.Bind(wx.EVT_BUTTON,
              self.OnBotaoDelDisciplinaButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAODELDISCIPLINA)

        self.caixaAlunos = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXAALUNOS,
              label=u'GerenciarAlunos', name=u'caixaAlunos', parent=self.panel1,
              pos=wx.Point(278, 202), size=wx.Size(768, 201), style=0)

        self.caixaDisciplinas = wx.StaticBox(id=wxID_FRAMEGERTURMAALUNOSCAIXADISCIPLINAS,
              label=u'Gerenciar Disciplinas', name=u'caixaDisciplinas',
              parent=self.panel1, pos=wx.Point(275, 440), size=wx.Size(775,
              184), style=0)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.panel1, pos=wx.Point(304, 32),
              size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOVOLTAR)

        self.erroText = wx.StaticText(id=wxID_FRAMEGERTURMAALUNOSERROTEXT,
              label=u'                                                                                                             ',
              name=u'erroText', parent=self.panel1, pos=wx.Point(483, 640),
              size=wx.Size(436, 24), style=wx.ALIGN_CENTRE)
        self.erroText.Center(wx.HORIZONTAL)
        self.erroText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnDiscNaTurmaListboxDclick(self, event):
        event.Skip()

    def OnProfListBoxListbox(self, event):
        event.Skip()

    def OnBotaoAdicionarAlunoButton(self, event):
        event.Skip()

    def OnChoiceSerie(self, event):
        event.Skip()

    def OnChoiceTurnoChoice(self, event):
        event.Skip()

    def OnAlunosNaTurmaListboxDclick(self, event):
        event.Skip()

    def OnBotaoRemoverAlunoButton(self, event):
        event.Skip()

    def OnChoiceTurmaChoice(self, event):
        event.Skip()

    def OnAlunosMatriculadosListboxDclick(self, event):
        event.Skip()

    def OnDiscCadastradasListboxDclick(self, event):
        event.Skip()

    def OnBotaoAddDisciplinaButton(self, event):
        event.Skip()

    def OnBotaoDelDisciplinaButton(self, event):
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        event.Skip()
