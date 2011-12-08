#Boa:Frame:FrameGerAlunos

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
from Endereco import Endereco
from newLogin import Login
sys.path[0] = original

def create(parent):
    return FrameGerAlunos(parent)

[wxID_FRAMEGERALUNOS, wxID_FRAMEGERALUNOSBOTAOBUSCARCEP, 
 wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO, wxID_FRAMEGERALUNOSBOTAOEXCLUIR, 
 wxID_FRAMEGERALUNOSBOTAOSALVAR, wxID_FRAMEGERALUNOSBOTAOVOLTAR, 
 wxID_FRAMEGERALUNOSBOXALUNOSMATRICULADOSNATURMA, 
 wxID_FRAMEGERALUNOSCAIXATURNO, wxID_FRAMEGERALUNOSCAMPOBAIRRO, 
 wxID_FRAMEGERALUNOSCAMPOCELULAR, wxID_FRAMEGERALUNOSCAMPOCEP, 
 wxID_FRAMEGERALUNOSCAMPOCIDADE, wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO, 
 wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA, wxID_FRAMEGERALUNOSCAMPOCPFA, 
 wxID_FRAMEGERALUNOSCAMPOENDERECO, wxID_FRAMEGERALUNOSCAMPONASCIMENTOA, 
 wxID_FRAMEGERALUNOSCAMPONOMEA, wxID_FRAMEGERALUNOSCAMPONUMERO, 
 wxID_FRAMEGERALUNOSCAMPOSENHA, wxID_FRAMEGERALUNOSCAMPOTELEFONE, 
 wxID_FRAMEGERALUNOSCAMPOUF, wxID_FRAMEGERALUNOSLISTAALUNOS, 
 wxID_FRAMEGERALUNOSLOGOGERALUNOS, wxID_FRAMEGERALUNOSNOMEALUNO, 
 wxID_FRAMEGERALUNOSNOMEBAIRRO, wxID_FRAMEGERALUNOSNOMECELULAR, 
 wxID_FRAMEGERALUNOSNOMECEP, wxID_FRAMEGERALUNOSNOMECIDADE, 
 wxID_FRAMEGERALUNOSNOMECOMPLEMENTO, wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA, 
 wxID_FRAMEGERALUNOSNOMECPFALUNO, wxID_FRAMEGERALUNOSNOMEENDERECO, 
 wxID_FRAMEGERALUNOSNOMEERRO, wxID_FRAMEGERALUNOSNOMENASCIMENTO, 
 wxID_FRAMEGERALUNOSNOMENUMERO, wxID_FRAMEGERALUNOSNOMESERIE, 
 wxID_FRAMEGERALUNOSNOMESEXOALUNO, wxID_FRAMEGERALUNOSNOMETELEFONE, 
 wxID_FRAMEGERALUNOSNOMETURNO, wxID_FRAMEGERALUNOSNOMEUF, 
 wxID_FRAMEGERALUNOSNOTEBOOK1, wxID_FRAMEGERALUNOSPANEL1, 
 wxID_FRAMEGERALUNOSSELECIONARSERIE, wxID_FRAMEGERALUNOSSENHAALUNO, 
 wxID_FRAMEGERALUNOSSEXOFALUNO, wxID_FRAMEGERALUNOSSEXOMALUNO, 
 wxID_FRAMEGERALUNOSSTATICLINE1, wxID_FRAMEGERALUNOSWINDOW1, 
] = [wx.NewId() for _init_ctrls in range(49)]

