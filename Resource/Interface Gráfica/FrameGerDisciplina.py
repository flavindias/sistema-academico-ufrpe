#Boa:Frame:frameGerDisciplina

import wx
import Disciplina
import Professor
import DadosPessoais

def create(parent):
    return frameGerDisciplina(parent)

[wxID_FRAMEGERDISCIPLINA, wxID_FRAMEGERDISCIPLINAAPLICARBUTTON, 
 wxID_FRAMEGERDISCIPLINADISCLISTBOX, wxID_FRAMEGERDISCIPLINADISCSTATICBOX, 
 wxID_FRAMEGERDISCIPLINAEDITARBUTTON, wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON, 
 wxID_FRAMEGERDISCIPLINANOMEDISCSTATICTEXT, 
 wxID_FRAMEGERDISCIPLINANOMETEXTCTRL, wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1, 
 wxID_FRAMEGERDISCIPLINAPROFCHOICE, 
 wxID_FRAMEGERDISCIPLINAPROFDISCSTATICTEXT1, 
 wxID_FRAMEGERDISCIPLINASTATICBITMAP1, wxID_FRAMEGERDISCIPLINASTATICTEXT1, 
 wxID_FRAMEGERDISCIPLINATESTE, 
] = [wx.NewId() for _init_ctrls in range(14)]

class frameGerDisciplina(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERDISCIPLINA,
              name=u'frameGerDisciplina', parent=prnt, pos=wx.Point(516, 98),
              size=wx.Size(703, 640),
              style=wx.DEFAULT_FRAME_STYLE | wx.RAISED_BORDER | wx.CLOSE_BOX | wx.MAXIMIZE_BOX,
              title=u'Gerenciar Disciplina')
        self.SetClientSize(wx.Size(695, 606))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.discListBox = wx.ListBox(choices=[],
              id=wxID_FRAMEGERDISCIPLINADISCLISTBOX, name=u'discListBox',
              parent=self, pos=wx.Point(40, 208), size=wx.Size(288, 288),
              style=wx.NO_BORDER | wx.LB_ALWAYS_SB)
        self.discListBox.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnDiscListBoxListboxDclick,
              id=wxID_FRAMEGERDISCIPLINADISCLISTBOX)

        self.nomeTextCtrl = wx.TextCtrl(id=wxID_FRAMEGERDISCIPLINANOMETEXTCTRL,
              name=u'nomeTextCtrl', parent=self, pos=wx.Point(104, 72),
              size=wx.Size(232, 21), style=0, value=u'')

        self.editarButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAEDITARBUTTON,
              label=u'Editar', name=u'editarButton', parent=self,
              pos=wx.Point(344, 200), size=wx.Size(75, 23), style=0)
        self.editarButton.Bind(wx.EVT_BUTTON, self.OnEditarButtonButton,
              id=wxID_FRAMEGERDISCIPLINAEDITARBUTTON)

        self.excluirButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON,
              label=u'Excluir', name=u'excluirButton', parent=self,
              pos=wx.Point(344, 232), size=wx.Size(75, 23), style=0)
        self.excluirButton.Bind(wx.EVT_BUTTON, self.OnExcluirButtonButton,
              id=wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON)

        self.nomeDiscStaticText = wx.StaticText(id=wxID_FRAMEGERDISCIPLINANOMEDISCSTATICTEXT,
              label=u'Nome', name=u'nomeDiscStaticText', parent=self,
              pos=wx.Point(32, 72), size=wx.Size(38, 19), style=0)
        self.nomeDiscStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.nomeDiscStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.profDiscStaticText1 = wx.StaticText(id=wxID_FRAMEGERDISCIPLINAPROFDISCSTATICTEXT1,
              label=u'Professor', name=u'profDiscStaticText1', parent=self,
              pos=wx.Point(32, 128), size=wx.Size(62, 19), style=0)
        self.profDiscStaticText1.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.profDiscStaticText1.SetForegroundColour(wx.Colour(145, 145, 145))

        self.aplicarButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAAPLICARBUTTON,
              label=u'Aplicar', name=u'aplicarButton', parent=self,
              pos=wx.Point(344, 72), size=wx.Size(75, 23), style=0)
        self.aplicarButton.Bind(wx.EVT_BUTTON, self.OnAplicarButtonButton,
              id=wxID_FRAMEGERDISCIPLINAAPLICARBUTTON)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEGERDISCIPLINASTATICTEXT1,
              label=u'Gerenciar Disciplina', name='staticText1', parent=self,
              pos=wx.Point(232, 16), size=wx.Size(180, 23), style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Times New Roman'))
        self.staticText1.SetForegroundColour(wx.Colour(145, 145, 145))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/NovoLivros.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERDISCIPLINASTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(456, 128),
              size=wx.Size(208, 312), style=0)

        self.okBitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Emblem-Ok-48.PNG',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1,
              name=u'okBitmapButton1', parent=self, pos=wx.Point(600, 520),
              size=wx.Size(64, 56), style=wx.BU_AUTODRAW)
        self.okBitmapButton1.Bind(wx.EVT_BUTTON, self.DiscReturnMenu,
              id=wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1)

        self.profChoice = wx.Choice(choices=[],
              id=wxID_FRAMEGERDISCIPLINAPROFCHOICE, name=u'profChoice',
              parent=self, pos=wx.Point(104, 128), size=wx.Size(232, 21),
              style=0)

        self.discStaticBox = wx.StaticBox(id=wxID_FRAMEGERDISCIPLINADISCSTATICBOX,
              label=u'Disciplinas', name=u'discStaticBox', parent=self,
              pos=wx.Point(32, 192), size=wx.Size(304, 312), style=0)
        self.discStaticBox.SetForegroundColour(wx.Colour(145, 145, 145))
        self.discStaticBox.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.Teste = wx.TextCtrl(id=wxID_FRAMEGERDISCIPLINATESTE, name=u'Teste',
              parent=self, pos=wx.Point(496, 456), size=wx.Size(100, 21),
              style=wx.NO_BORDER, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def DiscReturnMenu(self, event):
        self.Close(True)
        event.Skip()

    def OnDiscListBoxListboxDclick(self, event):
        event.Skip()
        
    def carregarProf(self):
        
    
    def carregarDisc(self):
        disc = Disciplina()
        prof = Professor()
        dados = DadosPessoais()
        listDisc = disc.pegarId()
        listDiscBox = []
        for i in listDisc:
            disc.carregar(i)
            prof.carregar(disc.getProfessorId())
            dados.carregar(prof.getDadosId())
            listDiscBox += [disc.getNome() + ' - ' + dados.getNome()]
        self.discListBox.Set(listDiscBox)
        
    def delDisc(self):
        disc = Disciplina()
        disc.delete(self.discListBox.GetSelections())
        self.carregarDisc()
        
    def editDisc(self):
        disc = Disciplina()
        prof = Professor()
        listDiscId = disc.pegarId()
        editDisc = self.discListBox.GetSelections()
        disc.carregar(editDisc[0])
        

    def OnEditarButtonButton(self, event):
        event.Skip()

    def OnExcluirButtonButton(self, event):
        event.Skip()

    def OnAplicarButtonButton(self, event):
        self.carregarDisc()
        event.Skip()