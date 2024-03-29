#Boa:Frame:FrameGerTurmaAlunos

import wx
import wx.lib.buttons
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

from newAluno import Aluno
from newDisciplina import Disciplina
from newTurma import Turma
from newProfessor import Professor
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
              name=u'FrameGerTurmaAlunos', parent=prnt, pos=wx.Point(36, 3),
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
        self.botaoSalvarTurma.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarTurmaButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOSALVARTURMA)

        self.botaoExcluirTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMAALUNOSBOTAOEXCLUIRTURMA,
              label=u'   Excluir    ', name=u'botaoExcluirTurma',
              parent=self.panel1, pos=wx.Point(1112, 644), size=wx.Size(76, 30),
              style=0)
        self.botaoExcluirTurma.Bind(wx.EVT_BUTTON,
              self.OnBotaoExcluirTurmaButton,
              id=wxID_FRAMEGERTURMAALUNOSBOTAOEXCLUIRTURMA)

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
        self.choiceTurma.SetStringSelection(u'A')
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
              name=u'erroText', parent=self.panel1, pos=wx.Point(437, 640),
              size=wx.Size(436, 16), style=wx.ALIGN_CENTRE)
        self.erroText.Center(wx.HORIZONTAL)
        self.erroText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.listaAlTurmaId = []
        self.listaAlTurmaNome = []
        self.listaDiscTurma = []
        self.verificador = 0
        self.carregarDisciplinas()
        self.carregarAlunos()

    def OnDiscNaTurmaListboxDclick(self, event):
        event.Skip()

    def OnProfListBoxListbox(self, event):
        event.Skip()

    def OnBotaoAdicionarAlunoButton(self, event):
        if self.verificador == 2:
            turma = Turma()
            try:
                ver = self.listaAlunosTodos.GetSelections()[-1]
            except:
                ver = -1
                self.erroText.SetLabel('Selecione um aluno para Adicionar!')
            if ver != -1:
                turma.add(self.getSerie() + self.getTurma(), self.getTurno())
                turma.addAluno(self.getSerie() + self.getTurma(), self.listaAlunos[self.listaAlunosTodos.GetSelections()[-1]])
                self.carregarAlunosTurma(self.getSerie() + self.getTurma())
                self.carregarAlunosPorSerie()
                self.verificador = 1
                self.erroText.SetLabel('Adicionado com Sucesso!')
        elif self.verificador == 1:
            turma = Turma()
            try:
                ver = self.listaAlunosTodos.GetSelections()[-1]
            except:
                ver = -1
                self.erroText.SetLabel('Selecione um aluno para Adicionar!')
            if ver != -1:
                turma.addAluno(self.getSerie() + self.getTurma(), self.listaAlunos[self.listaAlunosTodos.GetSelections()[-1]])
                self.carregarAlunosTurma(self.getSerie() + self.getTurma())
                self.carregarAlunosPorSerie()
                self.erroText.SetLabel('Adicionado com Sucesso!')
        else:
            self.erroText.SetLabel('Nao pode ser Adicionado!')
        event.Skip()

    def OnChoiceSerie(self, event):
        turma = Turma()
        if self.getSerie() != 'false':
            turmaId = self.getSerie() + self.getTurma()
            if turma.carregar(turmaId) and turma.getTurno() == self.getTurno():
                self.carregarAlunosTurma(turmaId)
                self.carregarDisciplinasTurma(turmaId)
                self.carregarAlunosPorSerie()
                self.verificador = 1
                self.erroText.SetLabel('Turma carregada com Sucesso!')
            elif turma.carregar(turmaId):
                self.carregarAlunosPorSerie()
                self.verificador = 3
                self.zerar()
                self.erroText.SetLabel('Turma ja existe em outro turno!')
            else:
                self.carregarAlunosPorSerie()
                self.verificador = 2
                self.zerar()
                self.erroText.SetLabel('Turma ainda nao existe!')
        else:
            self.verificador = 3
            self.zerar()
            self.erroText.SetLabel('Opcao de serie Invalida!!')
                
        event.Skip()

    def OnChoiceTurnoChoice(self, event):
        turma = Turma()
        if self.getSerie() != 'false':
            turmaId = self.getSerie() + self.getTurma()
            if turma.carregar(turmaId) and turma.getTurno() == self.getTurno():
                self.carregarAlunosTurma(turmaId)
                self.carregarDisciplinasTurma(turmaId)
                self.carregarAlunosPorSerie()
                self.verificador = 1
                self.erroText.SetLabel('Turma carregada com Sucesso!')
            elif turma.carregar(turmaId):
                self.carregarAlunosPorSerie()
                self.verificador = 3
                self.zerar()
                self.erroText.SetLabel('Turma ja existe em outro turno!')
            else:
                self.carregarAlunosPorSerie()
                self.verificador = 2
                self.zerar()
                self.erroText.SetLabel('Turma ainda nao existe!')
        else:
            self.verificador = 3
            self.zerar()
            self.erroText.SetLabel('Opcao de serie Invalida!!')
            
        event.Skip()

    def OnAlunosNaTurmaListboxDclick(self, event):
        event.Skip()

    def OnBotaoRemoverAlunoButton(self, event):
        turma = Turma()
        try:
            ver = self.listaAlunosSelecionados.GetSelections()[-1]
        except:
            ver = -1
        if self.listaAlTurmaId != [] and ver != -1:
            if turma.deleteAluno(self.listaAlTurmaId[self.listaAlunosSelecionados.GetSelections()[-1]]):
                self.carregarAlunosTurma(self.getSerie() + self.getTurma())
                self.carregarAlunosPorSerie()
                self.erroText.SetLabel('Aluno deletado com Sucesso!')
            else:
                self.erroText.SetLabel('Erro ao tentar deletar o Aluno!')
        else:
            self.erroText.SetLabel('Selecione uma aluno para Excluir!')
        event.Skip()

    def OnChoiceTurmaChoice(self, event):
        turma = Turma()
        if self.getSerie() != 'false':
            turmaId = self.getSerie() + self.getTurma()
            if turma.carregar(turmaId) and turma.getTurno() == self.getTurno():
                self.carregarAlunosTurma(turmaId)
                self.carregarDisciplinasTurma(turmaId)
                self.carregarAlunosPorSerie()
                self.verificador = 1
                self.erroText.SetLabel('Turma carregada com Sucesso!')
            elif turma.carregar(turmaId):
                self.carregarAlunosPorSerie()
                self.verificador = 3
                self.zerar()
                self.erroText.SetLabel('Turma ja existe em outro turno!')
            else:
                self.carregarAlunosPorSerie()
                self.verificador = 2
                self.zerar()
                self.erroText.SetLabel('Turma ainda nao existe!')
        else:
            self.verificador = 3
            self.zerar()
            self.erroText.SetLabel('Opcao de serie Invalida!!')
                
        event.Skip()

    def OnAlunosMatriculadosListboxDclick(self, event):
        event.Skip()

    def OnDiscCadastradasListboxDclick(self, event):
        event.Skip()

    def OnBotaoAddDisciplinaButton(self, event):
        if self.verificador == 2:
            turma = Turma()
            try:
                ver = self.listaDisciplinasTodas.GetSelections()[-1]
            except:
                ver = -1
                self.erroText.SetLabel('Selecione um disciplina para Adicionar!')
            if ver != -1:
                turma.add(self.getSerie() + self.getTurma(), self.getTurno())
                disciplina = self.listDisc[self.listaDisciplinasTodas.GetSelections()[-1]][0]
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), disciplina)
                self.carregarDisciplinasTurma(self.getSerie() + self.getTurma())
                self.carregarDisciplinas()
                self.verificador = 1
                self.erroText.SetLabel('Adicionado com Sucesso!')
        elif self.verificador == 1:
            turma = Turma()
            try:
                ver = self.listaDisciplinasTodas.GetSelections()[-1]
                disciplina = self.listDisc[self.listaDisciplinasTodas.GetSelections()[-1]][0]
            except:
                ver = -1
                
            if ver == -1:
                self.erroText.SetLabel('Selecione uma disciplina para Adicionar!')
            elif disciplina in self.listaDiscTurma:
                self.erroText.SetLabel('Disciplina ja esta na Turma!')
            else:
                if len(self.listaDiscTurma) == 0:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), disciplina)
                elif len(self.listaDiscTurma) == 1:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0], disciplina)
                elif len(self.listaDiscTurma) == 2:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                     self.listaDiscTurma[1], disciplina)
                elif len(self.listaDiscTurma) == 3:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                     self.listaDiscTurma[1], self.listaDiscTurma[2], disciplina)
                elif len(self.listaDiscTurma) == 4:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                     self.listaDiscTurma[1], self.listaDiscTurma[2], self.listaDiscTurma[3], disciplina)
                elif len(self.listaDiscTurma) == 5:
                    turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                     self.listaDiscTurma[1], self.listaDiscTurma[2], self.listaDiscTurma[3],
                                     self.listaDiscTurma[4], disciplina)
                elif len(self.listaDiscTurma) == 6:
                    self.erroText.SetLabel('Turma ja tem 6 Disciplinas')
                if len(self.listaDiscTurma) != 6:
                    self.carregarDisciplinasTurma(self.getSerie() + self.getTurma())
                    self.erroText.SetLabel('Adicionado com Sucesso!')
        else:
            self.erroText.SetLabel('Nao pode ser Adicionado!')
        event.Skip()

    def OnBotaoDelDisciplinaButton(self, event):
        turma = Turma()
        try:
            ver = self.listaDisciplinasSelecionadas.GetSelections()[-1]
        except:
            ver = -1
        if self.listaDiscTurma != [] and ver != -1:
            del self.listaDiscTurma[self.listaDisciplinasSelecionadas.GetSelections()[-1]]
            if len(self.listaDiscTurma) == 0:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno())
            elif len(self.listaDiscTurma) == 1:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0])
            elif len(self.listaDiscTurma) == 2:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                 self.listaDiscTurma[1])
            elif len(self.listaDiscTurma) == 3:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                 self.listaDiscTurma[1], self.listaDiscTurma[2])
            elif len(self.listaDiscTurma) == 4:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                 self.listaDiscTurma[1], self.listaDiscTurma[2], self.listaDiscTurma[3])
            elif len(self.listaDiscTurma) == 5:
                turma.salvarEdit(self.getSerie() + self.getTurma(), self.getTurno(), self.listaDiscTurma[0],
                                 self.listaDiscTurma[1], self.listaDiscTurma[2], self.listaDiscTurma[3],
                                 self.listaDiscTurma[4])
            self.erroText.SetLabel('Excluido com Sucesso!')
            self.carregarDisciplinasTurma(self.getSerie() + self.getTurma())
        else:
            self.erroText.SetLabel('Selecione uma disciplina!')
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        self.Close(True)
        ponte.mainFrameGerTurmaApp()
        exit()
        event.Skip()

    def carregarDisciplinas(self):
        disc = Disciplina()
        prof = Professor()
        self.listDisc = disc.listaDb()
        self.listDiscBox = []
        for i in self.listDisc:
            prof.carregar(i[1])
            self.listDiscBox += [str(i[0]) + ' - ' + str(prof.getNome())]
        self.listaDisciplinasTodas.Set(self.listDiscBox)

    def carregarAlunos(self):
        aluno = Aluno()
        self.carregarAlunoComTurma()
        lista = aluno.listaDb()
        self.listaAlunos = []
        self.listaAlunosBox = []
        for i in lista:
            if i[0] in self.alunosComTurma:continue
            else:
                self.listaAlunosBox += [i[1]]
                self.listaAlunos +=[i[0]]
        self.listaAlunosTodos.Set(self.listaAlunosBox)

    def salvarAlunosTurma(self, alunoId):
        aluno = Aluno()
        if aluno.carregar(alunoId):
            self.listaAlTurmaId += [alunoId]
            self.listaAlTurmaNome += [aluno.getNome()]
        self.listaAlunosSelecionados.Set(self.listaAlTurmaNome)

    def salvarDisciplinasTurma(self, DiscId):
        self.listaDiscTurma += [DiscId]
        self.listaDisciplinasSelecionadas.Set(self.listaDiscTurma)

    def excluirAlunosTurma(self, alunoId):
        aluno = Aluno()
        aluno.carregar(alunoId)
        self.listaAlTurmaId.remove(alunoId)
        self.listaAlTurmaNome.remove(aluno.getNome())

    def excluirDisciplinasTurma(self, DiscId):
        self.listaDiscTurma.remove(DiscId)

    def carregarAlunosTurma(self, turmaId):
        turma = Turma()
        aluno = Aluno()
        self.listaAlTurmaNome = []
        turma.carregarAluno(turmaId)
        self.listaAlTurmaId = turma.getAlunos()
        for i in self.listaAlTurmaId:
            if aluno.carregar(i):
                self.listaAlTurmaNome += [aluno.getNome()]
        self.listaAlunosSelecionados.Set(self.listaAlTurmaNome)

    def carregarDisciplinasTurma(self, turmaId):
        turma = Turma()
        disc = Disciplina()
        self.listaDiscTurma = []
        turma.carregar(turmaId)
        if turma.getDisciplina1() != None and disc.carregar(turma.getDisciplina1()):
            self.listaDiscTurma += [turma.getDisciplina1()]
        if turma.getDisciplina2() != None and disc.carregar(turma.getDisciplina2()):
            self.listaDiscTurma += [turma.getDisciplina2()]
        if turma.getDisciplina3() != None and disc.carregar(turma.getDisciplina3()):
            self.listaDiscTurma += [turma.getDisciplina3()]
        if turma.getDisciplina4() != None and disc.carregar(turma.getDisciplina4()):
            self.listaDiscTurma += [turma.getDisciplina4()]
        if turma.getDisciplina5() != None and disc.carregar(turma.getDisciplina5()):
            self.listaDiscTurma += [turma.getDisciplina5()]
        if turma.getDisciplina6() != None and disc.carregar(turma.getDisciplina6()):
            self.listaDiscTurma += [turma.getDisciplina6()]

        self.listaDisciplinasSelecionadas.Set(self.listaDiscTurma)

    def carregarAlunoComTurma(self):
        turma = Turma()
        listaTurma = turma.listaDb()
        self.alunosComTurma = []
        for i in listaTurma:
            turma.carregarAluno(i[0])
            self.alunosComTurma += turma.getAlunos()

    def carregarAlunosPorSerie(self):
        aluno = Aluno()
        self.carregarAlunoComTurma()
        lista = aluno.listaDb()
        self.listaAlunos = []
        self.listaAlunosBox = []
        for i in lista:
            aluno.carregar(i[0])
            if i[0] in self.alunosComTurma:continue
            elif aluno.getTurno() == self.getTurno() and aluno.getSerie() == self.getSerie():
                self.listaAlunosBox += [i[1]]
                self.listaAlunos +=[i[0]]
        self.listaAlunosTodos.Set(self.listaAlunosBox)

    def getTurno(self):
        if self.choiceTurno.GetSelection() == 0:
            return 'M'
        elif self.choiceTurno.GetSelection() == 1:
            return 'T'
        elif self.choiceTurno.GetSelection() == 2:
            return 'N'

    def getSerie(self):
        if self.choiceSerie.GetSelection() in [0,1,7,12]:
            return 'false'
        else:
            if self.choiceSerie.GetSelection() == 2:
                return 'F1'
            elif self.choiceSerie.GetSelection() == 3:
                return 'F2'
            elif self.choiceSerie.GetSelection() == 4:
                return 'F3'
            elif self.choiceSerie.GetSelection() == 5:
                return 'F4'
            elif self.choiceSerie.GetSelection() == 6:
                return 'F5'
            elif self.choiceSerie.GetSelection() == 8:
                return 'F6'
            elif self.choiceSerie.GetSelection() == 9:
                return 'F7'
            elif self.choiceSerie.GetSelection() == 10:
                return 'F8'
            elif self.choiceSerie.GetSelection() == 11:
                return 'F9'
            elif self.choiceSerie.GetSelection() == 13:
                return 'M1'
            elif self.choiceSerie.GetSelection() == 14:
                return 'M2'
            elif self.choiceSerie.GetSelection() == 15:
                return 'M3'

    def getTurma(self):
        if self.choiceTurma.GetSelection() == 0:
            return 'A'
        elif self.choiceTurma.GetSelection() == 1:
            return 'B'
        elif self.choiceTurma.GetSelection() == 2:
            return 'C'
        elif self.choiceTurma.GetSelection() == 1:
            return 'D'
        elif self.choiceTurma.GetSelection() == 2:
            return 'E'

    def zerar(self):
        self.listaDisciplinasSelecionadas.Set([])
        self.listaAlunosSelecionados.Set([])

    def OnBotaoSalvarTurmaButton(self, event):
        event.Skip()

    def OnBotaoExcluirTurmaButton(self, event):
        turma = Turma()
        if self.verificador == 1:
            turmaId = self.getSerie() + self.getTurma()
            if turma.delete(turmaId):
                self.listaAlunosSelecionados.Set([])
                self.listaDisciplinasSelecionadas.Set([])
                self.erroText.SetLabel('Turma excluida com Sucesso!')
            else:
                self.erroText.SetLabel('Erro ao tentar excluir a Turma!')
        else:
            self.erroText.SetLabel('Escolha uma turma valida para excluir!')
        event.Skip()
