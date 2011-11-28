#Boa:Frame:FrameGerAlunos

import wx
import wx.lib.buttons

def create(parent):
    return FrameGerAlunos(parent)

[wxID_FRAMEGERALUNOS, wxID_FRAMEGERALUNOSBOTAOBUSCARCEP, 
 wxID_FRAMEGERALUNOSBOTAOBUSCARCPF, wxID_FRAMEGERALUNOSBOTAOSALVAR, 
 wxID_FRAMEGERALUNOSBOTAOVOLTAR, wxID_FRAMEGERALUNOSCAMPOCELULAR, 
 wxID_FRAMEGERALUNOSCAMPOCEP, wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO, 
 wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA, wxID_FRAMEGERALUNOSCAMPOCPFA, 
 wxID_FRAMEGERALUNOSCAMPOCPFRESPONSAVEL, wxID_FRAMEGERALUNOSCAMPOENDERECO, 
 wxID_FRAMEGERALUNOSCAMPONASCIMENTOA, wxID_FRAMEGERALUNOSCAMPONASCRESPONSAVEL, 
 wxID_FRAMEGERALUNOSCAMPONOMEA, wxID_FRAMEGERALUNOSCAMPONOMERESPONSAVEL, 
 wxID_FRAMEGERALUNOSCAMPONUMERO, wxID_FRAMEGERALUNOSCAMPOSENHA, 
 wxID_FRAMEGERALUNOSCAMPOTELEFONE, wxID_FRAMEGERALUNOSCPFRESPONSAVEL, 
 wxID_FRAMEGERALUNOSLOGOGERALUNOS, wxID_FRAMEGERALUNOSNOMEALUNO, 
 wxID_FRAMEGERALUNOSNOMECELULAR, wxID_FRAMEGERALUNOSNOMECEP, 
 wxID_FRAMEGERALUNOSNOMECOMPLEMENTO, wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA, 
 wxID_FRAMEGERALUNOSNOMECPFALUNO, wxID_FRAMEGERALUNOSNOMEENDERECO, 
 wxID_FRAMEGERALUNOSNOMENASCIMENTO, wxID_FRAMEGERALUNOSNOMENUMERO, 
 wxID_FRAMEGERALUNOSNOMERESPONSAVEL, wxID_FRAMEGERALUNOSNOMESERIE, 
 wxID_FRAMEGERALUNOSNOMESEXOALUNO, wxID_FRAMEGERALUNOSNOMETELEFONE, 
 wxID_FRAMEGERALUNOSNOTEBOOK1, wxID_FRAMEGERALUNOSPANEL1, 
 wxID_FRAMEGERALUNOSRADIOBUTTON1, wxID_FRAMEGERALUNOSRADIOBUTTON2, 
 wxID_FRAMEGERALUNOSSELECIONASERIE, wxID_FRAMEGERALUNOSSENHAALUNO, 
 wxID_FRAMEGERALUNOSSEXOFALUNO, wxID_FRAMEGERALUNOSSEXOMALUNO, 
 wxID_FRAMEGERALUNOSSTATICLINE1, wxID_FRAMEGERALUNOSSTATICTEXT1, 
 wxID_FRAMEGERALUNOSSTATICTEXT3, wxID_FRAMEGERALUNOSSTATICTEXT5, 
 wxID_FRAMEGERALUNOSSTATICTEXT6, wxID_FRAMEGERALUNOSTEXTCTRL2, 
 wxID_FRAMEGERALUNOSTEXTCTRL3, wxID_FRAMEGERALUNOSWINDOW1, 
 wxID_FRAMEGERALUNOSWINDOW2, 
] = [wx.NewId() for _init_ctrls in range(51)]

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
              parent=prnt, pos=wx.Point(559, 219), size=wx.Size(1322, 722),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Gerenciar Alunos')
        self.SetClientSize(wx.Size(1310, 688))

        self.panel1 = wx.Panel(id=wxID_FRAMEGERALUNOSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1312, 688),
              style=wx.TAB_TRAVERSAL)

        self.notebook1 = wx.Notebook(id=wxID_FRAMEGERALUNOSNOTEBOOK1,
              name='notebook1', parent=self.panel1, pos=wx.Point(16, 165),
              size=wx.Size(1272, 432), style=0)

        self.window2 = wx.Window(id=wxID_FRAMEGERALUNOSWINDOW2, name='window2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              406), style=0)

        self.campoTelefone = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.window2, pos=wx.Point(441,
              320), size=wx.Size(152, 21), style=0, value=u'')

        self.campoNomeResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMERESPONSAVEL,
              name=u'campoNomeResponsavel', parent=self.window2,
              pos=wx.Point(412, 40), size=wx.Size(396, 21), style=0, value=u'')

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.window2,
              pos=wx.Point(701, 241), size=wx.Size(42, 13), style=0)

        self.botaoBuscarCPF = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPF,
              label=u'Buscar', name=u'botaoBuscarCPF', parent=self.window2,
              pos=wx.Point(598, 95), size=wx.Size(56, 23), style=0)

        self.cpfResponsavel = wx.StaticText(id=wxID_FRAMEGERALUNOSCPFRESPONSAVEL,
              label=u'CPF:', name=u'cpfResponsavel', parent=self.window2,
              pos=wx.Point(412, 72), size=wx.Size(24, 13), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.window2, pos=wx.Point(428,
              262), size=wx.Size(240, 21), style=0, value=u'')

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco', parent=self.window2,
              pos=wx.Point(418, 182), size=wx.Size(50, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONUMERO,
              name=u'campoNumero', parent=self.window2, pos=wx.Point(713, 264),
              size=wx.Size(100, 21), style=0, value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.window2, pos=wx.Point(421, 236), size=wx.Size(70, 13),
              style=0)

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCELULAR,
              name=u'campoCelular', parent=self.window2, pos=wx.Point(648, 320),
              size=wx.Size(168, 21), style=0, value=u'')

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOENDERECO,
              name=u'campoEndereco', parent=self.window2, pos=wx.Point(423,
              203), size=wx.Size(392, 21), style=0, value=u'')

        self.campoCPFResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFRESPONSAVEL,
              name=u'campoCPFResponsavel', parent=self.window2,
              pos=wx.Point(417, 96), size=wx.Size(167, 21), style=0, value=u'')

        self.nomeResponsavel = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMERESPONSAVEL,
              label=u'Nome:', name=u'nomeResponsavel', parent=self.window2,
              pos=wx.Point(408, 19), size=wx.Size(32, 13), style=0)

        self.NomeCelular = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECELULAR,
              label=u'Celular:', name=u'NomeCelular', parent=self.window2,
              pos=wx.Point(637, 301), size=wx.Size(38, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAMEGERALUNOSSTATICTEXT6,
              label=u'Confirmar Senha:', name='staticText6',
              parent=self.window2, pos=wx.Point(640, 351), size=wx.Size(85, 13),
              style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.window2,
              pos=wx.Point(425, 299), size=wx.Size(47, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEGERALUNOSSTATICTEXT5,
              label=u'Sexo:', name='staticText5', parent=self.window2,
              pos=wx.Point(414, 131), size=wx.Size(29, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEGERALUNOSSTATICTEXT3,
              label=u'Senha:', name='staticText3', parent=self.window2,
              pos=wx.Point(423, 350), size=wx.Size(35, 13), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEGERALUNOSSTATICTEXT1,
              label=u'Data de Nascimento:', name='staticText1',
              parent=self.window2, pos=wx.Point(678, 76), size=wx.Size(101, 13),
              style=0)

        self.radioButton2 = wx.RadioButton(id=wxID_FRAMEGERALUNOSRADIOBUTTON2,
              label=u'Masculino', name='radioButton2', parent=self.window2,
              pos=wx.Point(427, 153), size=wx.Size(81, 13), style=0)
        self.radioButton2.SetValue(True)

        self.radioButton1 = wx.RadioButton(id=wxID_FRAMEGERALUNOSRADIOBUTTON1,
              label=u'Feminino', name='radioButton1', parent=self.window2,
              pos=wx.Point(518, 153), size=wx.Size(81, 13), style=0)
        self.radioButton1.SetValue(True)

        self.campoCEP = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCEP,
              name=u'campoCEP', parent=self.window2, pos=wx.Point(621, 152),
              size=wx.Size(119, 21), style=0, value=u'')

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.window2,
              pos=wx.Point(603, 129), size=wx.Size(24, 13), style=0)

        self.botaoBuscarCEP = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCEP,
              label=u'Buscar', name=u'botaoBuscarCEP', parent=self.window2,
              pos=wx.Point(756, 151), size=wx.Size(56, 23), style=0)

        self.campoNascResponsavel = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCRESPONSAVEL,
              name=u'campoNascResponsavel', parent=self.window2,
              pos=wx.Point(688, 100), size=wx.Size(120, 21), style=0,
              value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAMEGERALUNOSTEXTCTRL3,
              name='textCtrl3', parent=self.window2, pos=wx.Point(441, 371),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAMEGERALUNOSTEXTCTRL2,
              name='textCtrl2', parent=self.window2, pos=wx.Point(657, 372),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.window1 = wx.Window(id=wxID_FRAMEGERALUNOSWINDOW1, name='window1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              406), style=0)

        self.nomeNascimento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENASCIMENTO,
              label=u'Data de Nascimento:', name=u'nomeNascimento',
              parent=self.window1, pos=wx.Point(642, 97), size=wx.Size(101, 13),
              style=0)

        self.sexoFAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOFALUNO,
              label=u'Feminino', name=u'sexoFAluno', parent=self.window1,
              pos=wx.Point(747, 182), size=wx.Size(81, 13), style=0)
        self.sexoFAluno.SetValue(True)

        self.campoNascimentoA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCIMENTOA,
              name=u'campoNascimentoA', parent=self.window1, pos=wx.Point(664,
              116), size=wx.Size(144, 21), style=0, value=u'')

        self.campoNomeA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMEA,
              name=u'campoNomeA', parent=self.window1, pos=wx.Point(412, 59),
              size=wx.Size(396, 21), style=0, value=u'')

        self.senhaAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSSENHAALUNO,
              label=u'Senha:', name=u'senhaAluno', parent=self.window1,
              pos=wx.Point(414, 214), size=wx.Size(35, 13), style=0)

        self.sexoMAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOMALUNO,
              label=u'Masculino', name=u'sexoMAluno', parent=self.window1,
              pos=wx.Point(656, 182), size=wx.Size(81, 13), style=0)
        self.sexoMAluno.SetValue(True)

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.window1, pos=wx.Point(432,
              292), size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.nomeCPFAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECPFALUNO,
              label=u'CPF:', name=u'nomeCPFAluno', parent=self.window1,
              pos=wx.Point(412, 93), size=wx.Size(24, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOSENHA,
              name=u'campoSenha', parent=self.window1, pos=wx.Point(432, 235),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.selecionaSerie = wx.ComboBox(choices=[],
              id=wxID_FRAMEGERALUNOSSELECIONASERIE, name=u'selecionaSerie',
              parent=self.window1, pos=wx.Point(423, 172), size=wx.Size(130,
              21), style=0, value=u'Selecione a serie')
        self.selecionaSerie.SetLabel(u'Selecione a serie')

        self.nomeSexoAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESEXOALUNO,
              label=u'Sexo:', name=u'nomeSexoAluno', parent=self.window1,
              pos=wx.Point(643, 160), size=wx.Size(29, 13), style=0)

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.window1, pos=wx.Point(416, 271), size=wx.Size(85, 13),
              style=0)

        self.campoCPFA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFA,
              name=u'campoCPFA', parent=self.window1, pos=wx.Point(417, 112),
              size=wx.Size(167, 21), style=0, value=u'')

        self.nomeAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEALUNO,
              label=u'Nome:', name=u'nomeAluno', parent=self.window1,
              pos=wx.Point(408, 40), size=wx.Size(32, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.window1,
              pos=wx.Point(413, 154), size=wx.Size(29, 13), style=0)

        self.logoGerAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/LogoAlunos.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSLOGOGERALUNOS,
              name=u'logoGerAlunos', parent=self.panel1, pos=wx.Point(413, 8),
              size=wx.Size(485, 110), style=0)
        self.logoGerAlunos.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERALUNOSSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(256, 128),
              size=wx.Size(799, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.panel1, pos=wx.Point(253, 12),
              size=wx.Size(48, 48), style=wx.BU_AUTODRAW)

        self.botaoSalvar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/bot\xe3o adicionar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOSALVAR,
              label=u'       Salvar      ', name=u'botaoSalvar',
              parent=self.panel1, pos=wx.Point(1183, 632), size=wx.Size(104,
              30), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
