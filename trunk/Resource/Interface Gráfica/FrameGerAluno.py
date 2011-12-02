#Boa:Frame:FrameGerAlunos

import wx
import wx.lib.buttons

def create(parent):
    return FrameGerAlunos(parent)

[wxID_FRAMEGERALUNOS, wxID_FRAMEGERALUNOSBOTAOBUSCARCEP, 
 wxID_FRAMEGERALUNOSBOTAOBUSCARCPF, wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO, 
 wxID_FRAMEGERALUNOSBOTAOSALVAR, wxID_FRAMEGERALUNOSBOTAOVOLTAR, 
 wxID_FRAMEGERALUNOSCAIXATURNO, wxID_FRAMEGERALUNOSCAMPOCELULAR, 
 wxID_FRAMEGERALUNOSCAMPOCEP, wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO, 
 wxID_FRAMEGERALUNOSCAMPOCONFIRMARSENHARESP, 
 wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA, wxID_FRAMEGERALUNOSCAMPOCPFA, 
 wxID_FRAMEGERALUNOSCAMPOCPFRESPONSAVEL, wxID_FRAMEGERALUNOSCAMPOENDERECO, 
 wxID_FRAMEGERALUNOSCAMPONASCIMENTOA, wxID_FRAMEGERALUNOSCAMPONASCRESPONSAVEL, 
 wxID_FRAMEGERALUNOSCAMPONOMEA, wxID_FRAMEGERALUNOSCAMPONOMERESPONSAVEL, 
 wxID_FRAMEGERALUNOSCAMPONUMERO, wxID_FRAMEGERALUNOSCAMPOSENHA, 
 wxID_FRAMEGERALUNOSCAMPOSENHARESP, wxID_FRAMEGERALUNOSCAMPOTELEFONE, 
 wxID_FRAMEGERALUNOSCPFRESPONSAVEL, wxID_FRAMEGERALUNOSLOGOGERALUNOS, 
 wxID_FRAMEGERALUNOSNOMEALUNO, wxID_FRAMEGERALUNOSNOMECELULAR, 
 wxID_FRAMEGERALUNOSNOMECEP, wxID_FRAMEGERALUNOSNOMECOMPLEMENTO, 
 wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA, 
 wxID_FRAMEGERALUNOSNOMECONFIRMARSENHARESP, wxID_FRAMEGERALUNOSNOMECPFALUNO, 
 wxID_FRAMEGERALUNOSNOMEDATANASCRESP, wxID_FRAMEGERALUNOSNOMEENDERECO, 
 wxID_FRAMEGERALUNOSNOMENASCIMENTO, wxID_FRAMEGERALUNOSNOMENUMERO, 
 wxID_FRAMEGERALUNOSNOMERESPONSAVEL, wxID_FRAMEGERALUNOSNOMESENHARESP, 
 wxID_FRAMEGERALUNOSNOMESERIE, wxID_FRAMEGERALUNOSNOMESEXOALUNO, 
 wxID_FRAMEGERALUNOSNOMESEXORESP, wxID_FRAMEGERALUNOSNOMETELEFONE, 
 wxID_FRAMEGERALUNOSNOMETURNO, wxID_FRAMEGERALUNOSNOTEBOOK1, 
 wxID_FRAMEGERALUNOSPANEL1, wxID_FRAMEGERALUNOSSELECIONASERIE, 
 wxID_FRAMEGERALUNOSSENHAALUNO, wxID_FRAMEGERALUNOSSEXOFALUNO, 
 wxID_FRAMEGERALUNOSSEXOFRESPONSAVEL, wxID_FRAMEGERALUNOSSEXOMALUNO, 
 wxID_FRAMEGERALUNOSSEXOMRESPONSAVEL, wxID_FRAMEGERALUNOSSTATICLINE1, 
 wxID_FRAMEGERALUNOSWINDOW1, wxID_FRAMEGERALUNOSWINDOW2, 
] = [wx.NewId() for _init_ctrls in range(54)]

