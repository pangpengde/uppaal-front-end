# coding:utf-8
import wx


class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(600, 600))
        self.init_toolbar()
        self.init_panel()

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

    def init_panel(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        specSizer = wx.BoxSizer(wx.VERTICAL)
        # specification = wx.Panel(self, -1)
        # wx.TextCtrl(specification, pos=(3, 3), size=(775, 250))

        # Task
        taskGrid = wx.GridBagSizer(hgap=7, vgap=3)

        task = wx.StaticText(self, label="Task: ", pos=(0, 10))
        taskGrid.Add(task, pos=(0, 0))

        tname = wx.StaticText(self, label="task name: ", pos=(10, 10))
        taskGrid.Add(tname, pos=(1, 0))

        edit_tname = wx.TextCtrl(self, pos=(10, 60), size=(70, -1))
        taskGrid.Add(edit_tname, pos=(2, 0))

        period = wx.StaticText(self, label="period: ", pos=(40, 10))
        taskGrid.Add(period, pos=(1, 1))

        editperiod = wx.TextCtrl(self, pos=(40, 60), size=(70, -1))
        taskGrid.Add(editperiod, pos=(2, 1))

        offset = wx.StaticText(self, label="offset: ", pos=(70, 10))
        taskGrid.Add(offset, pos=(1, 2))

        editoffset= wx.TextCtrl(self, pos=(70, 60), size=(70, -1))
        taskGrid.Add(editoffset, pos=(2, 2))

        bect = wx.StaticText(self, label="bect: ", pos=(100, 10))
        taskGrid.Add(bect, pos=(1, 3))

        editbect = wx.TextCtrl(self, pos=(100, 60), size=(70, -1))
        taskGrid.Add(editbect, pos=(2, 3))

        wect = wx.StaticText(self, label="wect: ", pos=(130, 10))
        taskGrid.Add(wect, pos=(1, 4))

        editwect = wx.TextCtrl(self, pos=(130, 60), size=(70, -1))
        taskGrid.Add(editwect, pos=(2, 4))

        minusButton = wx.Button(self, label="-")
        taskGrid.Add(minusButton, pos=(2, 5))
        plusButton = wx.Button(self, label="+")
        taskGrid.Add(plusButton, pos=(2, 6))

        # Platform
        platformGrid = wx.GridBagSizer(hgap=5, vgap=3)

        platform = wx.StaticText(self, label="Platform: ", pos=(0, 10))
        platformGrid.Add(platform, pos=(0, 0))

        pname = wx.StaticText(self, label="pf name: ", pos=(10, 10))
        platformGrid.Add(pname, pos=(1, 0))

        edit_pname = wx.TextCtrl(self, pos=(10, 60), size=(70, -1))
        platformGrid.Add(edit_pname, pos=(2, 0))

        strategy = wx.StaticText(self, label="strategy: ", pos=(40, 10))
        platformGrid.Add(strategy, pos=(1, 1))

        editstrategy = wx.TextCtrl(self, pos=(40, 60), size=(70, -1))
        platformGrid.Add(editstrategy, pos=(2, 1))

        speed = wx.StaticText(self, label="speed(bus): ", pos=(70, 10))
        platformGrid.Add(speed, pos=(1, 2))

        editspeed= wx.TextCtrl(self, pos=(70, 60), size=(70, -1))
        platformGrid.Add(editspeed, pos=(2, 2))

        pButton1 = wx.Button(self, label="-")
        pButton2 = wx.Button(self, label="+")
        platformGrid.Add(pButton1, pos=(2, 3))
        platformGrid.Add(pButton2, pos=(2, 4))

        # Mapping
        mapGrid = wx.GridBagSizer(hgap=4, vgap=3)

        mapping = wx.StaticText(self, label="Mapping: ", pos=(10, 60))
        mapGrid.Add(mapping, pos=(0, 0))

        tsk_name = wx.StaticText(self, label="task name: ", pos=(40, 70))
        mapGrid.Add(tsk_name, pos=(1, 0))

        edit_tskname = wx.TextCtrl(self, pos=(10, 60), size=(70, -1))
        mapGrid.Add(edit_tskname, pos=(2, 0))

        pt_name = wx.StaticText(self, label="pf name: ", pos=(40, 70))
        mapGrid.Add(pt_name, pos=(1, 1))

        editpfname = wx.TextCtrl(self, pos=(40, 60), size=(70, -1))
        mapGrid.Add(editpfname, pos=(2, 1))

        mButton1 = wx.Button(self, label="-")
        mButton2 = wx.Button(self, label="+")
        mapGrid.Add(mButton1, pos=(2, 2))
        mapGrid.Add(mButton2, pos=(2, 3))

        # Denpendency
        depGrid = wx.GridBagSizer(hgap=5, vgap=3)
        dep = wx.StaticText(self, label="Dependency: ", pos=(0, 10))
        depGrid.Add(dep, pos=(0, 0))

        t_name = wx.StaticText(self, label="task name: ", pos=(10, 10))
        depGrid.Add(t_name, pos=(1, 0))

        edit_dtname = wx.TextCtrl(self, pos=(10, 60), size=(70, -1))
        depGrid.Add(edit_dtname, pos=(2, 0))

        predecessor = wx.StaticText(self, label="predecessor: ", pos=(40, 10))
        depGrid.Add(predecessor, pos=(1, 1))

        editpredecessor = wx.TextCtrl(self, pos=(40, 60), size=(70, -1))
        depGrid.Add(editpredecessor, pos=(2, 1))

        data = wx.StaticText(self, label="data: ", pos=(70, 10))
        depGrid.Add(data, pos=(1, 2))

        editdata= wx.TextCtrl(self, pos=(70, 60), size=(70, -1))
        depGrid.Add(editdata, pos=(2, 2))

        dButton1 = wx.Button(self, label="-")
        dButton2 = wx.Button(self, label="+")
        depGrid.Add(dButton1, pos=(2, 3))
        depGrid.Add(dButton2, pos=(2, 4))

        verifyButton = wx.Button(self, label='Verify!')

        specSizer.Add(taskGrid, 0, wx.LEFT)
        specSizer.Add(platformGrid, 0, wx.LEFT)
        specSizer.Add(mapGrid, 0, wx.LEFT)
        specSizer.Add(depGrid, 0, wx.LEFT)
        specSizer.Add(verifyButton, 0, wx.LEFT)

        resultSizer = wx.BoxSizer(wx.VERTICAL)
        result = wx.Panel(self, -1)
        wx.TextCtrl(result, pos=(3, -1), size = (580, 250))
        res = wx.StaticText(self, label='Verification Result:')
        resultSizer.Add(res, 0, wx.LEFT)
        resultSizer.Add(result, 0, wx.CENTER)

        mainSizer.Add(specSizer, 0, wx.CENTER)
        mainSizer.Add(resultSizer, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)
        #self.add_task()

    """def add_task(self):
        sp = wx.Panel(self, -1)
        self.mainSizer.Add(sp, 0, wx.CENTER)"""


def main():
    app = wx.App()
    frame = mainFrame(None, 'Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()