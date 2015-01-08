# coding:utf-8
import wx


class mainFrame(wx.Frame):
    mainSizer = None
    # only one menu bar in the mainframe,includes file menu and about menu
    menuBar = None
    fileMenu = None
    aboutMenu = None
    # the system specification area, includes processor panel, and so on
    specPanel = None
    specSizer = None
    # the processor panel includes several processor, each in a spec_propanel
    proPanel = None
    proSizer = None
    spec_proPanel = []
    processorGrid = []
    proN = 0
    #bus panel, only one bus
    busPanel = None
    busSizer = None
    busGrid = None
    #task panel, similar to propanel
    taskPanel = None
    taskSizer = None
    spec_taskPanel = []
    taskGrid = []
    taskN = 0
    # the result area
    resultPanel = None

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.init_filemenu()
        self.init_aboutmenu()
        self.init_menubar()

        self.init_specpanel()

        self.init_propanel()
        self.init_spec_propanel()

        self.init_buspanel()

        self.init_taskpanel()
        self.init_spec_taskpanel()

        self.init_resultpanel()

        verify_button = wx.Button(self, size=(70, -1), label="Verify!!")
        self.Bind(wx.EVT_BUTTON, self.on_verify, verify_button)
        self.mainSizer.Add(self.specPanel)
        self.mainSizer.Add(verify_button)
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
        self.specPanel = wx.Panel(self, size=(900, 600))
        self.specSizer = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(self.specPanel, label="System Specification")
        self.specSizer.Add(st)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def init_propanel(self):
        self.proPanel = wx.Panel(self.specPanel, size=(800, 600))
        # self.propanel.SetBackgroundColour('#00ff00')
        self.proSizer = wx.BoxSizer(wx.VERTICAL)
        processor = wx.StaticText(self.proPanel, label="Processors: ")
        self.proSizer.Add(processor)

    def init_spec_propanel(self):
        self.spec_proPanel.append(wx.Panel(self.proPanel, size=(800, 100)))
        # self.spec_propanel[self.pron].SetBackgroundColour('#00ffff')
        self.processorGrid.append(wx.GridBagSizer(hgap=4, vgap=2))
        pname = wx.StaticText(self.spec_proPanel[self.proN], label="name: ")
        self.processorGrid[self.proN].Add(pname, pos=(0, 0))

        edit_pname = wx.TextCtrl(self.spec_proPanel[self.proN], size=(70, -1))
        self.processorGrid[self.proN].Add(edit_pname, pos=(1, 0))

        policy = wx.StaticText(self.spec_proPanel[self.proN], label="policy: ")
        self.processorGrid[self.proN].Add(policy, pos=(0, 1))

        policy_list = ['RMS', 'EDF']
        policy_combo = wx.ComboBox(self.spec_proPanel[self.proN], -1, size=(70, -1), value=" ", choices=policy_list, style=wx.CB_DROPDOWN)
        self.processorGrid[self.proN].Add(policy_combo, pos=(1, 1))

        preempt = wx.StaticText(self.spec_proPanel[self.proN], label="preemptible?: ")
        self.processorGrid[self.proN].Add(preempt, pos=(0, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(self.spec_proPanel[self.proN], -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        self.processorGrid[self.proN].Add(preemptcombo, pos=(1, 2))

        pro_aButton = wx.Button(self.spec_proPanel[self.proN], size=(70, -1), label="Add")
        self.processorGrid[self.proN].Add(pro_aButton, pos=(1, 3))
        self.Bind(wx.EVT_BUTTON, self.on_pro_abutton, pro_aButton)
        self.spec_proPanel[self.proN].SetSizerAndFit(self.processorGrid[self.proN])
        self.proSizer.Add(self.spec_proPanel[self.proN])
        self.proPanel.SetSizerAndFit(self.proSizer)
        self.specSizer.Add(self.proPanel)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def add_spec_propanel(self):
        self.proN += 1
        self.spec_proPanel.append(wx.Panel(self.proPanel, size=(800, 100)))
        self.processorGrid.append(wx.GridBagSizer(hgap=5, vgap=2))
        pname = wx.StaticText(self.spec_proPanel[self.proN], label="name: ")
        self.processorGrid[self.proN].Add(pname, pos=(0, 0))

        edit_pname = wx.TextCtrl(self.spec_proPanel[self.proN], size=(70, -1))
        self.processorGrid[self.proN].Add(edit_pname, pos=(1, 0))

        policy = wx.StaticText(self.spec_proPanel[self.proN], label="policy: ")
        self.processorGrid[self.proN].Add(policy, pos=(0, 1))

        policylist = ['RMS', 'EDF']
        policycombo = wx.ComboBox(self.spec_proPanel[self.proN], -1, size=(70, -1), value=" ", choices=policylist, style=wx.CB_DROPDOWN)
        self.processorGrid[self.proN].Add(policycombo, pos=(1, 1))

        preempt = wx.StaticText(self.spec_proPanel[self.proN], label="preemptible?: ")
        self.processorGrid[self.proN].Add(preempt, pos=(0, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(self.spec_proPanel[self.proN], -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        self.processorGrid[self.proN].Add(preemptcombo, pos=(1, 2))

        pro_dButton = (wx.Button(self.spec_proPanel[self.proN], size=(70, -1), label="Delete"))
        pro_aButton = wx.Button(self.spec_proPanel[self.proN], size=(70, -1), label="Add")
        self.processorGrid[self.proN].Add(pro_dButton, pos=(1, 3))
        self.processorGrid[self.proN].Add(pro_aButton, pos=(1, 4))
        self.Bind(wx.EVT_BUTTON, lambda evt, mark=self.proN: self.on_pro_dbutton(evt, mark), pro_dButton)
        self.Bind(wx.EVT_BUTTON, self.on_pro_abutton, pro_aButton)
        self.spec_proPanel[self.proN].SetSizerAndFit(self.processorGrid[self.proN])
        self.proSizer.Add(self.spec_proPanel[self.proN])
        self.proPanel.SetSizerAndFit(self.proSizer)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def init_buspanel(self):
        self.busPanel = wx.Panel(self.specPanel, size=(800, 100))
        self.busSizer = wx.BoxSizer(wx.VERTICAL)
        bus = wx.StaticText(self.busPanel, label="Bus:")
        self.busSizer.Add(bus)
        self.busGrid = wx.GridBagSizer(hgap=2, vgap=2)
        bcet = wx.StaticText(self.busPanel, label="bcet: ")
        self.busGrid.Add(bcet, pos=(0, 0))
        wcet = wx.StaticText(self.busPanel, label="wcet: ")
        self.busGrid.Add(wcet, pos=(0, 1))
        edit_bcet = wx.TextCtrl(self.busPanel, size=(70, -1))
        self.busGrid.Add(edit_bcet, pos=(1, 0))
        edit_wcet = wx.TextCtrl(self.busPanel, size=(70, -1))
        self.busGrid.Add(edit_wcet, pos=(1, 1))
        self.busSizer.Add(self.busGrid)
        self.busPanel.SetSizerAndFit(self.busSizer)
        self.specSizer.Add(self.busPanel)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def init_taskpanel(self):
        self.taskPanel = wx.Panel(self.specPanel, size=(800, 100))
        # self.taskpanel.SetBackgroundColour('#00ff00')
        self.taskSizer = wx.BoxSizer(wx.VERTICAL)
        task = wx.StaticText(self.taskPanel, label="Task: ")
        self.taskSizer.Add(task)

    def init_spec_taskpanel(self):
        self.spec_taskPanel.append(wx.Panel(self.taskPanel, size=(800, 100)))
        # self.spec_propanel[self.pron].SetBackgroundColour('#00ffff')
        self.taskGrid.append(wx.GridBagSizer(hgap=9, vgap=2))
        tname = wx.StaticText(self.spec_taskPanel[self.taskN], label="task name:")
        self.taskGrid[self.taskN].Add(tname, pos=(0, 0))

        edit_tname = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_tname, pos=(1, 0))

        offset = wx.StaticText(self.spec_taskPanel[self.taskN], label="offset: ")
        self.taskGrid[self.taskN].Add(offset, pos=(0, 1))

        edit_offset = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_offset, pos=(1, 1))

        bcet = wx.StaticText(self.spec_taskPanel[self.taskN], label="bcet: ")
        self.taskGrid[self.taskN].Add(bcet, pos=(0, 2))

        edit_bcet = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_bcet, pos=(1, 2))

        wcet = wx.StaticText(self.spec_taskPanel[self.taskN], label="wcet: ")
        self.taskGrid[self.taskN].Add(wcet, pos=(0, 3))

        edit_wcet = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_wcet, pos=(1, 3))

        deadline = wx.StaticText(self.spec_taskPanel[self.taskN], label="deadline: ")
        self.taskGrid[self.taskN].Add(deadline, pos=(0, 4))

        edit_deadline = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_deadline, pos=(1, 4))

        period = wx.StaticText(self.spec_taskPanel[self.taskN], label="period: ")
        self.taskGrid[self.taskN].Add(period, pos=(0, 5))

        edit_period = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_period, pos=(1, 5))

        processor = wx.StaticText(self.spec_taskPanel[self.taskN], label="processor: ")
        self.taskGrid[self.taskN].Add(processor, pos=(0, 6))

        edit_processor = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_processor, pos=(1, 6))

        predecessor = wx.StaticText(self.spec_taskPanel[self.taskN], label="predeccesor: ")
        self.taskGrid[self.taskN].Add(predecessor, pos=(0, 7))

        edit_pre = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_pre, pos=(1, 7))

        t_aButton = wx.Button(self.spec_taskPanel[self.proN], size=(70, -1), label="Add")
        self.taskGrid[self.taskN].Add(t_aButton, pos=(1, 8))
        self.Bind(wx.EVT_BUTTON, self.on_t_abutton, t_aButton)

        self.spec_taskPanel[self.taskN].SetSizerAndFit(self.taskGrid[self.taskN])
        self.taskSizer.Add(self.spec_taskPanel[self.taskN])
        self.taskPanel.SetSizerAndFit(self.taskSizer)
        self.specSizer.Add(self.taskPanel)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def add_spec_taskpanel(self):
        self.taskN += 1
        self.spec_taskPanel.append(wx.Panel(self.taskPanel, size=(800, 100)))
        # self.spec_taskpanel[self.taskn].SetBackgroundColour('#00ffff')
        self.taskGrid.append(wx.GridBagSizer(hgap=10, vgap=2))
        tname = wx.StaticText(self.spec_taskPanel[self.taskN], label="task name:")
        self.taskGrid[self.taskN].Add(tname, pos=(0, 0))

        edit_tname = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_tname, pos=(1, 0))

        offset = wx.StaticText(self.spec_taskPanel[self.taskN], label="offset: ")
        self.taskGrid[self.taskN].Add(offset, pos=(0, 1))

        edit_offset = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_offset, pos=(1, 1))

        bcet = wx.StaticText(self.spec_taskPanel[self.taskN], label="bcet: ")
        self.taskGrid[self.taskN].Add(bcet, pos=(0, 2))

        edit_bcet = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_bcet, pos=(1, 2))

        wcet = wx.StaticText(self.spec_taskPanel[self.taskN], label="wcet: ")
        self.taskGrid[self.taskN].Add(wcet, pos=(0, 3))

        edit_wcet = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_wcet, pos=(1, 3))

        deadline = wx.StaticText(self.spec_taskPanel[self.taskN], label="deadline: ")
        self.taskGrid[self.taskN].Add(deadline, pos=(0, 4))

        edit_deadline = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_deadline, pos=(1, 4))

        period = wx.StaticText(self.spec_taskPanel[self.taskN], label="period: ")
        self.taskGrid[self.taskN].Add(period, pos=(0, 5))

        edit_period = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_period, pos=(1, 5))

        processor = wx.StaticText(self.spec_taskPanel[self.taskN], label="processor: ")
        self.taskGrid[self.taskN].Add(processor, pos=(0, 6))

        edit_processor = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_processor, pos=(1, 6))

        predecessor = wx.StaticText(self.spec_taskPanel[self.taskN], label="predeccesor: ")
        self.taskGrid[self.taskN].Add(predecessor, pos=(0, 7))

        edit_pre = wx.TextCtrl(self.spec_taskPanel[self.taskN], size=(70, -1))
        self.taskGrid[self.taskN].Add(edit_pre, pos=(1, 7))

        t_dButton = wx.Button(self.spec_taskPanel[self.taskN], size=(70, -1), label="Delete")
        self.taskGrid[self.taskN].Add(t_dButton, pos=(1, 8))
        self.Bind(wx.EVT_BUTTON, lambda evt, mark=self.taskN: self.on_t_dbutton(evt, mark), t_dButton)

        t_aButton = wx.Button(self.spec_taskPanel[self.taskN], size=(70, -1), label="Add")
        self.taskGrid[self.taskN].Add(t_aButton, pos=(1, 9))
        self.Bind(wx.EVT_BUTTON, self.on_t_abutton, t_aButton)

        self.spec_taskPanel[self.taskN].SetSizerAndFit(self.taskGrid[self.taskN])
        self.taskSizer.Add(self.spec_taskPanel[self.taskN])
        self.taskPanel.SetSizerAndFit(self.taskSizer)
        self.specPanel.SetSizerAndFit(self.specSizer)

    def init_resultpanel(self):
        self.resultPanel = wx.Panel(self, size=(900, 500))
        # result = wx.StaticText(self.resultpanel, label="Result:")
        self.resultPanel.SetBackgroundColour('#00ffff')

    def on_quit(self, e):
        self.Close()

    def on_pro_dbutton(self, e, mark):
        self.proSizer.Remove(mark+1)
        self.spec_proPanel.pop()
        self.processorGrid.pop()
        self.proN -= 1
        # if self.pron == 0:
        #    self.spec_propanel[0].SetSizerAndFit(self.processorgrid[0])
        self.proPanel.SetSizerAndFit(self.proSizer)
        self.specPanel.SetSizerAndFit(self.specSizer)
        self.mainSizer.Layout()

    def on_pro_abutton(self, e):
        self.add_spec_propanel()
        self.mainSizer.Layout()

    def on_t_dbutton(self, e, mark):
        self.taskSizer.Remove(mark+1)
        self.spec_taskPanel.pop()
        self.taskGrid.pop()
        self.taskN -= 1
        # if self.taskn == 0:
        #    self.spec_taskpanel[0].SetSizerAndFit(self.taskgrid[0])
        self.taskPanel.SetSizerAndFit(self.taskSizer)
        self.specPanel.SetSizerAndFit(self.specSizer)
        self.mainSizer.Layout()

    def on_t_abutton(self, e):
        self.add_spec_taskpanel()
        self.mainSizer.Layout()

    def on_verify(self, e):
        print 1


def main():
    app = wx.App()
    frame = mainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()