# coding:utf-8
import wx


class mainFrame(wx.Frame):
    menubar = None
    fileMenu = None
    specpanel = None
    resulpanel = None

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.init_toolbar()
        self.init_specpanel()
        # self.init_resultpenal()

    def init_toolbar(self):
        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(wx.ID_NEW, '&New', 'Start to describe a new system')
        self.fileMenu.Append(wx.ID_OPEN, '&Open', 'Open a exist system specification')
        self.fileMenu.Append(wx.ID_SAVE, '&Save', 'Save system specification')
        self.fileMenu.AppendSeparator()
        fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Tool')
        self.menubar.Append(self.fileMenu, '&File')
        aboutmenu = wx.Menu()
        aboutmenu.Append(wx.ID_ABOUT, '&About', 'About this tool')
        self.menubar.Append(aboutmenu, '&About')
        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_MENU, self.on_quit, fitem)

    def on_quit(self, e):
        self.Close()

    def on_pro_dbutton(self, e):
        pass

    def on_pro_abutton(self, e):
        pass

    def init_specpanel(self):
        self.specpanel = wx.Panel(self)
        specSizer = wx.BoxSizer(wx.VERTICAL)

        # ID_BUTTON_ADD = wx.NewId()
        # ID_BUTTON_DELETE = wx.NewId()

        # Processor
        processorGrid = wx.GridBagSizer(hgap=5, vgap=3)

        platform = wx.StaticText(self.specpanel, label="Processors: ")
        processorGrid.Add(platform, pos=(0, 0))

        pname = wx.StaticText(self.specpanel, label="name: ")
        processorGrid.Add(pname, pos=(1, 0))

        edit_pname = wx.TextCtrl(self.specpanel, size=(70, -1))
        processorGrid.Add(edit_pname, pos=(2, 0))

        policy = wx.StaticText(self.specpanel, label="policy: ")
        processorGrid.Add(policy, pos=(1, 1))

        policylist = ['RMS', 'EDF']
        policycombo = wx.ComboBox(self.specpanel, -1, size=(70, -1), value=" ", choices=policylist, style=wx.CB_DROPDOWN)
        processorGrid.Add(policycombo, pos=(2, 1))

        preempt = wx.StaticText(self.specpanel, label="preemptible?: ")
        processorGrid.Add(preempt, pos=(1, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(self.specpanel, -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        processorGrid.Add(preemptcombo, pos=(2, 2))

        pro_dButton = wx.Button(self.specpanel,size=(70, -1), label="Delete")
        pro_aButton = wx.Button(self.specpanel, size=(70, -1), label="Add")
        processorGrid.Add(pro_dButton, pos=(2, 3))
        processorGrid.Add(pro_aButton, pos=(2, 4))
        self.Bind(wx.EVT_BUTTON, self.on_pro_dbutton, pro_dButton)
        self.Bind(wx.EVT_BUTTON, self.on_pro_abutton, pro_aButton)

        # Bus
        busgrid = wx.GridBagSizer(hgap=4, vgap=3)
        bus = wx.StaticText(self.specpanel, label="Bus: ")
        busgrid.Add(bus, pos=(0, 0))

        bus_bcet = wx.StaticText(self.specpanel, label="bcet")
        busgrid.Add(bus_bcet, pos=(1, 0))

        edit_bus_bcet = wx.TextCtrl(self.specpanel, size=(70, -1))
        busgrid.Add(edit_bus_bcet, pos=(2, 0))

        bus_wcet = wx.StaticText(self.specpanel, label="wcet: ")
        busgrid.Add(bus_wcet, pos=(1, 1))

        edit_bus_wcet = wx.TextCtrl(self.specpanel, size=(70, -1))
        busgrid.Add(edit_bus_wcet, pos=(2, 1))

        bus_dButton = wx.Button(self.specpanel,  size=(70, -1), label="Delete")
        bus_aButton = wx.Button(self.specpanel, size=(70, -1),  label="Add")
        busgrid.Add(bus_dButton, pos=(2, 2))
        busgrid.Add(bus_aButton, pos=(2, 3))

        # Task
        taskGrid = wx.GridBagSizer(hgap=10, vgap=3)

        task = wx.StaticText(self.specpanel, label="Task: ")
        taskGrid.Add(task, pos=(0, 0))

        tname = wx.StaticText(self.specpanel, label="task name: ")
        taskGrid.Add(tname, pos=(1, 0))

        edit_tname = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(edit_tname, pos=(2, 0))

        offset = wx.StaticText(self.specpanel, label="offset: ")
        taskGrid.Add(offset, pos=(1, 1))

        editoffset= wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(editoffset, pos=(2, 1))

        task_bcet = wx.StaticText(self.specpanel, label="bect: ")
        taskGrid.Add(task_bcet, pos=(1, 2))

        edit_task_bcet = wx.TextCtrl(self.specpanel,  size=(70, -1))
        taskGrid.Add(edit_task_bcet, pos=(2, 2))

        task_wcet = wx.StaticText(self.specpanel, label="wect: ")
        taskGrid.Add(task_wcet, pos=(1, 3))

        edit_task_wcet = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(edit_task_wcet, pos=(2, 3))

        deadline = wx.StaticText(self.specpanel, label="deadline: ")
        taskGrid.Add(deadline, pos=(1, 4))

        edit_deadline = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(edit_deadline, pos=(2, 4))

        period = wx.StaticText(self.specpanel, label="period: ")
        taskGrid.Add(period, pos=(1, 5))

        editperiod = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(editperiod, pos=(2, 5))

        processor = wx.StaticText(self.specpanel, label="processor: ")
        taskGrid.Add(processor, pos=(1, 6))

        editprocessor = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(editprocessor, pos=(2, 6))

        predecessor = wx.StaticText(self.specpanel, label="predecessor: ")
        taskGrid.Add(predecessor, pos=(1, 7))

        editpredecessor = wx.TextCtrl(self.specpanel, size=(70, -1))
        taskGrid.Add(editpredecessor, pos=(2, 7))

        task_dButton = wx.Button(self.specpanel,  size=(70, -1), label="Delete")
        taskGrid.Add(task_dButton, pos=(2, 8))
        task_aButton = wx.Button(self.specpanel,  size=(70, -1), label="Add")
        taskGrid.Add(task_aButton, pos=(2, 9))

        modelgenbutton = wx.Button(self.specpanel, label='Model Generate!')

        specSizer.Add(processorGrid, 0, wx.LEFT)
        specSizer.Add(busgrid, 0, wx.LEFT)
        specSizer.Add(taskGrid, 0, wx.LEFT)
        specSizer.Add(modelgenbutton, 0, wx.LEFT)
        self.specpanel.SetSizerAndFit(specSizer)

        '''mainSizer.Add(specSizer, 0, wx.CENTER)
        mainSizer.Add(resultSizer, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)
        #self.add_task()'''

    '''def init_resultpenal(self):
        resultSizer = wx.BoxSizer(wx.VERTICAL)
        resultpanel = wx.Panel(self, -1)
        wx.TextCtrl(resultpanel, pos=(3, -1), size = (580, 250))
        res = wx.StaticText(self, label='Verification Result:')
        resultSizer.Add(res, 0, wx.LEFT)
        resultSizer.Add(resultpanel, 0, wx.CENTER)
        resultpanel.SetSizerAndFit(resultSizer)'''


def main():
    app = wx.App()
    frame = mainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()