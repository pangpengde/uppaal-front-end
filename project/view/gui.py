# coding:utf-8
import wx

class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(800, 600))
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
        specification = wx.Panel(self, -1)
        taskGrid = wx.GridBagSizer(hgap=7, vgap=2)

        name = wx.StaticText(self, label="task name: ", pos=(10, 10))
        taskGrid.Add(name, pos=(0, 0))

        editname = wx.TextCtrl(self, pos=(10, 60), size=(70, -1))
        taskGrid.Add(editname, pos=(1, 0))

        period = wx.StaticText(self, label="period: ", pos=(40, 10))
        taskGrid.Add(period, pos=(0, 1))

        editperiod = wx.TextCtrl(self, pos=(40, 60), size=(70, -1))
        taskGrid.Add(editperiod, pos=(1, 1))

        offset = wx.StaticText(self, label="offset: ", pos=(70, 10))
        taskGrid.Add(offset, pos=(0, 2))

        editoffset= wx.TextCtrl(self, pos=(70, 60), size=(70, -1))
        taskGrid.Add(editoffset, pos=(1, 2))

        bect = wx.StaticText(self, label="bect: ", pos=(100, 10))
        taskGrid.Add(bect, pos=(0, 3))

        editbect = wx.TextCtrl(self, pos=(100, 60), size=(70, -1))
        taskGrid.Add(editbect, pos=(1, 3))

        wect = wx.StaticText(self, label="wect: ", pos=(130, 10))
        taskGrid.Add(wect, pos=(0, 4))

        editwect = wx.TextCtrl(self, pos=(130, 60), size=(70, -1))
        taskGrid.Add(editwect, pos=(1, 4))

        minusButton = wx.Button(self, label="-", pos=(160, 60))
        taskGrid.Add(minusButton, pos=(1, 5))
        plusButton = wx.Button(self, label="+", pos=(190, 60))
        taskGrid.Add(plusButton, pos=(1, 6))

        #wx.TextCtrl(specification, pos=(3, 3), size=(775, 250))

        specSizer.Add(taskGrid, 0, wx.LEFT)

        result = wx.Panel(self, -1)
        wx.TextCtrl(result, pos=(3, -1), size = (775, 250))

        mainSizer.Add(specSizer, 0, wx.CENTER)
        mainSizer.Add(result, 0, wx.CENTER)
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