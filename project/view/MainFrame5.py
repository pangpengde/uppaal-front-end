# coding:utf-8
import wx
from model.Processor import Processor
from model.Bus import Bus
from model.Task import Task
from model.Dep import Dep
from model.Template import Template
from model.UserInput import UserInput
from controller.TemplateAnalyse import TemplateAnalyse
from controller.ModelGenerate import ModelGenerate

class MainFrame(wx.Frame):
    mainSizer = None
    mainPanel = None
    # only one menu bar in the mainframe,includes file menu and about menu
    menuBar = None
    fileMenu = None
    aboutMenu = None
    # the system specification area
    specSizer = None
    # the processor panel includes several processors
    proSizer = None
    proAddButton = None
    processorPanels = {}
    # the bus panel
    busSizer = None
    busPanel = None
    # the task panel includes several tasks
    taskSizer = None
    taskAddButton = None
    taskPanels = {}
    # the result area
    resultSizer = None
    resultPanel = None
    #temp xml panel
    xmlPanel = None

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
        self.init_bus_panel()
        self.init_task_sizer()
        self.init_spec_task_panel()

        self.verify_button = wx.Button(self.mainPanel, size=(70, -1), label="Verify!!")
        self.Bind(wx.EVT_BUTTON, self.on_verify, self.verify_button)
        self.mainSizer.Add(self.specSizer)
        self.mainSizer.Add(self.verify_button)
        self.mainSizer.Add(self.resultSizer)
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
        pName = wx.StaticText(self.mainPanel, label="p_id: ", size=(70, -1))
        h_text_sizer.Add(pName)
        policy = wx.StaticText(self.mainPanel, label="policy: ", size=(70, -1))
        h_text_sizer.Add(policy)
        preempt = wx.StaticText(self.mainPanel, label="preemptible?: ", size=(70, -1))
        h_text_sizer.Add(preempt)
        self.proSizer.Add(h_sizer)
        self.proSizer.Add(h_text_sizer)

    def init_spec_propanel(self):
        self.processorPanels[0] = FirstSpecProcessor(self.mainPanel)
        self.proSizer.Add(self.processorPanels[0])
        self.specSizer.Add(self.proSizer)

    def init_bus_panel(self):
        self.busSizer = wx.BoxSizer(wx.VERTICAL)
        bus = wx.StaticText(self.mainPanel, label="Bus:")
        self.busSizer.Add(bus)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bcet = wx.StaticText(self.mainPanel, label="bcet: ", size=(70, -1))
        wcet = wx.StaticText(self.mainPanel, label="wcet: ", size=(70, -1))
        text_sizer.AddMany([bcet, wcet])
        self.busSizer.Add(text_sizer)
        self.busPanel = BusPanel(self.mainPanel)
        self.busSizer.Add(self.busPanel)
        self.specSizer.Add(self.busSizer)

    def init_task_sizer(self):
        self.taskSizer = wx.BoxSizer(wx.VERTICAL)
        task = wx.StaticText(self.mainPanel, label="Task:", size=(70, -1))
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer.Add(task)
        self.taskAddButton = wx.Button(self.mainPanel, size=(70, -1), label="Add")
        self.taskAddButton.Bind(wx.EVT_BUTTON, self.on_task_add_button, self.taskAddButton)
        h_sizer.Add(self.taskAddButton)
        self.taskSizer.Add(h_sizer)
        h_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tname = wx.StaticText(self.mainPanel, label="t_id:", size=(70, -1))
        h_text_sizer.Add(tname)
        offset = wx.StaticText(self.mainPanel, label="offset: ", size=(70, -1))
        h_text_sizer.Add(offset)
        bcet = wx.StaticText(self.mainPanel, label="bcet: ", size=(70, -1))
        h_text_sizer.Add(bcet)
        wcet = wx.StaticText(self.mainPanel, label="wcet: ", size=(70, -1))
        h_text_sizer.Add(wcet)
        deadline = wx.StaticText(self.mainPanel, label="deadline: ", size=(70, -1))
        h_text_sizer.Add(deadline)
        period = wx.StaticText(self.mainPanel, label="period: ", size=(70, -1))
        h_text_sizer.Add(period)
        processor = wx.StaticText(self.mainPanel, label="processor: ", size=(70, -1))
        h_text_sizer.Add(processor)
        predecessor = wx.StaticText(self.mainPanel, label="predeccesor: ", size=(80, -1))
        h_text_sizer.Add(predecessor)
        self.taskSizer.Add(h_text_sizer)

    def init_spec_task_panel(self):
        self.taskPanels[0] = FirstTaskPanel(self.mainPanel)
        self.taskSizer.Add(self.taskPanels[0])
        self.specSizer.Add(self.taskSizer)

    def init_resultpanel(self):
        # self.resultPanel = wx.Panel(self.mainPanel, size=(900, 500))
        self.resultSizer = wx.BoxSizer(wx.VERTICAL)
        # result = wx.StaticText(self.resultpanel, label="Result:")
        # self.resultPanel.SetBackgroundColour('#00ffff')
        # self.resultPanel.SetSizerAndFit(self.resultSizer)

    def on_quit(self, e):
        self.Close()

    def on_pro_del_button(self, e):
        button = e.GetEventObject()
        self.processorPanels[button].Destroy()
        del self.processorPanels[button]
        self.mainSizer.Layout()

    def on_pro_add_button(self, e):
        temp = SpecProcessor(self.mainPanel)
        self.processorPanels[temp.proDelButton] = temp
        temp.proDelButton.Bind(wx.EVT_BUTTON, self.on_pro_del_button, temp.proDelButton)
        self.proSizer.Add(temp)
        self.mainSizer.Layout()

    def on_task_del_button(self, e):
        button = e.GetEventObject()
        self.taskPanels[button].Destroy()
        del self.taskPanels[button]
        self.mainSizer.Layout()

    def on_task_add_button(self, e):
        temp = TaskPanel(self.mainPanel)
        self.taskPanels[temp.taskDelButton] = temp
        temp.taskDelButton.Bind(wx.EVT_BUTTON, self.on_task_del_button, temp.taskDelButton)
        self.taskSizer.Add(temp)
        self.mainSizer.Layout()

    def on_verify(self, e):
        userinput = UserInput()
        for k, v in self.processorPanels.items():
            userinput.processors.append(Processor(int(v.editPname.GetValue()),
                                                  str(v.policyCombo.GetValue()),
                                                  str(v.preemptCombo.GetValue())))
        userinput.bus = Bus(int(self.busPanel.edit_bcet.GetValue()),
                            int(self.busPanel.edit_wcet.GetValue()))
        for k, v in self.taskPanels.items():
            userinput.tasks.append(Task(int(v.editTid.GetValue()),
                                        int(v.editOffset.GetValue()),
                                        int(v.editBcet.GetValue()),
                                        int(v.editWcet.GetValue()),
                                        int(v.editDeadline.GetValue()),
                                        int(v.editPeriod.GetValue()),
                                        userinput.processors[int(v.editProcessor.GetValue())]))
            if len(v.editPre.GetValue()) != 0:
                userinput.deps.append(Dep(userinput.tasks[int(v.editTid.GetValue())],
                                          userinput.tasks[int(v.editPre.GetValue())]))
        ta = TemplateAnalyse()
        ta.user_input = userinput
        ta.init_template()
        mg = ModelGenerate()
        mg.ta = ta
        mg.init_ta()
        mg.genarate()




