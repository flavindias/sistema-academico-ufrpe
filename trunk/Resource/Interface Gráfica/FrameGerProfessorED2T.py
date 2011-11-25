#Boa:Frame:FrameAddProfessor

import wx
import wx.richtext

def create(parent):
    return FrameAddProfessor(parent)

[wxID_FRAMEADDPROFESSOR, wxID_FRAMEADDPROFESSORBOTAOBUSCAR, 
 wxID_FRAMEADDPROFESSORBOTAOCARREGAR, wxID_FRAMEADDPROFESSORBOTAOEDITAR, 
 wxID_FRAMEADDPROFESSORBOTAOFEMININO, wxID_FRAMEADDPROFESSORBOTAOMASC, 
 wxID_FRAMEADDPROFESSORCAMPOBAIRRO, wxID_FRAMEADDPROFESSORCAMPOCELULAR, 
 wxID_FRAMEADDPROFESSORCAMPOCEP, wxID_FRAMEADDPROFESSORCAMPOCIDADE, 
 wxID_FRAMEADDPROFESSORCAMPOCOMPLEMENTO, wxID_FRAMEADDPROFESSORCAMPOCPF, 
 wxID_FRAMEADDPROFESSORCAMPOENDERECO, wxID_FRAMEADDPROFESSORCAMPOFIXO, 
 wxID_FRAMEADDPROFESSORCAMPONOME, wxID_FRAMEADDPROFESSORCAMPONOMEP, 
 wxID_FRAMEADDPROFESSORCAMPONUMERO, wxID_FRAMEADDPROFESSORCAMPOUF, 
 wxID_FRAMEADDPROFESSORNOMEBAIRRO, wxID_FRAMEADDPROFESSORNOMECELULAR, 
 wxID_FRAMEADDPROFESSORNOMECEP, wxID_FRAMEADDPROFESSORNOMECIDADE, 
 wxID_FRAMEADDPROFESSORNOMECOMPLEMENTO, wxID_FRAMEADDPROFESSORNOMECPF, 
 wxID_FRAMEADDPROFESSORNOMEDATANASC, wxID_FRAMEADDPROFESSORNOMENOME, 
 wxID_FRAMEADDPROFESSORNOMENUMERO, wxID_FRAMEADDPROFESSORNOMERUA, 
 wxID_FRAMEADDPROFESSORNOMESEXO, wxID_FRAMEADDPROFESSORNOMETELEFONE, 
 wxID_FRAMEADDPROFESSORNOMEUF, wxID_FRAMEADDPROFESSORPANEL1, 
 wxID_FRAMEADDPROFESSORSTATICBITMAP1, wxID_FRAMEADDPROFESSORSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(34)]

