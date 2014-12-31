# coding:utf-8
import wx


class mainFrame(wx.Frame):
    # only one menu bar in the mainframe,includes file menu and about menu
    menubar = None
    fileMenu = None
    aboutmenu = None
    # the system specification area, includes processor panel, and so on
    specpanel = None
    specSizer = None
    # the processor panel includes several processor, each in a spec_propanel
    propanel = None
    proSizer = None
    spec_propanel = []
    processorgrid = []
    # pro_dButton = []
    pron = 0
    # the result area
    resulpanel = None

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(900, 600))
        self.init_filemenu()
        self.init_aboutmenu()
        self.init_menubar()
        self.init_specpanel()
        self.init_propanel()
        self.init_spec_propanel()
        self.add_propanel()
        self.init_resultpanel()

    def init_menubar(self):
        self.menubar = wx.MenuBar()
        self.menubar.Append(self.fileMenu, '&File')
        self.menubar.Append(self.aboutmenu, '&About')
        self.SetMenuBar(self.menubar)

    def init_filemenu(self):
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(wx.ID_NEW, '&New', 'Start to describe a new system')
        self.fileMenu.Append(wx.ID_OPEN, '&Open', 'Open a exist system specification')
        self.fileMenu.Append(wx.ID_SAVE, '&Save', 'Save system specification')
        self.fileMenu.AppendSeparator()
        fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Tool')
        self.Bind(wx.EVT_MENU, self.on_quit, fitem)

    def init_aboutmenu(self):
        self.aboutmenu = wx.Menu()
        self.aboutmenu.Append(wx.ID_ABOUT, '&About', 'About this tool')

    def init_specpanel(self):
        self.specpanel = wx.Panel(self, size=(900, 600))
        self.specSizer = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(self.specpanel, label="System Specification")
        self.specSizer.Add(st)
        self.specpanel.SetSizerAndFit(self.specSizer)

    def add_propanel(self):
        self.specSizer.Add(self.propanel)
        self.specpanel.SetSizerAndFit(self.specSizer)

    def init_propanel(self):
        self.propanel = wx.Panel(self.specpanel, size=(500, 600))
        self.propanel.SetBackgroundColour('#00ff00')
        self.proSizer = wx.BoxSizer(wx.VERTICAL)
        processor = wx.StaticText(self.propanel, label="Processors: ")
        self.proSizer.Add(processor)

    def init_spec_propanel(self):
        self.spec_propanel.append(wx.Panel(self.propanel, size=(500, 100)))
        self.spec_propanel[self.pron].SetBackgroundColour('#00ffff')
        self.processorgrid.append(wx.GridBagSizer(hgap=4, vgap=2))
        pname = wx.StaticText(self.spec_propanel[self.pron], label="name: ")
        self.processorgrid[self.pron].Add(pname, pos=(0, 0))

        edit_pname = wx.TextCtrl(self.spec_propanel[self.pron], size=(70, -1))
        self.processorgrid[self.pron].Add(edit_pname, pos=(1, 0))

        policy = wx.StaticText(self.spec_propanel[self.pron], label="policy: ")
        self.processorgrid[self.pron].Add(policy, pos=(0, 1))

        policylist = ['RMS', 'EDF']
        policycombo = wx.ComboBox(self.spec_propanel[self.pron], -1, size=(70, -1), value=" ", choices=policylist, style=wx.CB_DROPDOWN)
        self.processorgrid[self.pron].Add(policycombo, pos=(1, 1))

        preempt = wx.StaticText(self.spec_propanel[self.pron], label="preemptible?: ")
        self.processorgrid[self.pron].Add(preempt, pos=(0, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(self.spec_propanel[self.pron], -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        self.processorgrid[self.pron].Add(preemptcombo, pos=(1, 2))

        # pro_dButton = wx.Button(self.spec_propanel[self.taskn], size=(70, -1), label="Delete")
        pro_aButton = wx.Button(self.spec_propanel[self.pron], size=(70, -1), label="Add")
        # processorgrid.Add(pro_dButton, pos=(1, 3))
        self.processorgrid[self.pron].Add(pro_aButton, pos=(1, 3))
        # self.Bind(wx.EVT_BUTTON, self.on_pro_dbutton, pro_dButton)
        self.Bind(wx.EVT_BUTTON, self.on_pro_abutton, pro_aButton)
        self.spec_propanel[self.pron].SetSizerAndFit(self.processorgrid[self.pron])
        self.proSizer.Add(self.spec_propanel[self.pron])
        self.propanel.SetSizerAndFit(self.proSizer)

    def add_spec_propanel(self):
        self.pron += 1
        self.spec_propanel.append(wx.Panel(self.propanel, size=(500, 100)))
        self.processorgrid.append(wx.GridBagSizer(hgap=5, vgap=2))
        pname = wx.StaticText(self.spec_propanel[self.pron], label="name: ")
        self.processorgrid[self.pron].Add(pname, pos=(0, 0))

        edit_pname = wx.TextCtrl(self.spec_propanel[self.pron], size=(70, -1))
        self.processorgrid[self.pron].Add(edit_pname, pos=(1, 0))

        policy = wx.StaticText(self.spec_propanel[self.pron], label="policy: ")
        self.processorgrid[self.pron].Add(policy, pos=(0, 1))

        policylist = ['RMS', 'EDF']
        policycombo = wx.ComboBox(self.spec_propanel[self.pron], -1, size=(70, -1), value=" ", choices=policylist, style=wx.CB_DROPDOWN)
        self.processorgrid[self.pron].Add(policycombo, pos=(1, 1))

        preempt = wx.StaticText(self.spec_propanel[self.pron], label="preemptible?: ")
        self.processorgrid[self.pron].Add(preempt, pos=(0, 2))

        preemptlist = ['true', 'false']
        preemptcombo = wx.ComboBox(self.spec_propanel[self.pron], -1, size=(70, -1), value=" ", choices=preemptlist, style=wx.CB_DROPDOWN)
        self.processorgrid[self.pron].Add(preemptcombo, pos=(1, 2))

        # self.pro_dButton.append(wx.Button(self.spec_propanel[self.pron], size=(70, -1), label="Delete"))
        pro_dButton = (wx.Button(self.spec_propanel[self.pron], size=(70, -1), label="Delete"))
        pro_aButton = wx.Button(self.spec_propanel[self.pron], size=(70, -1), label="Add")
        # self.processorgrid[self.pron].Add(self.pro_dButton[self.pron-1], pos=(1, 3))
        self.processorgrid[self.pron].Add(pro_dButton, pos=(1, 3))
        self.processorgrid[self.pron].Add(pro_aButton, pos=(1, 4))
        # self.Bind(wx.EVT_BUTTON, lambda evt, mark=self.pron: self.on_pro_dbutton(evt, mark), self.pro_dButton[self.pron-1])
        self.Bind(wx.EVT_BUTTON, lambda evt, mark=self.pron: self.on_pro_dbutton(evt, mark), pro_dButton)
        self.Bind(wx.EVT_BUTTON, self.on_pro_abutton, pro_aButton)
        self.spec_propanel[self.pron].SetSizerAndFit(self.processorgrid[self.pron])
        self.proSizer.Add(self.spec_propanel[self.pron])
        self.propanel.SetSizerAndFit(self.proSizer)

    def init_resultpanel(self):
        self.resulpanel = wx.Panel(self)

    def on_quit(self, e):
        self.Close()

    def on_pro_dbutton(self, e, mark):
        self.proSizer.Remove(mark+1)
        self.spec_propanel.pop()
        self.processorgrid.pop()
        self.pron -= 1
        if self.pron == 0:
            self.spec_propanel[0].SetSizerAndFit(self.processorgrid[0])
        self.propanel.SetSizerAndFit(self.proSizer)
        self.specpanel.SetSizerAndFit(self.specSizer)

    def on_pro_abutton(self, e):
        self.add_spec_propanel()
        self.propanel.SetSizerAndFit(self.proSizer)
        self.specpanel.SetSizerAndFit(self.specSizer)


def main():
    app = wx.App()
    frame = mainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()