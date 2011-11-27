#Boa:Frame:FrameAddProfessor

import wx
import wx.richtext

def create(parent):
    return FrameAddProfessor(parent)

[wxID_FRAMEADDPROFESSOR, wxID_FRAMEADDPROFESSORBOTAOBUSCAR, 
 wxID_FRAMEADDPROFESSORBOTAOBUSCARCPF, wxID_FRAMEADDPROFESSORBOTAOCADASTRAR, 
 wxID_FRAMEADDPROFESSORBOTAOFEMININO, wxID_FRAMEADDPROFESSORBOTAOMASC, 
 wxID_FRAMEADDPROFESSORCAMPOBAIRRO, wxID_FRAMEADDPROFESSORCAMPOCELULAR, 
 wxID_FRAMEADDPROFESSORCAMPOCEP, wxID_FRAMEADDPROFESSORCAMPOCIDADE, 
 wxID_FRAMEADDPROFESSORCAMPOCOMPLEMENTO, 
 wxID_FRAMEADDPROFESSORCAMPOCONFIRMESENHA, wxID_FRAMEADDPROFESSORCAMPOCPF, 
 wxID_FRAMEADDPROFESSORCAMPOENDERECO, wxID_FRAMEADDPROFESSORCAMPOFIXO, 
 wxID_FRAMEADDPROFESSORCAMPONASCIMENTO, wxID_FRAMEADDPROFESSORCAMPONOME, 
 wxID_FRAMEADDPROFESSORCAMPONUMERO, wxID_FRAMEADDPROFESSORCAMPOSENHA, 
 wxID_FRAMEADDPROFESSORCAMPOUF, wxID_FRAMEADDPROFESSORLOGOACADEMIC, 
 wxID_FRAMEADDPROFESSORNOMEBAIRRO, wxID_FRAMEADDPROFESSORNOMECELULAR, 
 wxID_FRAMEADDPROFESSORNOMECEP, wxID_FRAMEADDPROFESSORNOMECIDADE, 
 wxID_FRAMEADDPROFESSORNOMECOMPLEMENTO, 
 wxID_FRAMEADDPROFESSORNOMECONFIRMESENHA, wxID_FRAMEADDPROFESSORNOMECPF, 
 wxID_FRAMEADDPROFESSORNOMEDATANASC, wxID_FRAMEADDPROFESSORNOMENOME, 
 wxID_FRAMEADDPROFESSORNOMENUMERO, wxID_FRAMEADDPROFESSORNOMERUA, 
 wxID_FRAMEADDPROFESSORNOMESENHA, wxID_FRAMEADDPROFESSORNOMESEXO, 
 wxID_FRAMEADDPROFESSORNOMETELEFONE, wxID_FRAMEADDPROFESSORNOMEUF, 
 wxID_FRAMEADDPROFESSORPANEL1, wxID_FRAMEADDPROFESSORSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(38)]