class FrameAddProfessor(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEADDPROFESSOR,
              name=u'FrameAddProfessor', parent=prnt, pos=wx.Point(559, 219),
              size=wx.Size(1322, 722), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Adicionar Professor - AcademicSys')
        self.SetClientSize(wx.Size(1310, 688))

        self.panel1 = wx.Panel(id=wxID_FRAMEADDPROFESSORPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1310, 688),
              style=wx.TAB_TRAVERSAL)

        self.nomeNome = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENOME,
              label=u'Nome:', name=u'nomeNome', parent=self.panel1,
              pos=wx.Point(407, 218), size=wx.Size(32, 13), style=0)

        self.nomeDataNasc = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEDATANASC,
              label=u'Data de Nascimento:', name=u'nomeDataNasc',
              parent=self.panel1, pos=wx.Point(407, 274), size=wx.Size(101, 13),
              style=0)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.panel1,
              pos=wx.Point(408, 167), size=wx.Size(23, 13), style=0)

        self.nomeSexo = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMESEXO,
              label=u'Sexo:', name=u'nomeSexo', parent=self.panel1,
              pos=wx.Point(723, 274), size=wx.Size(29, 13), style=0)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.panel1,
              pos=wx.Point(407, 328), size=wx.Size(24, 13), style=0)

        self.nomeRua = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMERUA,
              label=u'Endereco:', name=u'nomeRua', parent=self.panel1,
              pos=wx.Point(407, 384), size=wx.Size(50, 13), style=0)

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.panel1,
              pos=wx.Point(407, 441), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.panel1,
              pos=wx.Point(685, 440), size=wx.Size(38, 13), style=0)

        self.nomeUF = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.panel1,
              pos=wx.Point(630, 492), size=wx.Size(18, 13), style=0)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMENUMERO,
              label=u'Numero:', name=u'nomeNumero', parent=self.panel1,
              pos=wx.Point(408, 491), size=wx.Size(42, 13), style=0)

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.panel1, pos=wx.Point(407, 540), size=wx.Size(70, 13),
              style=0)

        self.campoNome = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONOME,
              name=u'campoNome', parent=self.panel1, pos=wx.Point(407, 240),
              size=wx.Size(498, 21), style=0, value=u'')

        self.campoNomeP = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONOMEP,
              name=u'campoNomeP', parent=self.panel1, pos=wx.Point(407, 296),
              size=wx.Size(122, 21), style=0, value=u'')

        self.campoCPF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCPF,
              name=u'campoCPF', parent=self.panel1, pos=wx.Point(411, 190),
              size=wx.Size(139, 21), style=0, value=u'')

        self.botaoMasc = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOMASC,
              label=u'Masculino', name=u'botaoMasc', parent=self.panel1,
              pos=wx.Point(733, 297), size=wx.Size(81, 13), style=0)
        self.botaoMasc.SetValue(True)

        self.botaoFeminino = wx.RadioButton(id=wxID_FRAMEADDPROFESSORBOTAOFEMININO,
              label=u'Feminino', name=u'botaoFeminino', parent=self.panel1,
              pos=wx.Point(828, 298), size=wx.Size(81, 13), style=0)
        self.botaoFeminino.SetValue(True)

        self.campoCep = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCEP,
              name=u'campoCep', parent=self.panel1, pos=wx.Point(407, 352),
              size=wx.Size(100, 21), style=0, value=u'')

        self.botaoBuscar = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOBUSCAR,
              label=u'Buscar CEP', name=u'botaoBuscar', parent=self.panel1,
              pos=wx.Point(530, 350), size=wx.Size(75, 23), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOENDERECO,
              name=u'campoEndereco', parent=self.panel1, pos=wx.Point(407, 408),
              size=wx.Size(499, 21), style=0, value=u'')

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOBAIRRO,
              name=u'campoBairro', parent=self.panel1, pos=wx.Point(406, 462),
              size=wx.Size(232, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCIDADE,
              name=u'campoCidade', parent=self.panel1, pos=wx.Point(684, 462),
              size=wx.Size(224, 21), style=0, value=u'')

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPONUMERO,
              name=u'campoNumero', parent=self.panel1, pos=wx.Point(407, 512),
              size=wx.Size(100, 21), style=0, value=u'')

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.panel1, pos=wx.Point(407,
              566), size=wx.Size(499, 21), style=0, value=u'')

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOUF,
              name=u'campoUF', parent=self.panel1, pos=wx.Point(653, 512),
              size=wx.Size(32, 21), style=0, value=u'')

        self.botaoEditar = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOEDITAR,
              label=u'EDITAR', name=u'botaoEditar', parent=self.panel1,
              pos=wx.Point(833, 624), size=wx.Size(75, 23), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMETELEFONE,
              label=u'Fixo:', name=u'nomeTelefone', parent=self.panel1,
              pos=wx.Point(407, 604), size=wx.Size(25, 13), style=0)

        self.campoFixo = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOFIXO,
              name=u'campoFixo', parent=self.panel1, pos=wx.Point(407, 628),
              size=wx.Size(163, 21), style=0, value=u'')

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEADDPROFESSORNOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.panel1,
              pos=wx.Point(618, 603), size=wx.Size(38, 13), style=0)

        self.campoCelular = wx.TextCtrl(id=wxID_FRAMEADDPROFESSORCAMPOCELULAR,
              name=u'campoCelular', parent=self.panel1, pos=wx.Point(622, 627),
              size=wx.Size(180, 21), style=0, value=u'')

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEADDPROFESSORSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(367, 155),
              size=wx.Size(575, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/Users/Flavindias/Desenvolvimento/Laboratorio de Programa\xe7\xe3o/sistema-academico-ufrpe/Resource/Interface Gr\xe1fica/Imagens/logo pequeno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEADDPROFESSORSTATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(518, 24),
              size=wx.Size(274, 112), style=0)
        self.staticBitmap1.Center(wx.HORIZONTAL)

        self.botaoCarregar = wx.Button(id=wxID_FRAMEADDPROFESSORBOTAOCARREGAR,
              label=u'Carregar Dados', name=u'botaoCarregar',
              parent=self.panel1, pos=wx.Point(568, 187), size=wx.Size(96, 23),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
