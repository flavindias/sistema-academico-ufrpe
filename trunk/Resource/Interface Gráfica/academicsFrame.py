#Boa:Frame:Sistema_Academico

import wx
import ponte

def create(parent):
    return Sistema_Academico(parent)

[wxID_SISTEMA_ACADEMICO, wxID_SISTEMA_ACADEMICOGERALUNOSTATICTEXT, 
 wxID_SISTEMA_ACADEMICOGERDISCSTATICTEXT, 
 wxID_SISTEMA_ACADEMICOGERENCIAR_ALUNO, 
 wxID_SISTEMA_ACADEMICOGERENCIAR_DISCIPLINA, 
 wxID_SISTEMA_ACADEMICOGERENCIAR_FUNCIONARIO, 
 wxID_SISTEMA_ACADEMICOGERENCIAR_PROFESSOR, 
 wxID_SISTEMA_ACADEMICOGERFUNSTATICTEXT, 
 wxID_SISTEMA_ACADEMICOGERPROFSTATICTEXT, 
 wxID_SISTEMA_ACADEMICOGERTURMASTATICTEXT1, 
 wxID_SISTEMA_ACADEMICOGER_TURMABITMAPBUTTON, wxID_SISTEMA_ACADEMICOLOGOFF, 
 wxID_SISTEMA_ACADEMICOLOGOMARCA, wxID_SISTEMA_ACADEMICONOMESTATICTEXT1, 
 wxID_SISTEMA_ACADEMICOSTATICLINE2, wxID_SISTEMA_ACADEMICOVINDOSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(16)]

