#Boa:Frame:FrameGerAlunos

import wx
import wx.lib.buttons

def create(parent):
    return FrameGerAlunos(parent)

[wxID_FRAMEGERALUNOS, wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO, 
 wxID_FRAMEGERALUNOSBOTAOEXCLUIR, wxID_FRAMEGERALUNOSBOTAOSALVAR, 
 wxID_FRAMEGERALUNOSBOTAOVOLTAR, 
 wxID_FRAMEGERALUNOSBOXALUNOSMATRICULADOSNATURMA, 
 wxID_FRAMEGERALUNOSCAIXATURNO, wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA, 
 wxID_FRAMEGERALUNOSCAMPOCPFA, wxID_FRAMEGERALUNOSCAMPONASCIMENTOA, 
 wxID_FRAMEGERALUNOSCAMPONOMEA, wxID_FRAMEGERALUNOSCAMPOSENHA, 
 wxID_FRAMEGERALUNOSLOGOGERALUNOS, wxID_FRAMEGERALUNOSNOMEALUNO, 
 wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA, wxID_FRAMEGERALUNOSNOMECPFALUNO, 
 wxID_FRAMEGERALUNOSNOMENASCIMENTO, wxID_FRAMEGERALUNOSNOMESERIE, 
 wxID_FRAMEGERALUNOSNOMESEXOALUNO, wxID_FRAMEGERALUNOSNOMETURMA, 
 wxID_FRAMEGERALUNOSNOMETURNO, wxID_FRAMEGERALUNOSNOTEBOOK1, 
 wxID_FRAMEGERALUNOSPANEL1, wxID_FRAMEGERALUNOSPROFLISTBOX, 
 wxID_FRAMEGERALUNOSSELECIONARTURMA, wxID_FRAMEGERALUNOSSELECIONASERIE, 
 wxID_FRAMEGERALUNOSSENHAALUNO, wxID_FRAMEGERALUNOSSEXOFALUNO, 
 wxID_FRAMEGERALUNOSSEXOMALUNO, wxID_FRAMEGERALUNOSSTATICLINE1, 
 wxID_FRAMEGERALUNOSWINDOW1, 
] = [wx.NewId() for _init_ctrls in range(31)]

