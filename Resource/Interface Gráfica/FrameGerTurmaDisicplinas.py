#Boa:Frame:FrameGerTurmaDisciplina

import wx
import wx.lib.buttons

def create(parent):
    return FrameGerTurmaDisciplina(parent)

[wxID_FRAMEGERTURMADISCIPLINA, wxID_FRAMEGERTURMADISCIPLINABOTAOADICIONAR, 
 wxID_FRAMEGERTURMADISCIPLINABOTAOEXCLUIRTURMA, 
 wxID_FRAMEGERTURMADISCIPLINABOTAOREMOVER, 
 wxID_FRAMEGERTURMADISCIPLINABOTAOSALVARTURMA, 
 wxID_FRAMEGERTURMADISCIPLINACAIXAALUNOSTURMA, 
 wxID_FRAMEGERTURMADISCIPLINACHOICE1, wxID_FRAMEGERTURMADISCIPLINACHOICE2, 
 wxID_FRAMEGERTURMADISCIPLINAESCOLHATURMA, 
 wxID_FRAMEGERTURMADISCIPLINALISTADEDISCIPLINAS, 
 wxID_FRAMEGERTURMADISCIPLINALISTADISCIPLINAS, 
 wxID_FRAMEGERTURMADISCIPLINALISTAPROFESSORE, 
 wxID_FRAMEGERTURMADISCIPLINALOGOACADEMIC, 
 wxID_FRAMEGERTURMADISCIPLINANOMEDISCIPLINA, 
 wxID_FRAMEGERTURMADISCIPLINANOMEPROFESSOR, 
 wxID_FRAMEGERTURMADISCIPLINANOMESERIE, wxID_FRAMEGERTURMADISCIPLINANOMETURMA, 
 wxID_FRAMEGERTURMADISCIPLINANOMETURNO, wxID_FRAMEGERTURMADISCIPLINAPANEL1, 
 wxID_FRAMEGERTURMADISCIPLINASTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(20)]