class FrameGerAlunos(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.window1, select=False,
              text=u'Dados do Aluno')
        parent.AddPage(imageId=-1, page=self.window2, select=True,
              text=u'Dados do Resposavel')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERALUNOS, name=u'FrameGerAlunos',
              parent=prnt, pos=wx.Point(537, 227), size=wx.Size(1366, 706),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Gerenciar Alunos')
        self.SetClientSize(wx.Size(1354, 672))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',
              wx.BITMAP_TYPE_ICO))

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

        self.window2 = wx.Window(id=wxID_FRAMEGERALUNOSWINDOW2, name='window2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1320,
              406), style=wx.TAB_TRAVERSAL)

        self.nomeResponsavel = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMERESPONSAVEL,
              label=u'Nome:', name=u'nomeResponsavel', parent=self.window2,
              pos=wx.Point(408, 19), size=wx.Size(32, 13), style=0)

        self.NomeCelular = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECELULAR,
              label=u'Celular:', name=u'NomeCelular', parent=self.window2,
              pos=wx.Point(637, 301), size=wx.Size(38, 13), style=0)

        self.nomeConfirmarSenhaResp = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECONFIRMARSENHARESP,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenhaResp',
              parent=self.window2, pos=wx.Point(640, 351), size=wx.Size(85, 13),
              style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.window2,
              pos=wx.Point(407, 299), size=wx.Size(47, 13), style=0)

        self.nomeSexoResp = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESEXORESP,
              label=u'Sexo:', name=u'nomeSexoResp', parent=self.window2,
              pos=wx.Point(407, 131), size=wx.Size(29, 13), style=0)

        self.nomeSenhaResp = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESENHARESP,
              label=u'Senha:', name=u'nomeSenhaResp', parent=self.window2,
              pos=wx.Point(406, 350), size=wx.Size(35, 13), style=0)

        self.nomeDataNascResp = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEDATANASCRESP,
              label=u'Data de Nascimento:', name=u'nomeDataNascResp',
              parent=self.window2, pos=wx.Point(678, 76), size=wx.Size(101, 13),
              style=0)

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco', parent=self.window2,
              pos=wx.Point(408, 182), size=wx.Size(50, 13), style=0)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.window2,
              pos=wx.Point(603, 129), size=wx.Size(24, 13), style=0)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.window2,
              pos=wx.Point(701, 241), size=wx.Size(42, 13), style=0)

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.window2, pos=wx.Point(406, 236), size=wx.Size(70, 13),
              style=0)

        self.cpfResponsavel = wx.StaticText(id=wxID_FRAMEGERALUNOSCPFRESPONSAVEL,
              label=u'CPF:', name=u'cpfResponsavel', parent=self.window2,
              pos=wx.Point(407, 72), size=wx.Size(24, 13), style=0)

        self.campoNomeResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMERESPONSAVEL,
              name=u'campoNomeResponsavel', parent=self.window2,
              pos=wx.Point(411, 40), size=wx.Size(396, 21), style=0, value=u'')

        self.campoCPFResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFRESPONSAVEL,
              name=u'campoCPFResponsavel', parent=self.window2,
              pos=wx.Point(411, 96), size=wx.Size(167, 21), style=0, value=u'')

        self.botaoBuscarCPF = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPF,
              label=u'Buscar', name=u'botaoBuscarCPF', parent=self.window2,
              pos=wx.Point(598, 95), size=wx.Size(56, 23), style=0)

        self.campoNascResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCRESPONSAVEL,
              name=u'campoNascResponsavel', parent=self.window2,
              pos=wx.Point(688, 100), size=wx.Size(120, 21), style=0,
              value=u'')

        self.sexoMResponsavel = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOMRESPONSAVEL,
              label=u'Masculino', name=u'sexoMResponsavel', parent=self.window2,
              pos=wx.Point(411, 153), size=wx.Size(81, 13), style=0)
        self.sexoMResponsavel.SetValue(True)

        self.sexoFResponsavel = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOFRESPONSAVEL,
              label=u'Feminino', name=u'sexoFResponsavel', parent=self.window2,
              pos=wx.Point(508, 153), size=wx.Size(81, 13), style=0)
        self.sexoFResponsavel.SetValue(True)

        self.campoCEP = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCEP,
              name=u'campoCEP', parent=self.window2, pos=wx.Point(621, 152),
              size=wx.Size(119, 21), style=0, value=u'')

        self.botaoBuscarCEP = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCEP,
              label=u'Buscar', name=u'botaoBuscarCEP', parent=self.window2,
              pos=wx.Point(756, 151), size=wx.Size(56, 23), style=0)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEGERALUNOSBOTAOBUSCARCEP)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOENDERECO,
              name=u'campoEndereco', parent=self.window2, pos=wx.Point(411,
              203), size=wx.Size(399, 21), style=0, value=u'')

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.window2, pos=wx.Point(410,
              262), size=wx.Size(264, 21), style=0, value=u'')

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONUMERO,
              name=u'campoNumero', parent=self.window2, pos=wx.Point(713, 264),
              size=wx.Size(100, 21), style=0, value=u'')

        self.campoTelefone = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.window2, pos=wx.Point(410,
              320), size=wx.Size(176, 21), style=0, value=u'')

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCELULAR,
              name=u'campoCelular', parent=self.window2, pos=wx.Point(648, 320),
              size=wx.Size(168, 21), style=0, value=u'')

        self.campoSenhaResp = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOSENHARESP,
              name=u'campoSenhaResp', parent=self.window2, pos=wx.Point(410,
              372), size=wx.Size(169, 21), style=wx.TE_PASSWORD, value=u'')

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETURNO,
              label=u'Turno:', name=u'nomeTurno', parent=self.window1,
              pos=wx.Point(659, 156), size=wx.Size(33, 13), style=0)

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.window1, pos=wx.Point(648, 257), size=wx.Size(85, 13),
              style=0)

        self.nomeSexoAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESEXOALUNO,
              label=u'Sexo:', name=u'nomeSexoAluno', parent=self.window1,
              pos=wx.Point(410, 206), size=wx.Size(29, 13), style=0)

        self.nomeAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEALUNO,
              label=u'Nome:', name=u'nomeAluno', parent=self.window1,
              pos=wx.Point(408, 40), size=wx.Size(32, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.window1,
              pos=wx.Point(408, 154), size=wx.Size(29, 13), style=0)

        self.nomeNascimento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENASCIMENTO,
              label=u'Data de Nascimento:', name=u'nomeNascimento',
              parent=self.window1, pos=wx.Point(656, 97), size=wx.Size(101, 13),
              style=0)

        self.nomeCPFAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECPFALUNO,
              label=u'CPF:', name=u'nomeCPFAluno', parent=self.window1,
              pos=wx.Point(407, 93), size=wx.Size(24, 13), style=0)

        self.senhaAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSSENHAALUNO,
              label=u'Senha:', name=u'senhaAluno', parent=self.window1,
              pos=wx.Point(412, 257), size=wx.Size(35, 13), style=0)

        self.campoNomeA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMEA,
              name=u'campoNomeA', parent=self.window1, pos=wx.Point(412, 59),
              size=wx.Size(396, 21), style=0, value=u'')

        self.campoCPFA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFA,
              name=u'campoCPFA', parent=self.window1, pos=wx.Point(412, 112),
              size=wx.Size(167, 21), style=0, value=u'')

        self.botaoBuscarCPFAluno = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO,
              label=u'Buscar', name=u'botaoBuscarCPFAluno', parent=self.window1,
              pos=wx.Point(590, 111), size=wx.Size(56, 23), style=0)

        self.campoNascimentoA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCIMENTOA,
              name=u'campoNascimentoA', parent=self.window1, pos=wx.Point(664,
              116), size=wx.Size(144, 21), style=0, value=u'')

        self.selecionaSerie = wx.ComboBox(choices=['Fundamental I',
              '          1 Ano', '          2 Ano', '          3 Ano',
              '          4 Ano', '          5 Ano', 'Fundamental II',
              '          6 Ano', '          7 Ano', '          8 Ano',
              '          9 Ano', 'Ensino Medio', '          1 Ano',
              '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERALUNOSSELECIONASERIE, name=u'selecionaSerie',
              parent=self.window1, pos=wx.Point(410, 172), size=wx.Size(164,
              21), style=0, value=u'Selecione a serie')
        self.selecionaSerie.SetLabel(u'Selecione a serie')

        self.caixaTurno = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERALUNOSCAIXATURNO, name=u'caixaTurno',
              parent=self.window1, pos=wx.Point(664, 173), size=wx.Size(143,
              21), style=0)
        self.caixaTurno.SetStringSelection(u'Manha')

        self.sexoMAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOMALUNO,
              label=u'Masculino', name=u'sexoMAluno', parent=self.window1,
              pos=wx.Point(423, 228), size=wx.Size(81, 13), style=0)
        self.sexoMAluno.SetValue(True)

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
              30), style=0)

        self.campoConfirmarSenhaResp = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCONFIRMARSENHARESP,
              name=u'campoConfirmarSenhaResp', parent=self.window2,
              pos=wx.Point(648, 372), size=wx.Size(169, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.sexoFAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOFALUNO,
              label=u'Feminino', name=u'sexoFAluno', parent=self.window1,
              pos=wx.Point(514, 228), size=wx.Size(81, 13), style=0)
        self.sexoFAluno.SetValue(True)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOSENHA,
              name=u'campoSenha', parent=self.window1, pos=wx.Point(417, 278),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.window1, pos=wx.Point(652,
              278), size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoBuscarCEPButton(self, event):
        
        event.Skip()