class FrameGerAlunos(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.window1, select=True,
              text=u'Dados do Aluno')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERALUNOS, name=u'FrameGerAlunos',
              parent=prnt, pos=wx.Point(535, 225), size=wx.Size(1370, 710),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Gerenciar Alunos')
        self.SetClientSize(wx.Size(1354, 672))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGERALUNOSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1354, 672),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Center(wx.BOTH)

        self.notebook1 = wx.Notebook(id=wxID_FRAMEGERALUNOSNOTEBOOK1,
              name='notebook1', parent=self.panel1, pos=wx.Point(16, 165),
              size=wx.Size(1328, 432), style=0)

        self.window1 = wx.Window(id=wxID_FRAMEGERALUNOSWINDOW1, name='window1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1320,
              406), style=wx.TAB_TRAVERSAL)

        self.nomeTurma = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETURMA,
              label=u'Turma:', name=u'nomeTurma', parent=self.window1,
              pos=wx.Point(552, 243), size=wx.Size(35, 13), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETURNO,
              label=u'Turno:', name=u'nomeTurno', parent=self.window1,
              pos=wx.Point(326, 244), size=wx.Size(33, 13), style=0)

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.window1, pos=wx.Point(559, 305), size=wx.Size(85, 13),
              style=0)

        self.nomeSexoAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESEXOALUNO,
              label=u'Sexo:', name=u'nomeSexoAluno', parent=self.window1,
              pos=wx.Point(321, 181), size=wx.Size(29, 13), style=0)

        self.nomeAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEALUNO,
              label=u'Nome:', name=u'nomeAluno', parent=self.window1,
              pos=wx.Point(319, 44), size=wx.Size(32, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.window1,
              pos=wx.Point(553, 183), size=wx.Size(29, 13), style=0)

        self.nomeNascimento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENASCIMENTO,
              label=u'Data de Nascimento:', name=u'nomeNascimento',
              parent=self.window1, pos=wx.Point(567, 114), size=wx.Size(101,
              13), style=0)

        self.nomeCPFAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECPFALUNO,
              label=u'CPF:', name=u'nomeCPFAluno', parent=self.window1,
              pos=wx.Point(318, 110), size=wx.Size(24, 13), style=0)

        self.senhaAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSSENHAALUNO,
              label=u'Senha:', name=u'senhaAluno', parent=self.window1,
              pos=wx.Point(323, 305), size=wx.Size(35, 13), style=0)

        self.campoNomeA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMEA,
              name=u'campoNomeA', parent=self.window1, pos=wx.Point(323, 63),
              size=wx.Size(396, 21), style=0, value=u'')

        self.campoCPFA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFA,
              name=u'campoCPFA', parent=self.window1, pos=wx.Point(323, 129),
              size=wx.Size(167, 21), style=0, value=u'')

        self.botaoBuscarCPFAluno = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO,
              label=u'Buscar', name=u'botaoBuscarCPFAluno', parent=self.window1,
              pos=wx.Point(501, 128), size=wx.Size(56, 23), style=0)

        self.campoNascimentoA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCIMENTOA,
              name=u'campoNascimentoA', parent=self.window1, pos=wx.Point(575,
              133), size=wx.Size(144, 21), style=0, value=u'')

        self.sexoMAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOMALUNO,
              label=u'Masculino', name=u'sexoMAluno', parent=self.window1,
              pos=wx.Point(334, 203), size=wx.Size(81, 13), style=0)
        self.sexoMAluno.SetValue(True)

        self.sexoFAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOFALUNO,
              label=u'Feminino', name=u'sexoFAluno', parent=self.window1,
              pos=wx.Point(425, 203), size=wx.Size(81, 13), style=0)
        self.sexoFAluno.SetValue(True)
        self.sexoFAluno.Bind(wx.EVT_RADIOBUTTON, self.OnSexoFAlunoRadiobutton,
              id=wxID_FRAMEGERALUNOSSEXOFALUNO)

        self.logoGerAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/LogoAlunos.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSLOGOGERALUNOS,
              name=u'logoGerAlunos', parent=self.panel1, pos=wx.Point(434, 8),
              size=wx.Size(485, 110), style=0)
        self.logoGerAlunos.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERALUNOSSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(277, 128),
              size=wx.Size(799, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.panel1, pos=wx.Point(253, 12),
              size=wx.Size(48, 48), style=wx.BU_AUTODRAW)

        self.botaoSalvar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOSALVAR,
              label=u'       Salvar      ', name=u'botaoSalvar',
              parent=self.panel1, pos=wx.Point(1236, 630), size=wx.Size(104,
              34), style=0)

        self.selecionaSerie = wx.ComboBox(choices=['Fundamental I',
              '          1 Ano', '          2 Ano', '          3 Ano',
              '          4 Ano', '          5 Ano', 'Fundamental II',
              '          6 Ano', '          7 Ano', '          8 Ano',
              '          9 Ano', 'Ensino Medio', '          1 Ano',
              '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERALUNOSSELECIONASERIE, name=u'selecionaSerie',
              parent=self.window1, pos=wx.Point(555, 201), size=wx.Size(164,
              21), style=0, value=u'Selecione a serie')
        self.selecionaSerie.SetLabel(u'Selecione a serie')

        self.caixaTurno = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERALUNOSCAIXATURNO, name=u'caixaTurno',
              parent=self.window1, pos=wx.Point(331, 264), size=wx.Size(143,
              21), style=0)
        self.caixaTurno.SetStringSelection(u'Manha')
        self.caixaTurno.Bind(wx.EVT_CHOICE, self.OnCaixaTurnoChoice,
              id=wxID_FRAMEGERALUNOSCAIXATURNO)

        self.selecionarTurma = wx.Choice(choices=[],
              id=wxID_FRAMEGERALUNOSSELECIONARTURMA, name=u'selecionarTurma',
              parent=self.window1, pos=wx.Point(562, 263), size=wx.Size(157,
              21), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOSENHA,
              name=u'campoSenha', parent=self.window1, pos=wx.Point(328, 326),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.window1, pos=wx.Point(563,
              326), size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.boxAlunosMatriculadosNaTurma = wx.StaticBox(id=wxID_FRAMEGERALUNOSBOXALUNOSMATRICULADOSNATURMA,
              label=u'Alunos Matriculados:',
              name=u'boxAlunosMatriculadosNaTurma', parent=self.window1,
              pos=wx.Point(816, 48), size=wx.Size(232, 312), style=0)

        self.botaoExcluir = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOEXCLUIR,
              label=u'  Excluir   ', name=u'botaoExcluir', parent=self.panel1,
              pos=wx.Point(1110, 632), size=wx.Size(96, 32), style=0)
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnGenBitmapTextButton1Button,
              id=wxID_FRAMEGERALUNOSBOTAOEXCLUIR)

        self.profListBox = wx.ListBox(choices=[],
              id=wxID_FRAMEGERALUNOSPROFLISTBOX, name=u'profListBox',
              parent=self.window1, pos=wx.Point(832, 72), size=wx.Size(200,
              272), style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.profListBox.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick,
              id=wxID_FRAMEGERALUNOSPROFLISTBOX)
        self.profListBox.Bind(wx.EVT_LISTBOX, self.OnProfListBoxListbox,
              id=wxID_FRAMEGERALUNOSPROFLISTBOX)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoBuscarCEPButton(self, event):
        
        event.Skip()

    def OnCaixaTurnoChoice(self, event):
        event.Skip()

    def OnSexoFAlunoRadiobutton(self, event):
        event.Skip()

    def OnGenBitmapTextButton1Button(self, event):
        event.Skip()

    def OnProfListBoxListboxDclick(self, event):
        event.Skip()

    def OnProfListBoxListbox(self, event):
        event.Skip()
