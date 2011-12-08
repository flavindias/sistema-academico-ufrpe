#Boa:Frame:Frame1

import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BOTAOADDDISCIPLINA, wxID_FRAME1BOTAOADICIONARALUNO, 
 wxID_FRAME1BOTAODELDISCIPLINA, wxID_FRAME1BOTAOEXCLUIRTURMA, 
 wxID_FRAME1BOTAOREMOVERALUNO, wxID_FRAME1BOTAOSALVARTURMA, 
 wxID_FRAME1BOTAOVOLTAR, wxID_FRAME1CAIXAALUNOS, wxID_FRAME1CAIXAALUNOSTODOS, 
 wxID_FRAME1CAIXAALUNOSTURMA, wxID_FRAME1CAIXADISCIPLINAS, 
 wxID_FRAME1CAIXADISCIPLINASSELECIONADAS, wxID_FRAME1CAIXATODASDISCIPLINAS, 
 wxID_FRAME1CHOICE1, wxID_FRAME1CHOICE2, wxID_FRAME1ESCOLHATURMA, 
 wxID_FRAME1LISTAALUNOSSELECIONADOS, wxID_FRAME1LISTAALUNOSTODOS, 
 wxID_FRAME1LISTADISCIPLINASSELECIONADAS, wxID_FRAME1LISTADISCIPLINASTODAS, 
 wxID_FRAME1LOGOACADEMIC, wxID_FRAME1NOMESERIE, wxID_FRAME1NOMETURMA, 
 wxID_FRAME1NOMETURNO, wxID_FRAME1PANEL1, wxID_FRAME1STATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(27)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(537, 245), size=wx.Size(1326, 726),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gereciamento de Turmas - Alunos')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetHelpText(u'')
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1310, 688),
              style=wx.TAB_TRAVERSAL)

        self.caixaAlunosTurma = wx.StaticBox(id=wxID_FRAME1CAIXAALUNOSTURMA,
              label=u'Alunos Na Turma:', name=u'caixaAlunosTurma',
              parent=self.panel1, pos=wx.Point(782, 216), size=wx.Size(256,
              184), style=0)

        self.choice1 = wx.Choice(choices=['Selecione a serie', 'Fundamental I',
              '          1 Ano', '          2 Ano', '          3 Ano',
              '          4 Ano', '          5 Ano', 'Fundamental II',
              '          6 Ano', '          7 Ano', '          8 Ano',
              '          9 Ano', 'Ensino Medio', '          1 Ano',
              '          2 Ano', '          3 Ano'], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(432, 173),
              size=wx.Size(130, 21), style=0)
        self.choice1.SetStringSelection(u'Selecione a serie')

        self.choice2 = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAME1CHOICE2, name='choice2', parent=self.panel1,
              pos=wx.Point(600, 173), size=wx.Size(130, 21), style=0)
        self.choice2.SetStringSelection(u'Manha')

        self.nomeTurma = wx.StaticText(id=wxID_FRAME1NOMETURMA, label=u'Turma:',
              name=u'nomeTurma', parent=self.panel1, pos=wx.Point(752, 156),
              size=wx.Size(35, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAME1NOMESERIE, label=u'Serie:',
              name=u'nomeSerie', parent=self.panel1, pos=wx.Point(432, 157),
              size=wx.Size(29, 13), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAME1NOMETURNO, label=u'Turno:',
              name=u'nomeTurno', parent=self.panel1, pos=wx.Point(602, 157),
              size=wx.Size(33, 13), style=0)

        self.listaDisciplinasSelecionadas = wx.ListBox(choices=[],
              id=wxID_FRAME1LISTADISCIPLINASSELECIONADAS,
              name=u'listaDisciplinasSelecionadas', parent=self.panel1,
              pos=wx.Point(791, 475), size=wx.Size(244, 136),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaDisciplinasSelecionadas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick,
              id=wxID_FRAME1LISTADISCIPLINASSELECIONADAS)
        self.listaDisciplinasSelecionadas.Bind(wx.EVT_LISTBOX,
              self.OnProfListBoxListbox,
              id=wxID_FRAME1LISTADISCIPLINASSELECIONADAS)

        self.listaAlunosSelecionados = wx.ListBox(choices=[],
              id=wxID_FRAME1LISTAALUNOSSELECIONADOS,
              name=u'listaAlunosSelecionados', parent=self.panel1,
              pos=wx.Point(789, 234), size=wx.Size(241, 160),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaAlunosSelecionados.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick,
              id=wxID_FRAME1LISTAALUNOSSELECIONADOS)
        self.listaAlunosSelecionados.Bind(wx.EVT_LISTBOX,
              self.OnProfListBoxListbox, id=wxID_FRAME1LISTAALUNOSSELECIONADOS)

        self.caixaAlunosTodos = wx.StaticBox(id=wxID_FRAME1CAIXAALUNOSTODOS,
              label=u'Alunos Matriculados', name=u'caixaAlunosTodos',
              parent=self.panel1, pos=wx.Point(285, 216), size=wx.Size(256,
              184), style=0)

        self.botaoAdicionarAluno = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/add_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOADICIONARALUNO,
              name=u'botaoAdicionarAluno', parent=self.panel1, pos=wx.Point(635,
              254), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoAdicionarAluno.Center(wx.HORIZONTAL)
        self.botaoAdicionarAluno.Bind(wx.EVT_BUTTON,
              self.OnBotaoAdicionarButton, id=wxID_FRAME1BOTAOADICIONARALUNO)

        self.botaoRemoverAluno = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/del_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOREMOVERALUNO,
              name=u'botaoRemoverAluno', parent=self.panel1, pos=wx.Point(635,
              332), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoRemoverAluno.Center(wx.HORIZONTAL)

        self.botaoSalvarTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOSALVARTURMA,
              label=u'    Salvar   ', name=u'botaoSalvarTurma',
              parent=self.panel1, pos=wx.Point(1204, 643), size=wx.Size(76, 30),
              style=0)

        self.botaoExcluirTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOEXCLUIRTURMA,
              label=u'   Excluir    ', name=u'botaoExcluirTurma',
              parent=self.panel1, pos=wx.Point(1112, 644), size=wx.Size(76, 30),
              style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(251, 144),
              size=wx.Size(808, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.logoAcademic = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pqueno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1LOGOACADEMIC,
              name=u'logoAcademic', parent=self.panel1, pos=wx.Point(518, 16),
              size=wx.Size(274, 112), style=0)
        self.logoAcademic.Center(wx.HORIZONTAL)

        self.escolhaTurma = wx.Choice(choices=["A", "B", "C", "D", "E"],
              id=wxID_FRAME1ESCOLHATURMA, name=u'escolhaTurma',
              parent=self.panel1, pos=wx.Point(754, 173), size=wx.Size(130, 21),
              style=0)

        self.caixaDisciplinasSelecionadas = wx.StaticBox(id=wxID_FRAME1CAIXADISCIPLINASSELECIONADAS,
              label=u'Disciplinas Cadastradas',
              name=u'caixaDisciplinasSelecionadas', parent=self.panel1,
              pos=wx.Point(781, 457), size=wx.Size(264, 160), style=0)

        self.listaAlunosTodos = wx.ListBox(choices=[],
              id=wxID_FRAME1LISTAALUNOSTODOS, name=u'listaAlunosTodos',
              parent=self.panel1, pos=wx.Point(290, 234), size=wx.Size(244,
              160), style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaAlunosTodos.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick, id=wxID_FRAME1LISTBOX2)
        self.listaAlunosTodos.Bind(wx.EVT_LISTBOX, self.OnProfListBoxListbox,
              id=wxID_FRAME1LISTBOX2)

        self.caixaTodasDisciplinas = wx.StaticBox(id=wxID_FRAME1CAIXATODASDISCIPLINAS,
              label=u'Disciplinas Cadastradas', name=u'caixaTodasDisciplinas',
              parent=self.panel1, pos=wx.Point(280, 457), size=wx.Size(264,
              160), style=0)

        self.listaDisciplinasTodas = wx.ListBox(choices=[],
              id=wxID_FRAME1LISTADISCIPLINASTODAS,
              name=u'listaDisciplinasTodas', parent=self.panel1,
              pos=wx.Point(290, 475), size=wx.Size(244, 136),
              style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaDisciplinasTodas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick,
              id=wxID_FRAME1LISTADISCIPLINASTODAS)
        self.listaDisciplinasTodas.Bind(wx.EVT_LISTBOX,
              self.OnProfListBoxListbox, id=wxID_FRAME1LISTADISCIPLINASTODAS)

        self.botaoAddDisciplina = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/add_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOADDDISCIPLINA,
              name=u'botaoAddDisciplina', parent=self.panel1, pos=wx.Point(635,
              481), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoAddDisciplina.Center(wx.HORIZONTAL)

        self.botaoDelDisciplina = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/del_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAODELDISCIPLINA,
              name=u'botaoDelDisciplina', parent=self.panel1, pos=wx.Point(635,
              559), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoDelDisciplina.Center(wx.HORIZONTAL)

        self.caixaAlunos = wx.StaticBox(id=wxID_FRAME1CAIXAALUNOS,
              label=u'GerenciarAlunos', name=u'caixaAlunos', parent=self.panel1,
              pos=wx.Point(278, 202), size=wx.Size(768, 201), style=0)

        self.caixaDisciplinas = wx.StaticBox(id=wxID_FRAME1CAIXADISCIPLINAS,
              label=u'Gerenciar Disciplinas', name=u'caixaDisciplinas',
              parent=self.panel1, pos=wx.Point(275, 440), size=wx.Size(775,
              184), style=0)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.panel1, pos=wx.Point(304, 32),
              size=wx.Size(40, 40), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnProfListBoxListboxDclick(self, event):
        event.Skip()

    def OnProfListBoxListbox(self, event):
        event.Skip()

    def OnBotaoAdicionarButton(self, event):
        event.Skip()