class FrameAddProfessor(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEADDPROFESSOR,
              name=u'FrameAddProfessor', parent=prnt, pos=wx.Point(559, 219),
              size=wx.Size(1322, 722), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Adicionar Professor - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAMEADDPROFESSORPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1310, 688),
              style=wx.TAB_TRAVERSAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEADDPROFESSORSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(367, 145),
              size=wx.Size(575, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.logoAcademic = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pequeno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORLOGOACADEMIC,
              name=u'logoAcademic', parent=self.panel1, pos=wx.Point(518, 23),
              size=wx.Size(274, 112), style=0)
        self.logoAcademic.Center(wx.HORIZONTAL)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.panel1,
              pos=wx.Point(407, 164), size=wx.Size(24, 13), style=0)

        self.nomeDataNasc = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEDATANASC,
              label=u'Data de Nascimento:', name=u'nomeDataNasc',
              parent=self.panel1, pos=wx.Point(778, 164), size=wx.Size(101, 13),
              style=0)

        self.nomeNome = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENOME,
              label=u'Nome:', name=u'nomeNome', parent=self.panel1,
              pos=wx.Point(407, 219), size=wx.Size(32, 13), style=0)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.panel1,
              pos=wx.Point(407, 276), size=wx.Size(24, 13), style=0)

        self.nomeSexo = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMESEXO,
              label=u'Sexo:', name=u'nomeSexo', parent=self.panel1,
              pos=wx.Point(723, 281), size=wx.Size(29, 15), style=0)

        self.nomeRua = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMERUA,
              label=u'Endereco:', name=u'nomeRua', parent=self.panel1,
              pos=wx.Point(407, 332), size=wx.Size(50, 13), style=0)

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.panel1,
              pos=wx.Point(407, 386), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.panel1,
              pos=wx.Point(685, 385), size=wx.Size(38, 13), style=0)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.panel1,
              pos=wx.Point(408, 444), size=wx.Size(42, 13), style=0)

        self.nomeUF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.panel1,
              pos=wx.Point(630, 445), size=wx.Size(18, 13), style=0)

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.panel1, pos=wx.Point(407, 503), size=wx.Size(70, 13),
              style=0)

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.panel1,
              pos=wx.Point(618, 566), size=wx.Size(38, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMETELEFONE,
              label=u'Fixo:', name=u'nomeTelefone', parent=self.panel1,
              pos=wx.Point(407, 567), size=wx.Size(25, 13), style=0)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.panel1,
              pos=wx.Point(409, 623), size=wx.Size(35, 13), style=0)

        self.nomeConfirmesenha = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECONFIRMESENHA,
              label=u'Confirme a senha:', name=u'nomeConfirmesenha',
              parent=self.panel1, pos=wx.Point(625, 627), size=wx.Size(89, 13),
              style=0)

        self.campoCPF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCPF,
              name=u'campoCPF', parent=self.panel1, pos=wx.Point(407, 187),
              size=wx.Size(139, 21), style=0, value=u'')

        self.botaoBuscarCPF = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOBUSCARCPF,
              label=u'Buscar CPF', name=u'botaoBuscarCPF', parent=self.panel1,
              pos=wx.Point(572, 184), size=wx.Size(75, 23), style=0)

        self.campoNascimento = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONASCIMENTO,
              name=u'campoNascimento', parent=self.panel1, pos=wx.Point(778,
              186), size=wx.Size(126, 21), style=0, value=u'')

        self.campoNome = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONOME,
              name=u'campoNome', parent=self.panel1, pos=wx.Point(407, 241),
              size=wx.Size(498, 21), style=0, value=u'')

        self.campoCep = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCEP,
              name=u'campoCep', parent=self.panel1, pos=wx.Point(407, 300),
              size=wx.Size(100, 21), style=0, value=u'')

        self.botaoBuscar = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOBUSCAR,
              label=u'Buscar CEP', name=u'botaoBuscar', parent=self.panel1,
              pos=wx.Point(530, 298), size=wx.Size(75, 23), style=0)

        self.botaoMasc = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOMASC,
              label=u'Masculino', name=u'botaoMasc', parent=self.panel1,
              pos=wx.Point(723, 304), size=wx.Size(81, 13), style=0)
        self.botaoMasc.SetValue(True)

        self.botaoFeminino = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOFEMININO,
              label=u'Feminino', name=u'botaoFeminino', parent=self.panel1,
              pos=wx.Point(818, 305), size=wx.Size(81, 13), style=0)
        self.botaoFeminino.SetValue(True)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOENDERECO,
              name=u'campoEndereco', parent=self.panel1, pos=wx.Point(407, 356),
              size=wx.Size(499, 21), style=0, value=u'')

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOBAIRRO,
              name=u'campoBairro', parent=self.panel1, pos=wx.Point(406, 412),
              size=wx.Size(232, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCIDADE,
              name=u'campoCidade', parent=self.panel1, pos=wx.Point(684, 412),
              size=wx.Size(224, 21), style=0, value=u'')

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONUMERO,
              name=u'campoNumero', parent=self.panel1, pos=wx.Point(407, 468),
              size=wx.Size(100, 21), style=0, value=u'')

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOUF,
              name=u'campoUF', parent=self.panel1, pos=wx.Point(653, 468),
              size=wx.Size(32, 21), style=0, value=u'')

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.panel1, pos=wx.Point(407,
              534), size=wx.Size(499, 21), style=0, value=u'')

        self.campoFixo = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOFIXO,
              name=u'campoFixo', parent=self.panel1, pos=wx.Point(407, 591),
              size=wx.Size(163, 21), style=0, value=u'')

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCELULAR,
              name=u'campoCelular', parent=self.panel1, pos=wx.Point(622, 590),
              size=wx.Size(180, 21), style=0, value=u'')

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOSENHA,
              name=u'campoSenha', parent=self.panel1, pos=wx.Point(409, 646),
              size=wx.Size(159, 21), style=wx.TE_PASSWORD, value=u'')

        self.botaoCadastrar = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOCADASTRAR,
              label=u'CADASTRAR', name=u'botaoCadastrar', parent=self.panel1,
              pos=wx.Point(833, 645), size=wx.Size(75, 23), style=0)

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.panel1, pos=wx.Point(627,
              647), size=wx.Size(159, 21), style=wx.TE_PASSWORD, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
