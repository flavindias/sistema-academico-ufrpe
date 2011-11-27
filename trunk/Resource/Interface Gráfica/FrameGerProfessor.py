#Boa:Frame:FrameAddProfessor

import wx
import wx.lib.buttons
import wx.richtext

def create(parent):
    return FrameAddProfessor(parent)

[wxID_FRAMEADDPROFESSOR, wxID_FRAMEADDPROFESSORBOTAOADD, 
 wxID_FRAMEADDPROFESSORBOTAOBUSCARCEP, wxID_FRAMEADDPROFESSORBOTAOBUSCARCPF, 
 wxID_FRAMEADDPROFESSORBOTAOEDITAR, wxID_FRAMEADDPROFESSORBOTAOEXCLUIR, 
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
] = [wx.NewId() for _init_ctrls in range(40)]

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
              name='staticLine1', parent=self.panel1, pos=wx.Point(367, 136),
              size=wx.Size(575, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.logoAcademic = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo professor_peq.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORLOGOACADEMIC,
              name=u'logoAcademic', parent=self.panel1, pos=wx.Point(443, 12),
              size=wx.Size(424, 112), style=0)
        self.logoAcademic.Center(wx.HORIZONTAL)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.panel1,
              pos=wx.Point(407, 155), size=wx.Size(24, 13), style=0)

        self.nomeDataNasc = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEDATANASC,
              label=u'Data de Nascimento:', name=u'nomeDataNasc',
              parent=self.panel1, pos=wx.Point(778, 155), size=wx.Size(101, 13),
              style=0)

        self.nomeNome = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENOME,
              label=u'Nome:', name=u'nomeNome', parent=self.panel1,
              pos=wx.Point(407, 210), size=wx.Size(32, 13), style=0)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.panel1,
              pos=wx.Point(407, 267), size=wx.Size(24, 13), style=0)

        self.nomeSexo = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMESEXO,
              label=u'Sexo:', name=u'nomeSexo', parent=self.panel1,
              pos=wx.Point(723, 272), size=wx.Size(29, 15), style=0)

        self.nomeRua = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMERUA,
              label=u'Endereco:', name=u'nomeRua', parent=self.panel1,
              pos=wx.Point(407, 323), size=wx.Size(50, 13), style=0)

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.panel1,
              pos=wx.Point(407, 377), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.panel1,
              pos=wx.Point(685, 376), size=wx.Size(38, 13), style=0)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.panel1,
              pos=wx.Point(408, 428), size=wx.Size(42, 13), style=0)

        self.nomeUF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.panel1,
              pos=wx.Point(630, 429), size=wx.Size(18, 13), style=0)

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.panel1, pos=wx.Point(407, 478), size=wx.Size(70, 13),
              style=0)

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.panel1,
              pos=wx.Point(618, 527), size=wx.Size(38, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMETELEFONE,
              label=u'Fixo:', name=u'nomeTelefone', parent=self.panel1,
              pos=wx.Point(407, 528), size=wx.Size(25, 13), style=0)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.panel1,
              pos=wx.Point(406, 580), size=wx.Size(35, 13), style=0)

        self.nomeConfirmesenha = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECONFIRMESENHA,
              label=u'Confirme a senha:', name=u'nomeConfirmesenha',
              parent=self.panel1, pos=wx.Point(622, 584), size=wx.Size(89, 13),
              style=0)

        self.campoCPF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCPF,
              name=u'campoCPF', parent=self.panel1, pos=wx.Point(407, 178),
              size=wx.Size(139, 21), style=0, value=u'')

        self.botaoBuscarCPF = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOBUSCARCPF,
              label=u'Buscar CPF', name=u'botaoBuscarCPF', parent=self.panel1,
              pos=wx.Point(572, 175), size=wx.Size(75, 23), style=0)
        self.botaoBuscarCPF.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCPFButton,
              id=wxID_FRAMEADDPROFESSORBOTAOBUSCARCPF)

        self.campoNascimento = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONASCIMENTO,
              name=u'campoNascimento', parent=self.panel1, pos=wx.Point(778,
              177), size=wx.Size(126, 21), style=0, value=u'')

        self.campoNome = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONOME,
              name=u'campoNome', parent=self.panel1, pos=wx.Point(407, 232),
              size=wx.Size(498, 21), style=0, value=u'')

        self.campoCep = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCEP,
              name=u'campoCep', parent=self.panel1, pos=wx.Point(407, 291),
              size=wx.Size(100, 21), style=0, value=u'')

        self.botaoBuscarCEP = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOBUSCARCEP,
              label=u'Buscar CEP', name=u'botaoBuscarCEP', parent=self.panel1,
              pos=wx.Point(530, 289), size=wx.Size(75, 23), style=0)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEADDPROFESSORBOTAOBUSCARCEP)

        self.botaoMasc = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOMASC,
              label=u'Masculino', name=u'botaoMasc', parent=self.panel1,
              pos=wx.Point(723, 295), size=wx.Size(81, 13), style=0)
        self.botaoMasc.SetValue(True)

        self.botaoFeminino = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOFEMININO,
              label=u'Feminino', name=u'botaoFeminino', parent=self.panel1,
              pos=wx.Point(818, 296), size=wx.Size(81, 13), style=0)
        self.botaoFeminino.SetValue(True)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOENDERECO,
              name=u'campoEndereco', parent=self.panel1, pos=wx.Point(407, 347),
              size=wx.Size(499, 21), style=0, value=u'')

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOBAIRRO,
              name=u'campoBairro', parent=self.panel1, pos=wx.Point(406, 398),
              size=wx.Size(232, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCIDADE,
              name=u'campoCidade', parent=self.panel1, pos=wx.Point(684, 398),
              size=wx.Size(224, 21), style=0, value=u'')

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONUMERO,
              name=u'campoNumero', parent=self.panel1, pos=wx.Point(407, 447),
              size=wx.Size(100, 21), style=0, value=u'')

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOUF,
              name=u'campoUF', parent=self.panel1, pos=wx.Point(653, 447),
              size=wx.Size(32, 21), style=0, value=u'')

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.panel1, pos=wx.Point(407,
              500), size=wx.Size(499, 21), style=0, value=u'')

        self.campoFixo = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOFIXO,
              name=u'campoFixo', parent=self.panel1, pos=wx.Point(407, 550),
              size=wx.Size(163, 21), style=0, value=u'')

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCELULAR,
              name=u'campoCelular', parent=self.panel1, pos=wx.Point(622, 549),
              size=wx.Size(162, 21), style=0, value=u'')

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOSENHA,
              name=u'campoSenha', parent=self.panel1, pos=wx.Point(406, 603),
              size=wx.Size(159, 21), style=wx.TE_PASSWORD, value=u'')

        self.campoConfirmeSenha = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCONFIRMESENHA,
              name=u'campoConfirmeSenha', parent=self.panel1, pos=wx.Point(624,
              604), size=wx.Size(159, 21), style=wx.TE_PASSWORD, value=u'')

        self.botaoADD = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORBOTAOADD,
              label=u'Adicionar', name=u'botaoADD', parent=self.panel1,
              pos=wx.Point(824, 544), size=wx.Size(78, 24), style=0)
        self.botaoADD.Bind(wx.EVT_BUTTON, self.OnBotaoADDButton,
              id=wxID_FRAMEADDPROFESSORBOTAOADD)

        self.botaoEditar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o editar_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORBOTAOEDITAR,
              label=u'Editar      ', name=u'botaoEditar', parent=self.panel1,
              pos=wx.Point(825, 574), size=wx.Size(78, 24), style=0)
        self.botaoEditar.Bind(wx.EVT_BUTTON, self.OnBotaoEditarButton,
              id=wxID_FRAMEADDPROFESSORBOTAOEDITAR)

        self.botaoExcluir = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORBOTAOEXCLUIR,
              label=u'Excluir    ', name=u'botaoExcluir', parent=self.panel1,
              pos=wx.Point(824, 603), size=wx.Size(78, 24), style=0)
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAMEADDPROFESSORBOTAOEXCLUIR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoBuscarCPFButton(self, event):
        event.Skip()

    def OnBotaoBuscarCEPButton(self, event):
        event.Skip()

    def OnBotaoADDButton(self, event):
        event.Skip()

    def OnBotaoEditarButton(self, event):
        event.Skip()

    def OnBotaoExcluirButton(self, event):
        event.Skip()


