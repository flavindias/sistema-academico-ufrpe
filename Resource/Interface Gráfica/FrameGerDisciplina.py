#Boa:Frame:frameGerDisciplina
import sys
import os
import wx
import academics

lista = sys.path[0].split('\\')
temp = ''
for i in range(len(lista)):
    if i != len(lista)-1:
        temp += lista[i]
        temp += '\\'
    else:
        temp += 'Modules'
sys.path[0] = temp

from newDisciplina import Disciplina
from newProfessor import Professor

def create(parent):
    return frameGerDisciplina(parent)

[wxID_FRAMEGERDISCIPLINA, wxID_FRAMEGERDISCIPLINAACADEMICSSTATICBITMAP, 
 wxID_FRAMEGERDISCIPLINAAPLICARBUTTON, wxID_FRAMEGERDISCIPLINADISCLISTBOX, 
 wxID_FRAMEGERDISCIPLINADISCSTATICBOX, wxID_FRAMEGERDISCIPLINAEDITARBUTTON, 
 wxID_FRAMEGERDISCIPLINAERROTEXTCTRL, wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON, 
 wxID_FRAMEGERDISCIPLINANOMEDISCSTATICTEXT, 
 wxID_FRAMEGERDISCIPLINANOMETEXTCTRL, wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1, 
 wxID_FRAMEGERDISCIPLINAPROFCHOICE, 
 wxID_FRAMEGERDISCIPLINAPROFDISCSTATICTEXT1, 
 wxID_FRAMEGERDISCIPLINASTATICBITMAP1, wxID_FRAMEGERDISCIPLINASTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(15)]