class Sistema_Academico(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SISTEMA_ACADEMICO,
              name=u'Sistema_Academico', parent=prnt, pos=wx.Point(48, 16),
              size=wx.Size(1318, 722), style=wx.CAPTION,
              title=u'Sistema Academico')
        self.SetClientSize(wx.Size(1310, 688))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.SetToolTipString(u'Frame')
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Imagens/Icone.ico',wx.BITMAP_TYPE_ICO))

        self.Gerenciar_Aluno = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Man-128.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SISTEMA_ACADEMICOGERENCIAR_ALUNO,
              name=u'Gerenciar_Aluno', parent=self, pos=wx.Point(187, 276),
              size=wx.Size(160, 136), style=wx.BU_AUTODRAW)
        self.Gerenciar_Aluno.Bind(wx.EVT_BUTTON, self.OnGerenciar_AlunoButton,
              id=wxID_SISTEMA_ACADEMICOGERENCIAR_ALUNO)

        self.Gerenciar_Professor = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Supervisor-128.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SISTEMA_ACADEMICOGERENCIAR_PROFESSOR,
              name=u'Gerenciar_Professor', parent=self, pos=wx.Point(381, 277),
              size=wx.Size(160, 136), style=wx.BU_AUTODRAW)
        self.Gerenciar_Professor.Bind(wx.EVT_BUTTON,
              self.OnGerenciar_ProfessorButton,
              id=wxID_SISTEMA_ACADEMICOGERENCIAR_PROFESSOR)

        self.Gerenciar_Disciplina = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Graphite-doc-128.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_SISTEMA_ACADEMICOGERENCIAR_DISCIPLINA,
              name=u'Gerenciar_Disciplina', parent=self, pos=wx.Point(575, 276),
              size=wx.Size(160, 136), style=wx.BU_AUTODRAW)
        self.Gerenciar_Disciplina.Center(wx.BOTH)
        self.Gerenciar_Disciplina.Bind(wx.EVT_BUTTON,
              self.OnGerenciar_DisciplinaButton,
              id=wxID_SISTEMA_ACADEMICOGERENCIAR_DISCIPLINA)

        self.LogoMarca = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Imagens/logo pqueno.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SISTEMA_ACADEMICOLOGOMARCA,
              name=u'LogoMarca', parent=self, pos=wx.Point(408, 26),
              size=wx.Size(493, 158), style=0)
        self.LogoMarca.Center(wx.HORIZONTAL)

        self.LogOff = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Ball-shutdown-48.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SISTEMA_ACADEMICOLOGOFF,
              name=u'LogOff', parent=self, pos=wx.Point(1069, 548),
              size=wx.Size(64, 56), style=wx.BU_AUTODRAW)
        self.LogOff.Bind(wx.EVT_BUTTON, self.LogOffButton,
              id=wxID_SISTEMA_ACADEMICOLOGOFF)

        self.gerAlunoStaticText = wx.StaticText(id=wxID_SISTEMA_ACADEMICOGERALUNOSTATICTEXT,
              label=u'Gerenciar Aluno', name=u'gerAlunoStaticText', parent=self,
              pos=wx.Point(216, 420), size=wx.Size(107, 19), style=0)
        self.gerAlunoStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.gerAlunoStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.gerProfStaticText = wx.StaticText(id=wxID_SISTEMA_ACADEMICOGERPROFSTATICTEXT,
              label=u'Gerenciar Professor', name=u'gerProfStaticText',
              parent=self, pos=wx.Point(393, 420), size=wx.Size(131, 19),
              style=0)
        self.gerProfStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.gerProfStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.gerDiscStaticText = wx.StaticText(id=wxID_SISTEMA_ACADEMICOGERDISCSTATICTEXT,
              label=u'Gerenciar Disciplina', name=u'gerDiscStaticText',
              parent=self, pos=wx.Point(588, 421), size=wx.Size(133, 19),
              style=0)
        self.gerDiscStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.gerDiscStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.Gerenciar_Funcionario = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/Boss-128.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_SISTEMA_ACADEMICOGERENCIAR_FUNCIONARIO,
              name=u'Gerenciar_Funcionario', parent=self, pos=wx.Point(969,
              275), size=wx.Size(160, 136), style=wx.BU_AUTODRAW)

        self.gerFunStaticText = wx.StaticText(id=wxID_SISTEMA_ACADEMICOGERFUNSTATICTEXT,
              label=u'Gerenciar Funcion\xe1rio', name=u'gerFunStaticText',
              parent=self, pos=wx.Point(977, 427), size=wx.Size(148, 19),
              style=0)
        self.gerFunStaticText.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.gerFunStaticText.SetForegroundColour(wx.Colour(145, 145, 145))

        self.vindoStaticText1 = wx.StaticText(id=wxID_SISTEMA_ACADEMICOVINDOSTATICTEXT1,
              label=u'Bem-Vindo:', name=u'vindoStaticText1', parent=self,
              pos=wx.Point(231, 511), size=wx.Size(92, 21), style=0)
        self.vindoStaticText1.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.vindoStaticText1.SetForegroundColour(wx.Colour(145, 145, 145))

        self.nomeStaticText1 = wx.StaticText(id=wxID_SISTEMA_ACADEMICONOMESTATICTEXT1,
              label=u'', name=u'nomeStaticText1', parent=self, pos=wx.Point(331,
              510), size=wx.Size(0, 21), style=0)
        self.nomeStaticText1.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Times New Roman'))

        self.Ger_TurmaBitmapButton = wx.BitmapButton(bitmap=wx.Bitmap(u'./Imagens/User-group-128.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_SISTEMA_ACADEMICOGER_TURMABITMAPBUTTON,
              name=u'Ger_TurmaBitmapButton', parent=self, pos=wx.Point(774,
              276), size=wx.Size(160, 136), style=wx.BU_AUTODRAW)
        self.Ger_TurmaBitmapButton.Bind(wx.EVT_BUTTON,
              self.OnGer_TurmaBitmapButton,
              id=wxID_SISTEMA_ACADEMICOGER_TURMABITMAPBUTTON)

        self.gerTurmaStaticText1 = wx.StaticText(id=wxID_SISTEMA_ACADEMICOGERTURMASTATICTEXT1,
              label=u'Gerenciar Turma', name=u'gerTurmaStaticText1',
              parent=self, pos=wx.Point(806, 421), size=wx.Size(112, 19),
              style=0)
        self.gerTurmaStaticText1.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Times New Roman'))
        self.gerTurmaStaticText1.SetForegroundColour(wx.Colour(145, 145, 145))

        self.staticLine2 = wx.StaticLine(id=wxID_SISTEMA_ACADEMICOSTATICLINE2,
              name='staticLine2', parent=self, pos=wx.Point(205, 217),
              size=wx.Size(899, 1), style=0)
        self.staticLine2.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def LogOffButton(self, event):
        self.Close(True)
        ponte.mainFrameLogonApp()
        exit()
        event.Skip()

    def Gerenciar_DisciplinaButton(self, event):
        event.Skip()

    def OnGerenciar_DisciplinaButton(self, event):
        self.Close(True)
        ponte.mainFrameGerDisciplinaApp()
        exit()
        event.Skip()

    def OnGerenciar_ProfessorButton(self, event):
        self.Close(True)
        ponte.mainFrameGerProfessorApp()
        exit()
        event.Skip()

    def OnGerenciar_AlunoButton(self, event):
        self.Close(True)
        ponte.mainFrameGerAlunoApp()
        exit()
        event.Skip()

    def OnGer_TurmaBitmapButton(self, event):
        event.Skip()