class FrameGerTurmaDisciplina(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERTURMADISCIPLINA,
              name=u'FrameGerTurmaDisciplina', parent=prnt, pos=wx.Point(527,
              190), size=wx.Size(1326, 726), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Gerenciamento de Disciplina')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGERTURMADISCIPLINAPANEL1,
              name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(1310,
              688), style=wx.TAB_TRAVERSAL)

        self.logoAcademic = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pqueno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMADISCIPLINALOGOACADEMIC,
              name=u'logoAcademic', parent=self.panel1, pos=wx.Point(518, 16),
              size=wx.Size(274, 112), style=0)
        self.logoAcademic.Center(wx.HORIZONTAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERTURMADISCIPLINASTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(251, 144),
              size=wx.Size(808, 2), style=0)
        self.staticLine1.Center(wx.HORIZONTAL)

        self.choice2 = wx.Choice(choices=["Manha", "Tarde", "Noite"],
              id=wxID_FRAMEGERTURMADISCIPLINACHOICE2, name='choice2',
              parent=self.panel1, pos=wx.Point(600, 173), size=wx.Size(130, 21),
              style=0)
        self.choice2.SetStringSelection(u'Manha')

        self.nomeTurma = wx.StaticText(id=wxID_FRAMEGERTURMADISCIPLINANOMETURMA,
              label=u'Turma:', name=u'nomeTurma', parent=self.panel1,
              pos=wx.Point(752, 156), size=wx.Size(35, 13), style=0)

        self.nomeTurno = wx.StaticText(id=wxID_FRAMEGERTURMADISCIPLINANOMETURNO,
              label=u'Turno:', name=u'nomeTurno', parent=self.panel1,
              pos=wx.Point(602, 157), size=wx.Size(33, 13), style=0)

        self.nomeSerie = wx.StaticText(id=wxID_FRAMEGERTURMADISCIPLINANOMESERIE,
              label=u'Serie:', name=u'nomeSerie', parent=self.panel1,
              pos=wx.Point(432, 157), size=wx.Size(29, 13), style=0)

        self.choice1 = wx.Choice(choices=['Selecione a serie', 'Fundamental I',
              '          1 Ano', '          2 Ano', '          3 Ano',
              '          4 Ano', '          5 Ano', 'Fundamental II',
              '          6 Ano', '          7 Ano', '          8 Ano',
              '          9 Ano', 'Ensino Medio', '          1 Ano',
              '          2 Ano', '          3 Ano'],
              id=wxID_FRAMEGERTURMADISCIPLINACHOICE1, name='choice1',
              parent=self.panel1, pos=wx.Point(432, 173), size=wx.Size(130, 21),
              style=0)
        self.choice1.SetStringSelection(u'Selecione a serie')

        self.escolhaTurma = wx.Choice(choices=["A", "B", "C", "D", "E"],
              id=wxID_FRAMEGERTURMADISCIPLINAESCOLHATURMA, name=u'escolhaTurma',
              parent=self.panel1, pos=wx.Point(754, 173), size=wx.Size(130, 21),
              style=0)

        self.listadeDisciplinas = wx.ListBox(choices=[],
              id=wxID_FRAMEGERTURMADISCIPLINALISTADEDISCIPLINAS,
              name=u'listadeDisciplinas', parent=self.panel1, pos=wx.Point(728,
              240), size=wx.Size(312, 312), style=wx.LB_HSCROLL | wx.NO_BORDER)
        self.listadeDisciplinas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnProfListBoxListboxDclick,
              id=wxID_FRAMEGERTURMADISCIPLINALISTADEDISCIPLINAS)
        self.listadeDisciplinas.Bind(wx.EVT_LISTBOX, self.OnProfListBoxListbox,
              id=wxID_FRAMEGERTURMADISCIPLINALISTADEDISCIPLINAS)

        self.caixaAlunosTurma = wx.StaticBox(id=wxID_FRAMEGERTURMADISCIPLINACAIXAALUNOSTURMA,
              label=u'Lista de disciplinas', name=u'caixaAlunosTurma',
              parent=self.panel1, pos=wx.Point(712, 224), size=wx.Size(336,
              344), style=0)

        self.botaoAdicionar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/add_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMADISCIPLINABOTAOADICIONAR,
              name=u'botaoAdicionar', parent=self.panel1, pos=wx.Point(635,
              320), size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoAdicionar.Center(wx.HORIZONTAL)

        self.botaoRemover = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/del_p.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERTURMADISCIPLINABOTAOREMOVER,
              name=u'botaoRemover', parent=self.panel1, pos=wx.Point(635, 440),
              size=wx.Size(40, 40), style=wx.BU_AUTODRAW)
        self.botaoRemover.Center(wx.HORIZONTAL)

        self.botaoExcluirTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/botao excluir_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMADISCIPLINABOTAOEXCLUIRTURMA,
              label=u'   Excluir    ', name=u'botaoExcluirTurma',
              parent=self.panel1, pos=wx.Point(1112, 644), size=wx.Size(76, 30),
              style=0)

        self.botaoSalvarTurma = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap(u'./Imagens/bot\xe3o adicionar_p.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERTURMADISCIPLINABOTAOSALVARTURMA,
              label=u'    Salvar   ', name=u'botaoSalvarTurma',
              parent=self.panel1, pos=wx.Point(1204, 643), size=wx.Size(76, 30),
              style=0)

        self.nomeDisciplina = wx.StaticText(id=wxID_FRAMEGERTURMADISCIPLINANOMEDISCIPLINA,
              label=u'Disciplina:', name=u'nomeDisciplina', parent=self.panel1,
              pos=wx.Point(317, 255), size=wx.Size(48, 13), style=0)

        self.listaDisciplinas = wx.Choice(choices=[],
              id=wxID_FRAMEGERTURMADISCIPLINALISTADISCIPLINAS,
              name=u'listaDisciplinas', parent=self.panel1, pos=wx.Point(325,
              276), size=wx.Size(208, 21), style=0)

        self.nomeProfessor = wx.StaticText(id=wxID_FRAMEGERTURMADISCIPLINANOMEPROFESSOR,
              label=u'Professor:', name=u'nomeProfessor', parent=self.panel1,
              pos=wx.Point(317, 324), size=wx.Size(51, 13), style=0)

        self.listaProfessore = wx.Choice(choices=[],
              id=wxID_FRAMEGERTURMADISCIPLINALISTAPROFESSORE,
              name=u'listaProfessore', parent=self.panel1, pos=wx.Point(327,
              348), size=wx.Size(208, 21), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnProfListBoxListboxDclick(self, event):
        event.Skip()

    def OnProfListBoxListbox(self, event):
        event.Skip()