class FrameGerAlunos(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.window1, select=True,
              text=u'Dados do Aluno')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERALUNOS, name=u'FrameGerAlunos',
              parent=prnt, pos=wx.Point(4, 32), size=wx.Size(1362, 706),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Gerenciar Alunos')
        self.SetClientSize(wx.Size(1354, 672))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGERALUNOSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1354, 672),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Center(wx.BOTH)

        self.notebook1 = wx.Notebook(id=wxID_FRAMEGERALUNOSNOTEBOOK1,
              name='notebook1', parent=self.panel1, pos=wx.Point(16, 136),
              size=wx.Size(1328, 480), style=0)

        self.window1 = wx.Window(id=wxID_FRAMEGERALUNOSWINDOW1, name='window1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1320,
              454), style=wx.TAB_TRAVERSAL)

        self.nomebairro = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEBAIRRO,
              label='Bairro:', name='nomebairro', parent=self.window1,
              pos=wx.Point(325, 259), size=wx.Size(33, 13), style=0)

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEENDERECO,
              label=u'Endereco:', name=u'nomeEndereco', parent=self.window1,
              pos=wx.Point(322, 207), size=wx.Size(50, 13), style=0)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.window1,
              pos=wx.Point(507, 159), size=wx.Size(24, 13), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETURNO,
              label=u'Turno:', name=u'nomeTurno', parent=self.window1,
              pos=wx.Point(321, 156), size=wx.Size(33, 13), style=0)

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.window1, pos=wx.Point(559, 402), size=wx.Size(85, 13),
              style=0)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.window1,
              pos=wx.Point(323, 305), size=wx.Size(42, 13), style=0)

        self.nomeSexoAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESEXOALUNO,
              label=u'Sexo:', name=u'nomeSexoAluno', parent=self.window1,
              pos=wx.Point(320, 102), size=wx.Size(29, 13), style=0)

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.window1, pos=wx.Point(493, 308), size=wx.Size(70, 13),
              style=0)

        self.nomeAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEALUNO,
              label=u'Nome:', name=u'nomeAluno', parent=self.window1,
              pos=wx.Point(319, 7), size=wx.Size(32, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.window1,
              pos=wx.Point(322, 355), size=wx.Size(47, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.window1,
              pos=wx.Point(569, 105), size=wx.Size(29, 13), style=0)

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.window1,
              pos=wx.Point(572, 357), size=wx.Size(38, 13), style=0)

        self.nomeNascimento = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMENASCIMENTO,
              label=u'Data de Nascimento:', name=u'nomeNascimento',
              parent=self.window1, pos=wx.Point(567, 60), size=wx.Size(101, 13),
              style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.window1,
              pos=wx.Point(497, 261), size=wx.Size(38, 13), style=0)

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

        self.botaoSalvar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOSALVAR,
              label=u'       Salvar      ', name=u'botaoSalvar',
              parent=self.panel1, pos=wx.Point(1236, 630), size=wx.Size(104,
              34), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMEGERALUNOSBOTAOSALVAR)

        self.nomeCPFAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMECPFALUNO,
              label=u'CPF:', name=u'nomeCPFAluno', parent=self.window1,
              pos=wx.Point(318, 54), size=wx.Size(24, 13), style=0)

        self.nomeUF = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEUF, label=u'UF:',
              name=u'nomeUF', parent=self.window1, pos=wx.Point(679, 259),
              size=wx.Size(18, 13), style=0)

        self.senhaAluno = wx.StaticText(id=wxID_FRAMEGERALUNOSSENHAALUNO,
              label=u'Senha:', name=u'senhaAluno', parent=self.window1,
              pos=wx.Point(323, 402), size=wx.Size(35, 13), style=0)

        self.campoNomeA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONOMEA,
              name=u'campoNomeA', parent=self.window1, pos=wx.Point(323, 24),
              size=wx.Size(396, 21), style=0, value=u'')

        self.campoCPFA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCPFA,
              name=u'campoCPFA', parent=self.window1, pos=wx.Point(323, 73),
              size=wx.Size(167, 21), style=0, value=u'')

        self.botaoExcluir = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERALUNOSBOTAOEXCLUIR,
              label=u'  Excluir   ', name=u'botaoExcluir', parent=self.panel1,
              pos=wx.Point(1110, 632), size=wx.Size(96, 32), style=0)
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnGenBitmapTextButtonExcluir,
              id=wxID_FRAMEGERALUNOSBOTAOEXCLUIR)

        self.botaoBuscarCPFAluno = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO,
              label=u'Buscar', name=u'botaoBuscarCPFAluno', parent=self.window1,
              pos=wx.Point(501, 72), size=wx.Size(56, 23), style=0)
        self.botaoBuscarCPFAluno.Bind(wx.EVT_BUTTON,
              self.OnBotaoBuscarCPFAlunoButton,
              id=wxID_FRAMEGERALUNOSBOTAOBUSCARCPFALUNO)

        self.campoNascimentoA = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONASCIMENTOA,
              name=u'campoNascimentoA', parent=self.window1, pos=wx.Point(575,
              77), size=wx.Size(144, 21), style=0, value=u'')

        self.sexoMAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOMALUNO,
              label=u'Masculino', name=u'sexoMAluno', parent=self.window1,
              pos=wx.Point(323, 124), size=wx.Size(81, 13), style=0)
        self.sexoMAluno.SetValue(True)

        self.sexoFAluno = wx.RadioButton(id=wxID_FRAMEGERALUNOSSEXOFALUNO,
              label=u'Feminino', name=u'sexoFAluno', parent=self.window1,
              pos=wx.Point(425, 124), size=wx.Size(81, 13), style=0)
        self.sexoFAluno.SetValue(True)
        self.sexoFAluno.Bind(wx.EVT_RADIOBUTTON, self.OnSexoFAlunoRadiobutton,
              id=wxID_FRAMEGERALUNOSSEXOFALUNO)

        self.selecionarSerie = wx.Choice(choices=['Selecione a serie',
              'Fundamental I', '          1 Ano', '          2 Ano',
              '          3 Ano', '          4 Ano', '          5 Ano',
              'Fundamental II', '          6 Ano', '          7 Ano',
              '          8 Ano', '          9 Ano', 'Ensino Medio',
              '          1 Ano', '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERALUNOSSELECIONARSERIE, name=u'selecionarSerie',
              parent=self.window1, pos=wx.Point(573, 127), size=wx.Size(145,
              21), style=0)
        self.selecionarSerie.SetStringSelection(u'Selecione a serie')
        self.selecionarSerie.SetLabel(u'Selecione a serie')
        self.selecionarSerie.SetHelpText(u'')

        self.caixaTurno = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERALUNOSCAIXATURNO, name=u'caixaTurno',
              parent=self.window1, pos=wx.Point(323, 176), size=wx.Size(117,
              21), style=0)
        self.caixaTurno.SetStringSelection(u'Manha')
        self.caixaTurno.Bind(wx.EVT_CHOICE, self.OnCaixaTurnoChoice,
              id=wxID_FRAMEGERALUNOSCAIXATURNO)

        self.campoCEP = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCEP,
              name=u'campoCEP', parent=self.window1, pos=wx.Point(508, 178),
              size=wx.Size(124, 21), style=0, value=u'')

        self.botaoBuscarCEP = wx.Button(id=wxID_FRAMEGERALUNOSBOTAOBUSCARCEP,
              label=u'Buscar CEP', name=u'botaoBuscarCEP', parent=self.window1,
              pos=wx.Point(644, 177), size=wx.Size(75, 23), style=0)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEGERALUNOSBOTAOBUSCARCEP)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOENDERECO,
              name=u'campoEndereco', parent=self.window1, pos=wx.Point(327,
              228), size=wx.Size(392, 21), style=0, value=u'')

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOBAIRRO,
              name='campoBairro', parent=self.window1, pos=wx.Point(330, 280),
              size=wx.Size(149, 21), style=0, value='')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCIDADE,
              name=u'campoCidade', parent=self.window1, pos=wx.Point(500, 278),
              size=wx.Size(162, 21), style=0, value=u'')

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOUF,
              name=u'campoUF', parent=self.window1, pos=wx.Point(688, 276),
              size=wx.Size(30, 21), style=0, value=u'')

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPONUMERO,
              name=u'campoNumero', parent=self.window1, pos=wx.Point(331, 322),
              size=wx.Size(94, 21), style=0, value=u'')

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.window1, pos=wx.Point(499,
              330), size=wx.Size(221, 21), style=0, value=u'')

        self.campoTelefone = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.window1, pos=wx.Point(328,
              377), size=wx.Size(141, 21), style=0, value=u'')

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCELULAR,
              name=u'campoCelular', parent=self.window1, pos=wx.Point(584, 377),
              size=wx.Size(139, 21), style=0, value=u'')

        self.boxAlunosMatriculadosNaTurma = wx.StaticBox(id=wxID_FRAMEGERALUNOSBOXALUNOSMATRICULADOSNATURMA,
              label=u'Alunos Matriculados:',
              name=u'boxAlunosMatriculadosNaTurma', parent=self.window1,
              pos=wx.Point(816, 25), size=wx.Size(232, 407), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOSENHA,
              name=u'campoSenha', parent=self.window1, pos=wx.Point(328, 423),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEGERALUNOSCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.window1, pos=wx.Point(563,
              423), size=wx.Size(160, 21), style=wx.TE_PASSWORD, value=u'')

        self.listaAlunos = wx.ListBox(choices=[],
              id=wxID_FRAMEGERALUNOSLISTAALUNOS, name=u'listaAlunos',
              parent=self.window1, pos=wx.Point(832, 48), size=wx.Size(200,
              368), style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listaAlunos.Bind(wx.EVT_LISTBOX_DCLICK, self.OnAlunoListBoxDclick,
              id=wxID_FRAMEGERALUNOSLISTAALUNOS)

        self.nomeErro = wx.StaticText(id=wxID_FRAMEGERALUNOSNOMEERRO, label='',
              name='nomeErro', parent=self.panel1, pos=wx.Point(552, 640),
              size=wx.Size(0, 13), style=0)
        self.nomeErro.SetAutoLayout(True)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.verificador = 0

    def OnBotaoBuscarCEPButton(self, event):
        endereco = Endereco()
        try:
            if endereco.getEnderecoNet(self.campoCep.GetValue()):
                if endereco.getRua() != None and endereco.getBairro() != None:
                    self.campoEndereco.SetValue(endereco.getRua())
                    self.campoBairro.SetValue(endereco.getBairro())
                self.campoCidade.SetValue(endereco.getCidade())
                self.campoUF.SetValue(endereco.getUf())
        except:
            None
        event.Skip()

    def OnCaixaTurnoChoice(self, event):
        if self.getSerie != 'false':
            self.carregarAlunos(self.getSerie(), self.getTurno())
            self.listaAlunos.Set(self.listaNome)
        event.Skip()

    def OnSexoFAlunoRadiobutton(self, event):
        event.Skip()

    def OnGenBitmapTextButtonExcluir(self, event):
        aluno = Aluno()
        try:
            if str(int(self.campoCPFA)) == self.campoCPFA:
                if aluno.delete(self.campoCPFA.GetValue()):
                    None
                    self.zerar()
                else:
                    None
        except:
            None
        event.Skip()

    def OnAlunoListBoxDclick(self, event):
        if self.listaAlunos.GetSelections()[-1] != -1:
            self.campoCPFA.SetValue(self.listaA[self.listaAlunos.GetSelections()[-1]])
            self.carregarDados()
        event.Skip()

    def OnSelecionarTurmaChoice(self, event):
        event.Skip()

    def OnBotaoSalvarButton(self, event):
        aluno = Aluno()
        login = Login()
        try:
            if self.verificador == 0:
                try:
                    if self.sexoMAluno.GetValue():
                        sexo = 1
                    else:
                        sexo = 2
                    num = int(self.campoNumero.GetValue())
                    tel = str(int(self.campoTelefone.GetValue()))
                    cel = str(int(self.campoCelular.GetValue()))
                    aluno.add(str(int(self.campoCPFA.GetValue())), self.campoNomeA.GetValue(), self.invertData(self.campoNascimentoA.GetValue()), sexo, self.campoCEP.GetValue(),
                              self.campoUF.GetValue(), self.campoCidade.GetValue(), self.campoBairro.GetValue(), self.campoEndereco.GetValue(), num, self.campoComplemento.GetValue(),
                              self.getSerie(), self.getTurno(), tel, cel)
                    self.zerar()
                except:
                    None
            else:
                try:
                    if self.sexoMAluno.GetValue():
                        sexo = 1
                    else:
                        sexo = 2
                    num = int(self.campoNumero.GetValue())
                    tel = str(int(self.campoTelefone.GetValue()))
                    cel = str(int(self.campoCelular.GetValue()))
                    aluno.salvarEdit(str(int(self.campoCPFA.GetValue())), self.campoNomeA.GetValue(), self.invertData(self.campoNascimentoA.GetValue()), sexo, self.campoCEP.GetValue(),
                              self.campoUF.GetValue(), self.campoCidade.GetValue(), self.campoBairro.GetValue(), self.campoEndereco.GetValue(), num, self.campoComplemento.GetValue(),
                              self.getSerie(), self.getTurno(), tel, cel)
                    self.zerar()
                except:
                    None
        except:
            None
        event.Skip()

    def OnBotaoBuscarCPFAlunoButton(self, event):
        self.carregarDados()
        event.Skip()

    def carregarDados(self):
        aluno = Aluno()
        try:
            if aluno.carregar(str(int(self.campoCPFA.GetValue()))):
                self.campoCPFA.SetValue(aluno.getCpf())
                self.campoNomeA.SetValue(aluno.getNome())
                self.campoNascimentoA.SetValue(self.invertData(str(aluno.getData())))
                if aluno.getSexo()== 1:
                    self.sexoMAluno.SetValue(True)
                else:
                    self.sexoFAluno.SetValue(True)
                self.campoCEP.SetValue(aluno.getCep())
                self.campoUF.SetValue(aluno.getUf())
                self.campoCidade.SetValue(aluno.getCidade())
                self.campoBairro.SetValue(aluno.getBairro())
                self.campoEndereco.SetValue(aluno.getRua())
                self.campoNumero.SetValue(str(aluno.getNum()))
                self.campoComplemento.SetValue(aluno.getComp())
                self.campoTelefone.SetValue(aluno.getTelefone())
                self.campoCelular.SetValue(aluno.getCelular())
                self.setSerie(aluno.getSerie())
                self.setTurno(aluno.getTurno())
                self.verificador = 1
            else:
                None
        except:
            None

    def invertData(self, data):
        nasc = ''
        for i in range(len(data)-1, -1, -1):
            if nasc == '':
                nasc += data[i]
            else:
                nasc += '-' + data[i]
        return nasc

    def getTurno(self):
        if self.caixaTurno.GetSelection() == 0:
            return 'M'
        elif self.caixaTurno.GetSelection() == 1:
            return 'T'
        elif self.caixaTurno.GetSelection() == 2:
            return 'N'

    def getSerie(self):
        if self.selecionarSerie.GetSelection() in [0,1,7,12]:
            return 'false'
        else:
            if self.selecionarSerie.GetSelection() == 2:
                return 'F1'
            elif self.selecionarSerie.GetSelection() == 3:
                return 'F2'
            elif self.selecionarSerie.GetSelection() == 4:
                return 'F3'
            elif self.selecionarSerie.GetSelection() == 5:
                return 'F4'
            elif self.selecionarSerie.GetSelection() == 6:
                return 'F5'
            elif self.selecionarSerie.GetSelection() == 8:
                return 'F6'
            elif self.selecionarSerie.GetSelection() == 9:
                return 'F7'
            elif self.selecionarSerie.GetSelection() == 10:
                return 'F8'
            elif self.selecionarSerie.GetSelection() == 11:
                return 'F9'
            elif self.selecionarSerie.GetSelection() == 13:
                return 'M1'
            elif self.selecionarSerie.GetSelection() == 14:
                return 'M2'
            elif self.selecionarSerie.GetSelection() == 15:
                return 'M3'

    def setTurno(self, turno):
        if turno == 'M':
            self.caixaTurno.SetStringSelection('Manha')
        elif turno == 'T':
            self.caixaTurno.SetStringSelection('Tarde')
        elif turno == 'N':
            self.caixaTurno.SetStringSelection('Noite')

    def setSerie(self, serie):
        #self.selecionarSerie.SetStringSelection('')
        if serie == 'F1':
            self.selecionarSerie.SetStringSelection('          1 Ano')
        elif serie == 'F2':
            self.selecionarSerie.SetStringSelection('          2 Ano')
        elif serie == 'F3':
            self.selecionarSerie.SetStringSelection('          3 Ano')
        elif serie == 'F4':
            self.selecionarSerie.SetStringSelection('          4 Ano')
        elif serie == 'F5':
            self.selecionarSerie.SetStringSelection('          5 Ano')
        elif serie == 'F6':
            self.selecionarSerie.SetStringSelection('          6 Ano')
        elif serie == 'F7':
            self.selecionarSerie.SetStringSelection('          7 Ano')
        elif serie == 'F8':
            self.selecionarSerie.SetStringSelection('          8 Ano')
        elif serie == 'F9':
            self.selecionarSerie.SetStringSelection('          9 Ano')
        elif serie == 'M1':
            self.selecionarSerie.SetStringSelection('          1 Ano')
        elif serie == 'M2':
            self.selecionarSerie.SetStringSelection('          2 Ano')
        elif serie == 'M3':
            self.selecionarSerie.SetStringSelection('          3 Ano')

    def carregarAlunos(self, serie, turno):
        aluno = Aluno()
        tuplaA = aluno.listaDb()
        self.listaA = []
        self.listaNome = []
        for i in tuplaA:
            if i[13] == serie and i[14] == turno:
                self.listaA += i[0]
                self.listaNome += i[1]

    def zerar(self):
        self.campoCPFA.SetValue('')
        self.campoNomeA.SetValue('')
        self.campoNascimentoA.SetValue('')
        self.campoCEP.SetValue('')
        self.campoUF.SetValue('')
        self.campoCidade.SetValue('')
        self.campoBairro.SetValue('')
        self.campoEndereco.SetValue('')
        self.campoNumero.SetValue('')
        self.campoComplemento.SetValue('')
        self.campoTelefone.SetValue('')
        self.campoCelular.SetValue('')
        self.campoSenha.SetValue('')
        self.campoConfirmeSenha.SetValue('')
        self.verificador = 0