class FirstSpecProcessor(wx.Panel):
    processorSizer = None
    editPname = None
    policyList = ['RMS', 'EDF']
    policyCombo = None
    preemptList = ['true', 'false']
    preemptCombo = None

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
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

    def __init__(self, parent):
        FirstSpecProcessor.__init__(self, parent)
        self.proDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.processorSizer.Add(self.proDelButton)
        self.SetSizerAndFit(self.processorSizer)


class BusPanel(wx.Panel):
    edit_bcet = None
    edit_wcet = None
    sizer = None

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.edit_bcet = wx.TextCtrl(self, size=(70, -1))
        self.sizer.Add(self.edit_bcet)
        self.edit_wcet = wx.TextCtrl(self, size=(70, -1))
        self.sizer.Add(self.edit_wcet)
        self.SetSizerAndFit(self.sizer)

class FirstTaskPanel(wx.Panel):
    taskSizer = None
    editTid = None
    editOffset = None
    editBcet = None
    editWcet = None
    editDeadline = None
    editPeriod = None
    editProcessor = None
    editPre = None

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.taskSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.editTid = wx.TextCtrl(self, size=(70, -1))
        self.editOffset = wx.TextCtrl(self, size=(70, -1))
        self.editBcet = wx.TextCtrl(self, size=(70, -1))
        self.editWcet = wx.TextCtrl(self, size=(70, -1))
        self.editDeadline = wx.TextCtrl(self, size=(70, -1))
        self.editPeriod = wx.TextCtrl(self, size=(70, -1))
        self.editProcessor = wx.TextCtrl(self, size=(70, -1))
        self.editPre = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.AddMany([self.editTid, self.editOffset, self.editBcet, self.editWcet, self.editDeadline, self.editPeriod, self.editProcessor, self.editPre])
        self.SetSizerAndFit(self.taskSizer)


class TaskPanel(FirstTaskPanel):
    taskDelButton = None

    def __init__(self, parent):
        FirstTaskPanel.__init__(self, parent)
        self.taskDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.taskSizer.Add(self.taskDelButton)
        self.SetSizerAndFit(self.taskSizer)


def main():
    app = wx.App()
    frame = MainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()