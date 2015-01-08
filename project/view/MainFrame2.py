# coding:utf-8
import wx


class MainFrame(wx.Frame):
    mainSizer = None
    # only one menu bar in the mainframe,includes file menu and about menu
    menuBar = None
    fileMenu = None
    aboutMenu = None
    # the system specification area, includes processor panel, and so on
    specSizer = None
    # the processor panel includes several processor, each in a spec_propanel
    proSizer = None
    proAddButton = None
    specProcessor = []
    proN = 0
    # the result area
    resultPanel = None

    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.init_filemenu()
        self.init_aboutmenu()
        self.init_menubar()

        self.init_specpanel()

        self.init_propanel()
        self.init_spec_propanel()

        self.init_resultpanel()

        self.verify_button = wx.Button(self, size=(70, -1), label="Verify!!")
        self.Bind(wx.EVT_BUTTON, self.on_verify, self.verify_button)
        self.mainSizer.Add(self.specSizer)
        self.mainSizer.Add(self.verify_button)
        self.mainSizer.Add(self.resultPanel)
        self.SetSizerAndFit(self.mainSizer)

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

    def init_specpanel(self):
        self.specSizer = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(self, label="System Specification")
        self.specSizer.Add(st)

    def init_propanel(self):
        self.proSizer = wx.BoxSizer(wx.VERTICAL)
        processor = wx.StaticText(self, label="Processors: ")
        self.proSizer.Add(processor)
        self.proAddButton = wx.Button(self, size=(70, -1), label="Add")
        self.proSizer.Add(self.proAddButton)
        self.proAddButton.Bind(wx.EVT_BUTTON, self.on_pro_add_button, self.proAddButton)

    def init_spec_propanel(self):
        self.specProcessor.append(SpecProPanel(self, self.proN))
        self.proSizer.Add(self.specProcessor[self.proN].processorGrid)
        self.specSizer.Add(self.proSizer)

    def init_resultpanel(self):
        self.resultPanel = wx.Panel(self, size=(900, 500))
        # result = wx.StaticText(self.resultpanel, label="Result:")
        self.resultPanel.SetBackgroundColour('#00ffff')

    def on_quit(self, e):
        self.Close()

    def on_pro_del_button(self, e, mark):
        button = e.GetEventObject()
        print button.GetLabel()
        self.specProcessor[mark].processorGrid.DeleteWindows()
        self.proSizer.Remove(self.specProcessor[mark].processorGrid)
        self.specProcessor.remove(self.specProcessor[mark])
        self.mainSizer.Layout()
        self.proN -= 1

    def on_pro_add_button(self, e):
        self.proN += 1
        self.specProcessor.append(SpecProPanel(self, self.proN))
        self.specProcessor[self.proN].proDelButton.Bind(wx.EVT_BUTTON, lambda evt, mark=self.specProcessor[self.proN].id: self.on_pro_del_button(evt, mark), self.specProcessor[self.proN].proDelButton)
        self.specProcessor[self.proN].SetSizerAndFit(self.specProcessor[self.proN].processorGrid)
        self.proSizer.Add(self.specProcessor[self.proN].processorGrid)
        self.mainSizer.Layout()

    def on_verify(self, e):
        print 1


class FirstSpecProPanel(wx.Panel):
    id = None
    processorGrid = None
    pName = None
    editPname = None
    policy = None
    policyList = ['RMS', 'EDF']
    policyCombo = None
    preempt = None
    preemptList = ['true', 'false']
    preemptCombo = None

    def __init__(self, parent, n):
        wx.Panel.__init__(self, parent, n)
        self.id = n
        self.processorGrid = wx.GridBagSizer(hgap=4, vgap=2)
        self.pName = wx.StaticText(self, label="name: ")
        self.processorGrid.Add(self.pName, pos=(0, 0))

        self.editPname = wx.TextCtrl(self, size=(70, -1))
        self.processorGrid.Add(self.editPname, pos=(1, 0))

        self.policy = wx.StaticText(self, label="policy: ")
        self.processorGrid.Add(self.policy, pos=(0, 1))

        self.policyCombo = wx.ComboBox(self, -1, size=(70, -1), value="", choices=self.policyList, style=wx.CB_DROPDOWN)
        self.processorGrid.Add(self.policyCombo, pos=(1, 1))

        self.preempt = wx.StaticText(self, label="preemptible?: ")
        self.processorGrid.Add(self.preempt, pos=(0, 2))

        self.preemptCombo = wx.ComboBox(self, -1, size=(70, -1), value="", choices=self.preemptList, style=wx.CB_DROPDOWN)
        self.processorGrid.Add(self.preemptCombo, pos=(1, 2))


class SpecProPanel(FirstSpecProPanel):
    proDelButton = None

    def __init__(self, parent, n):
        FirstSpecProPanel.__init__(self, parent, n)
        self.proDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.processorGrid.Add(self.proDelButton, pos=(1, 3))


def main():
    app = wx.App()
    frame = MainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()