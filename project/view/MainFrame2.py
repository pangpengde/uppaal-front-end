# coding:utf-8
import wx


class MainFrame(wx.Frame):
    mainSizer = None
    mainPanel = None
    # only one menu bar in the mainframe,includes file menu and about menu
    menuBar = None
    fileMenu = None
    aboutMenu = None
    # the system specification area
    specSizer = None
    # the processor panel includes several processor
    proSizer = None
    proAddButton = None
    processorPanels = []
    proN = 0
    # the result area
    resultPanel = None

    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.mainPanel = wx.Panel(self, size=(900, 600))
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.init_filemenu()
        self.init_aboutmenu()
        self.init_menubar()

        self.init_spec_sizer()
        self.init_pro_sizer()
        self.init_spec_propanel()
        self.init_resultpanel()

        self.verify_button = wx.Button(self.mainPanel, size=(70, -1), label="Verify!!")
        self.Bind(wx.EVT_BUTTON, self.on_verify, self.verify_button)
        self.mainSizer.Add(self.specSizer)
        self.mainSizer.Add(self.verify_button)
        self.mainSizer.Add(self.resultPanel)
        self.mainPanel.SetSizerAndFit(self.mainSizer)

    def init_menubar(self):
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, '&File')
        self.menuBar.Append(self.aboutMenu, '&About')
        self.SetMenuBar(self.menuBar)

    def init_filemenu(self):
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(wx.ID_NEW, '&New', 'Start to describe a new system')
        self.fileMenu.Append(wx.ID_OPEN, '&Open', 'Open a exist system specification')
        self.fileMenu.Append(wx.ID_SAVE, '&Save', 'Save system specification')
        self.fileMenu.AppendSeparator()
        fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Tool')
        self.Bind(wx.EVT_MENU, self.on_quit, fitem)

    def init_aboutmenu(self):
        self.aboutMenu = wx.Menu()
        self.aboutMenu.Append(wx.ID_ABOUT, '&About', 'About this tool')

    def init_spec_sizer(self):
        self.specSizer = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(self.mainPanel, label="System Specification")
        self.specSizer.Add(st)

    def init_pro_sizer(self):
        self.proSizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        processor = wx.StaticText(self.mainPanel, label="Processors: ")
        h_sizer.Add(processor)
        self.proAddButton = wx.Button(self.mainPanel, size=(70, -1), label="Add")
        self.proAddButton.Bind(wx.EVT_BUTTON, self.on_pro_add_button, self.proAddButton)
        h_sizer.Add(self.proAddButton)
        h_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pName = wx.StaticText(self.mainPanel, label="name: ", size=(70, -1))
        h_text_sizer.Add(pName)
        policy = wx.StaticText(self.mainPanel, label="policy: ", size=(70, -1))
        h_text_sizer.Add(policy)
        preempt = wx.StaticText(self.mainPanel, label="preemptible?: ", size=(70, -1))
        h_text_sizer.Add(preempt)
        self.proSizer.Add(h_sizer)
        self.proSizer.Add(h_text_sizer)

    def init_spec_propanel(self):
        self.processorPanels.append(FirstSpecProcessor(self.mainPanel, self.proN))
        self.proSizer.Add(self.processorPanels[self.proN])
        self.specSizer.Add(self.proSizer)

    def init_resultpanel(self):
        self.resultPanel = wx.Panel(self.mainPanel, size=(900, 500))
        # result = wx.StaticText(self.resultpanel, label="Result:")
        self.resultPanel.SetBackgroundColour('#00ffff')

    def on_quit(self, e):
        self.Close()

    def on_pro_del_button(self, e, mark):
        button = e.GetEventObject()
        self.processorPanels[mark].processorSizer.DeleteWindows()
        self.proSizer.Remove(self.processorPanels[mark])
        self.processorPanels.remove(self.processorPanels[mark])
        self.mainSizer.Layout()
        self.proN -= 1

    def on_pro_add_button(self, e):
        self.proN += 1
        self.processorPanels.append(SpecProcessor(self.mainPanel, self.proN))
        self.processorPanels[self.proN].proDelButton.Bind(wx.EVT_BUTTON, lambda evt, mark=self.processorPanels[self.proN].id: self.on_pro_del_button(evt, mark), self.processorPanels[self.proN].proDelButton)
        self.proSizer.Add(self.processorPanels[self.proN])
        self.mainSizer.Layout()

    def on_verify(self, e):
        print 1


class FirstSpecProcessor(wx.Panel):
    id = None
    processorSizer = None
    editPname = None
    policyList = ['RMS', 'EDF']
    policyCombo = None
    preemptList = ['true', 'false']
    preemptCombo = None

    def __init__(self, parent, n):
        wx.Panel.__init__(self, parent, n)
        self.id = n
        self.processorSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.editPname = wx.TextCtrl(self, size=(70, -1))
        self.processorSizer.Add(self.editPname)

        self.policyCombo = wx.ComboBox(self, -1, size=(70, -1), value="", choices=self.policyList, style=wx.CB_DROPDOWN)
        self.processorSizer.Add(self.policyCombo)

        self.preemptCombo = wx.ComboBox(self, -1, size=(70, -1), value="", choices=self.preemptList, style=wx.CB_DROPDOWN)
        self.processorSizer.Add(self.preemptCombo)
        self.SetSizerAndFit(self.processorSizer)


class SpecProcessor(FirstSpecProcessor):
    proDelButton = None

    def __init__(self, parent, n):
        FirstSpecProcessor.__init__(self, parent, n)
        self.proDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.processorSizer.Add(self.proDelButton)
        self.SetSizerAndFit(self.processorSizer)


def main():
    app = wx.App()
    frame = MainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()