class frameGerDisciplina(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERDISCIPLINA,
              name=u'frameGerDisciplina', parent=prnt, pos=wx.Point(520, 68),
              size=wx.Size(696, 670), style=wx.CAPTION,
              title=u'Gerenciar Disciplina')
        self.SetClientSize(wx.Size(690, 638))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.discListBox = wx.ListBox(choices=[],
              id=wxID_FRAMEGERDISCIPLINADISCLISTBOX, name=u'discListBox',
              parent=self, pos=wx.Point(40, 264), size=wx.Size(288, 288),
              style=wx.NO_BORDER | wx.LB_ALWAYS_SB)
        self.discListBox.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnDiscListBoxListboxDclick,
              id=wxID_FRAMEGERDISCIPLINADISCLISTBOX)

        self.nomeTextCtrl = wx.TextCtrl(id=wxID_FRAMEGERDISCIPLINANOMETEXTCTRL,
              name=u'nomeTextCtrl', parent=self, pos=wx.Point(104, 144),
              size=wx.Size(232, 21), style=0, value=u'')

        self.editarButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAEDITARBUTTON,
              label=u'Editar', name=u'editarButton', parent=self,
              pos=wx.Point(344, 256), size=wx.Size(50, 50), style=0)
        self.editarButton.Bind(wx.EVT_BUTTON, self.OnEditarButtonButton,
              id=wxID_FRAMEGERDISCIPLINAEDITARBUTTON)

        self.excluirButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON,
              label=u'Excluir', name=u'excluirButton', parent=self,
              pos=wx.Point(344, 320), size=wx.Size(50, 50), style=0)
        self.excluirButton.Bind(wx.EVT_BUTTON, self.OnExcluirButtonButton,
              id=wxID_FRAMEGERDISCIPLINAEXCLUIRBUTTON)

        self.nomeDiscStaticText = wx.StaticText(id=wxID_FRAMEGERDISCIPLINANOMEDISCSTATICTEXT,
              label=u'Nome', name=u'nomeDiscStaticText', parent=self,
              pos=wx.Point(32, 144), size=wx.Size(38, 19), style=0)
        self.nomeDiscStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.nomeDiscStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.profDiscStaticText1 = wx.StaticText(id=wxID_FRAMEGERDISCIPLINAPROFDISCSTATICTEXT1,
              label=u'Professor', name=u'profDiscStaticText1', parent=self,
              pos=wx.Point(32, 192), size=wx.Size(62, 19), style=0)
        self.profDiscStaticText1.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.profDiscStaticText1.SetForegroundColour(wx.Colour(145, 145, 145))

        self.aplicarButton = wx.Button(id=wxID_FRAMEGERDISCIPLINAAPLICARBUTTON,
              label=u'Aplicar', name=u'aplicarButton', parent=self,
              pos=wx.Point(344, 144), size=wx.Size(50, 50), style=0)
        self.aplicarButton.Bind(wx.EVT_BUTTON, self.OnAplicarButtonButton,
              id=wxID_FRAMEGERDISCIPLINAAPLICARBUTTON)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/NovoLivros.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERDISCIPLINASTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(456, 168),
              size=wx.Size(208, 312), style=0)

        self.okBitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/botaoVoltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1,
              name=u'okBitmapButton1', parent=self, pos=wx.Point(600, 552),
              size=wx.Size(50, 50), style=wx.BU_AUTODRAW)
        self.okBitmapButton1.Bind(wx.EVT_BUTTON, self.DiscReturnMenu,
              id=wxID_FRAMEGERDISCIPLINAOKBITMAPBUTTON1)

        self.profChoice = wx.Choice(choices=self.listProf,
              id=wxID_FRAMEGERDISCIPLINAPROFCHOICE, name=u'profChoice',
              parent=self, pos=wx.Point(104, 192), size=wx.Size(232, 21),
              style=0)

        self.discStaticBox = wx.StaticBox(id=wxID_FRAMEGERDISCIPLINADISCSTATICBOX,
              label=u'Disciplinas', name=u'discStaticBox', parent=self,
              pos=wx.Point(32, 248), size=wx.Size(304, 312), style=0)
        self.discStaticBox.SetForegroundColour(wx.Colour(145, 145, 145))
        self.discStaticBox.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.erroTextCtrl = wx.TextCtrl(id=wxID_FRAMEGERDISCIPLINAERROTEXTCTRL,
              name=u'erroTextCtrl', parent=self, pos=wx.Point(32, 592),
              size=wx.Size(488, 21), style=wx.NO_BORDER, value=u'')
        self.erroTextCtrl.SetForegroundColour(wx.Colour(255, 0, 0))
        self.erroTextCtrl.SetFont(wx.Font(10, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Times New Roman'))

        self.staticLine1 = wx.StaticLine(id=wxID_FRAMEGERDISCIPLINASTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(100, 120),
              size=wx.Size(487, 1), style=0)
        self.staticLine1.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.staticLine1.Center(wx.HORIZONTAL)
        self.staticLine1.SetAutoLayout(False)

        self.academicsStaticBitmap = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pequeno.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERDISCIPLINAACADEMICSSTATICBITMAP,
              name=u'academicsStaticBitmap', parent=self, pos=wx.Point(207, 0),
              size=wx.Size(274, 112), style=0)
        self.academicsStaticBitmap.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self.verificador = 0
        #self.carregarProf()
        self.listProf= []
        self._init_ctrls(parent)
        self.carregarDisc()
        
    def DiscReturnMenu(self, event):
        self.Close(True)
        academics.comeca()
        exit()
        event.Skip()

    def OnDiscListBoxListboxDclick(self, event):
        self.verificador = 1
        self.editDisc()
        event.Skip()
        
    def carregarProf(self):
        prof = Professor()
        self.listProfId = prof.listaDb()
        self.listProf = []
        for i in self.listProfId:
            self.listProf += [i[1]]
    
    def carregarDisc(self):
        disc = Disciplina()
        prof = Professor()
        self.listDisc = disc.listaDb()
        listDiscBox = []
        self.listDiscId = []
        for i in self.listDisc:
            prof.carregar(i[1])
            listDiscBox += [str(i[0]) + ' - ' + str(prof.getNome())]
        self.discListBox.Set(listDiscBox)
        
    def delDisc(self):
        if self.discListBox.GetSelections() == ():
            self.erroTextCtrl.SetValue('Selecione uma Disciplina para deletar!')
        else:
            self.erroTextCtrl.SetValue('')
            disc = Disciplina()
            disc.delete(self.listDisc[self.discListBox.GetSelections()[-1]][0])
        
    def editDisc(self):
        self.nomeTextCtrl.SetValue(self.listDisc[self.discListBox.GetSelections()[-1]][0])
    
    def addDisc(self):
        if (self.nomeTextCtrl.GetValue() == '') or (self.profChoice.GetSelection() == -1):
            self.erroTextCtrl.SetValue('Insira um Nome e um Professor para adicionar uma nova Disciplina!')
        else:
            self.erroTextCtrl.SetValue('')
            disc = Disciplina()
            disc.setDisciplina(self.nomeTextCtrl.GetValue())
            select = self.profChoice.GetSelection()
            disc.setProfessor(self.listProfId[select][0])
            disc.add()
            self.nomeTextCtrl.SetValue('')

    def OnEditarButtonButton(self, event):
        self.verificador = 1
        self.editDisc()
        event.Skip()

    def OnExcluirButtonButton(self, event):
        self.delDisc()
        self.carregarDisc()
        event.Skip()

    def OnAplicarButtonButton(self, event):
        if self.verificador == 1:
            if (self.nomeTextCtrl.GetValue() == ''):
                self.erroTextCtrl.SetValue('Insira um Nome para Editar a Disciplina!')
            else:
                self.discEdit.setDisciplina(self.nomeTextCtrl.GetValue())
                select = self.profChoice.GetSelection()
                if (select == -1):None
                else:
                    self.discEdit.setProfessor(self.listProfId[select][0])
                self.discEdit.salvarEdit(self.discEdit.getDisciplina(), self.discEdit.getProfessor())
                self.verificador = 0
                self.discEdit = None
                self.nomeTextCtrl.SetValue('')
                self.carregarDisc()
        else:
            self.addDisc()
            self.carregarDisc()
        event.Skip()
