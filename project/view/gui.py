# coding:utf-8
import wx


class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.init_toolbar()
        self.init_specpanel()
        # self.init_resultpenal()

    def init_toolbar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New', 'Start to describe a new system')
        fileMenu.Append(wx.ID_OPEN, '&Open', 'Open a exist system specification')
        fileMenu.Append(wx.ID_SAVE, '&Save', 'Save system specification')
        fileMenu.AppendSeparator()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Tool')
        menubar.Append(fileMenu, '&File')
        aboutmenu = wx.Menu()
        aboutmenu.Append(wx.ID_ABOUT, '&About', 'About this tool')
        menubar.Append(aboutmenu, '&About')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit, fitem)

    def on_quit(self, e):
        self.Close()

    def init_specpanel(self):
        specpanel = wx.Panel(self)
        specSizer = wx.BoxSizer(wx.VERTICAL)

        # Task
        taskGrid = wx.GridBagSizer(hgap=10, vgap=3)

        task = wx.StaticText(specpanel, label="Task: ")
        taskGrid.Add(task, pos=(0, 0))

        tname = wx.StaticText(specpanel, label="task name: ")
        taskGrid.Add(tname, pos=(1, 0))

        edit_tname = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(edit_tname, pos=(2, 0))

        offset = wx.StaticText(specpanel, label="offset: ")
        taskGrid.Add(offset, pos=(1, 1))

        editoffset= wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(editoffset, pos=(2, 1))

        task_bcet = wx.StaticText(specpanel, label="bect: ")
        taskGrid.Add(task_bcet, pos=(1, 2))

        edit_task_bcet = wx.TextCtrl(specpanel,  size=(70, -1))
        taskGrid.Add(edit_task_bcet, pos=(2, 2))

        task_wcet = wx.StaticText(specpanel, label="wect: ")
        taskGrid.Add(task_wcet, pos=(1, 3))

        edit_task_wcet = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(edit_task_wcet, pos=(2, 3))

        deadline = wx.StaticText(specpanel, label="deadline: ")
        taskGrid.Add(deadline, pos=(1, 4))

        edit_deadline = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(edit_deadline, pos=(2, 4))

        period = wx.StaticText(specpanel, label="period: ")
        taskGrid.Add(period, pos=(1, 5))

        editperiod = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(editperiod, pos=(2, 5))

        processor = wx.StaticText(specpanel, label="processor: ")
        taskGrid.Add(processor, pos=(1, 6))

        editprocessor = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(editprocessor, pos=(2, 6))

        predecessor = wx.StaticText(specpanel, label="predecessor: ")
        taskGrid.Add(predecessor, pos=(1, 7))

        editpredecessor = wx.TextCtrl(specpanel, size=(70, -1))
        taskGrid.Add(editpredecessor, pos=(2, 7))

        task_dButton = wx.Button(specpanel,  size=(70, -1), label="Delete")
        taskGrid.Add(task_dButton, pos=(2, 8))
        task_aButton = wx.Button(specpanel,  size=(70, -1), label="Add")
        taskGrid.Add(task_aButton, pos=(2, 9))

        # Processor
        processorGrid = wx.GridBagSizer(hgap=5, vgap=3)

        platform = wx.StaticText(specpanel, label="Processors: ")
        processorGrid.Add(platform, pos=(0, 0))

        pname = wx.StaticText(specpanel, label="name: ")
        processorGrid.Add(pname, pos=(1, 0))

        edit_pname = wx.TextCtrl(specpanel, size=(70, -1))
        processorGrid.Add(edit_pname, pos=(2, 0))

        policy = wx.StaticText(specpanel, label="policy: ")
        processorGrid.Add(policy, pos=(1, 1))

        policylist = ['RMS', 'EDF']
        policycombo = wx.ComboBox(specpanel, -1, size=(70, -1), value=" ", choices=policylist, style=wx.CB_DROPDOWN)
        processorGrid.Add(policycombo, pos=(2, 1))

        preempt = wx.StaticText(specpanel, label="preemptible?: ")
        processorGrid.Add(preempt, pos=(1, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(specpanel, -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        processorGrid.Add(preemptcombo, pos=(2, 2))

        pro_dButton = wx.Button(specpanel, size=(70, -1), label="Delete")
        pro_aButton = wx.Button(specpanel, size=(70, -1), label="Add")
        processorGrid.Add(pro_dButton, pos=(2, 3))
        processorGrid.Add(pro_aButton, pos=(2, 4))

        # Bus
        busgrid = wx.GridBagSizer(hgap=4, vgap=3)
        bus = wx.StaticText(specpanel, label="Bus: ")
        busgrid.Add(bus, pos=(0, 0))

        bus_bcet = wx.StaticText(specpanel, label="bcet")
        busgrid.Add(bus_bcet, pos=(1, 0))

        edit_bus_bcet = wx.TextCtrl(specpanel, size=(70, -1))
        busgrid.Add(edit_bus_bcet, pos=(2, 0))

        bus_wcet = wx.StaticText(specpanel, label="wcet: ")
        busgrid.Add(bus_wcet, pos=(1, 1))

        edit_bus_wcet = wx.TextCtrl(specpanel, size=(70, -1))
        busgrid.Add(edit_bus_wcet, pos=(2, 1))

        bus_dButton = wx.Button(specpanel,  size=(70, -1), label="Delete")
        bus_aButton = wx.Button(specpanel, size=(70, -1),  label="Add")
        busgrid.Add(bus_dButton, pos=(2, 2))
        busgrid.Add(bus_aButton, pos=(2, 3))

        modelgenbutton = wx.Button(specpanel, label='Model Generate!')

        specSizer.Add(processorGrid, 0, wx.LEFT)
        specSizer.Add(busgrid, 0, wx.LEFT)
        specSizer.Add(taskGrid, 0, wx.LEFT)
        specSizer.Add(modelgenbutton, 0, wx.LEFT)
        specpanel.SetSizerAndFit(specSizer)

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