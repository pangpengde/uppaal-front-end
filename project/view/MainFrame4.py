# coding:utf-8
import cmd
import os
import sys
import wx
from model.Processor import Processor
from model.Bus import Bus
from model.Task import Task
from model.Dep import Dep
from model.Template import Template
from model.UserInput import UserInput
from controller.TemplateAnalyse import TemplateAnalyse
from controller.ModelGenerate import ModelGenerate
from controller.ResultAnalyse import ResultAnalyse

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

    xmltext = None
    showinuppaal = None
    systemname = None
    resulttext = None

    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(800, 700))
        # TODO can not auto visiable scrollerbar
        self.mainPanel = wx.ScrolledWindow(self, -1)
        self.mainPanel.SetScrollbars(1, 1, 20, 20)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        # menus
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
        self.init_resultpanel()

        self.verify_button = wx.Button(self.mainPanel, size=(70, -1), label="Verify!!")
        self.Bind(wx.EVT_BUTTON, self.on_verify, self.verify_button)
        self.mainSizer.Add(self.specSizer)
        self.mainSizer.Add(self.verify_button, flag=wx.LEFT|wx.TOP, border=10)
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
        self.specSizer.Add(st, flag=wx.ALL, border=10)

    def init_pro_sizer(self):
        processor = wx.StaticBox(self.mainPanel, label="Processors:")
        self.proSizer = wx.StaticBoxSizer(processor, wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.proAddButton = wx.Button(self.mainPanel, size=(70, -1), label="Add")
        self.proAddButton.Bind(wx.EVT_BUTTON, self.on_pro_add_button, self.proAddButton)
        h_sizer.Add(self.proAddButton, flag=wx.LEFT, border=10)
        h_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pName = wx.StaticText(self.mainPanel, label="p_id: ", size=(70, -1))
        h_text_sizer.Add(pName, flag=wx.LEFT, border=10)
        policy = wx.StaticText(self.mainPanel, label="policy: ", size=(70, -1))
        h_text_sizer.Add(policy, flag=wx.LEFT, border=10)
        preempt = wx.StaticText(self.mainPanel, label="preemptible:", size=(90, -1))
        h_text_sizer.Add(preempt, flag=wx.LEFT, border=10)
        self.proSizer.Add(h_sizer)
        self.proSizer.Add(h_text_sizer)

    def init_spec_propanel(self):
        self.processorPanels[0] = FirstSpecProcessor(self.mainPanel)
        self.proSizer.Add(self.processorPanels[0], flag=wx.TOP, border=10)
        self.specSizer.Add(self.proSizer)

    def init_bus_panel(self):
        bus = wx.StaticBox(self.mainPanel, label="Bus:")
        self.busSizer = wx.StaticBoxSizer(bus, wx.VERTICAL)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bcet = wx.StaticText(self.mainPanel, label="bcet: ", size=(70, -1))
        text_sizer.Add(bcet, flag=wx.LEFT, border=10)
        wcet = wx.StaticText(self.mainPanel, label="wcet: ", size=(70, -1))
        text_sizer.Add(wcet, flag=wx.LEFT, border=10)
        self.busSizer.Add(text_sizer)
        self.busPanel = BusPanel(self.mainPanel)
        self.busSizer.Add(self.busPanel)
        self.specSizer.Add(self.busSizer)

    def init_task_sizer(self):
        task = wx.StaticBox(self.mainPanel, label="Task:", size=(70, -1))
        self.taskSizer = wx.StaticBoxSizer(task, wx.VERTICAL)
        self.taskAddButton = wx.Button(self.mainPanel, size=(70, -1), label="Add")
        self.taskAddButton.Bind(wx.EVT_BUTTON, self.on_task_add_button, self.taskAddButton)
        self.taskSizer.Add(self.taskAddButton, flag=wx.LEFT, border=10)
        h_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tname = wx.StaticText(self.mainPanel, label="t_id:", size=(70, -1))
        h_text_sizer.Add(tname, flag=wx.LEFT, border=10)
        offset = wx.StaticText(self.mainPanel, label="offset: ", size=(70, -1))
        h_text_sizer.Add(offset, flag=wx.LEFT, border=10)
        bcet = wx.StaticText(self.mainPanel, label="bcet: ", size=(70, -1))
        h_text_sizer.Add(bcet, flag=wx.LEFT, border=10)
        wcet = wx.StaticText(self.mainPanel, label="wcet: ", size=(70, -1))
        h_text_sizer.Add(wcet, flag=wx.LEFT, border=10)
        deadline = wx.StaticText(self.mainPanel, label="deadline: ", size=(70, -1))
        h_text_sizer.Add(deadline, flag=wx.LEFT, border=10)
        period = wx.StaticText(self.mainPanel, label="period: ", size=(70, -1))
        h_text_sizer.Add(period, flag=wx.LEFT, border=10)
        processor = wx.StaticText(self.mainPanel, label="processor: ", size=(70, -1))
        h_text_sizer.Add(processor, flag=wx.LEFT, border=10)
        predecessor = wx.StaticText(self.mainPanel, label="predeccesor: ", size=(80, -1))
        h_text_sizer.Add(predecessor, flag=wx.LEFT, border=10)
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
        self.proSizer.Add(temp, flag=wx.TOP, border=10)
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
        self.taskSizer.Add(temp, flag=wx.TOP, border=10)
        self.mainSizer.Layout()

    def on_verify(self, e):
        userinput = UserInput()
        temp = 0
        for a, b in self.processorPanels.items():
            for k, v in self.processorPanels.items():
                if int(v.editPname.GetValue()) == temp:
                    userinput.processors.append(Processor(int(v.editPname.GetValue()),
                                                          str(v.policyCombo.GetValue()),
                                                          str(v.preemptCombo.GetValue())))
                    temp += 1
        userinput.bus = Bus(int(self.busPanel.edit_bcet.GetValue()),
                            int(self.busPanel.edit_wcet.GetValue()))
        temp = 0
        for a, b in self.taskPanels.items():
            for k, v in self.taskPanels.items():
                if int(v.editTid.GetValue()) == temp:
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
                    temp += 1
                    continue
        ta = TemplateAnalyse()
        ta.user_input = userinput
        ta.init_template()
        mg = ModelGenerate()
        mg.ta = ta
        mg.init_ta()
        mg.genarate()
        self.systemname = "model"
        xml = file('../source/%s.xml' % self.systemname, 'r')
        modelxml = xml.read()
        if self.xmltext == None:
            self.xmltext = wx.TextCtrl(self.mainPanel, -1, str(modelxml), size=(700, 100), style=wx.TE_MULTILINE)
            self.mainSizer.Add(self.xmltext, flag=wx.LEFT|wx.TOP, border=10)
        else:
            self.xmltext.SetValue(str(modelxml))
        if self.showinuppaal == None:
            self.showinuppaal = wx.Button(self.mainPanel, size=(100, -1), label="Show in Uppaal")
            self.showinuppaal.Bind(wx.EVT_BUTTON, self.on_showinuppaal, self.showinuppaal)
            self.mainSizer.Add(self.showinuppaal, flag=wx.LEFT|wx.TOP, border=10)

        cmd = '..\\..\\uppaal-4.1.18\\bin-Win32\\verifyta.exe -qst 1 ..\\source\\%s.xml ..\\source\\%s.q '\
              % (self.systemname, self.systemname) + '1>..\\source\\%s.result 2>..\\source\\%s.trace'\
                                                     % (self.systemname, self.systemname)
        os.system(cmd)
        # resultfile = file('../source/%s.result' % self.systemname, 'r')
        # result = resultfile.read()
        ra = ResultAnalyse()
        if self.resulttext == None:
            self.resulttext = wx.TextCtrl(self.mainPanel, -1, str(ra.resultToShow), size=(700, 100), style=wx.TE_MULTILINE)
            self.mainSizer.Add(self.resulttext, flag=wx.LEFT|wx.TOP, border=10)
        else:
            self.resulttext.SetValue(str(ra.resultToShow))

        self.mainSizer.Layout()

    def on_showinuppaal(self, e):
        cmd1 = '..\\..\\uppaal-4.1.18\\uppaal.jar ..\\source\\%s.xml '% self.systemname
        os.system(cmd1)


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
        self.processorSizer.Add(self.editPname, flag=wx.LEFT, border=10)

        self.policyCombo = wx.ComboBox(self, -1, size=(70, -1), value=self.policyList[0], choices=self.policyList, style=wx.CB_DROPDOWN)
        self.processorSizer.Add(self.policyCombo, flag=wx.LEFT, border=10)

        self.preemptCombo = wx.ComboBox(self, -1, size=(70, -1), value=self.preemptList[0], choices=self.preemptList, style=wx.CB_DROPDOWN)
        self.processorSizer.Add(self.preemptCombo, flag=wx.LEFT, border=10)
        self.SetSizerAndFit(self.processorSizer)


class SpecProcessor(FirstSpecProcessor):
    proDelButton = None

    def __init__(self, parent):
        FirstSpecProcessor.__init__(self, parent)
        self.proDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.processorSizer.Add(self.proDelButton, flag=wx.LEFT, border=15)
        self.SetSizerAndFit(self.processorSizer)


class BusPanel(wx.Panel):
    edit_bcet = None
    edit_wcet = None
    sizer = None

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.edit_bcet = wx.TextCtrl(self, size=(70, -1))
        self.sizer.Add(self.edit_bcet, flag=wx.LEFT, border=10)
        self.edit_wcet = wx.TextCtrl(self, size=(70, -1))
        self.sizer.Add(self.edit_wcet, flag=wx.LEFT, border=10)
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
        self.taskSizer.Add(self.editTid, flag=wx.LEFT, border=10)
        self.editOffset = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editOffset, flag=wx.LEFT, border=10)
        self.editBcet = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editBcet, flag=wx.LEFT, border=10)
        self.editWcet = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editWcet, flag=wx.LEFT, border=10)
        self.editDeadline = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editDeadline, flag=wx.LEFT, border=10)
        self.editPeriod = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editPeriod, flag=wx.LEFT, border=10)
        self.editProcessor = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editProcessor, flag=wx.LEFT, border=10)
        self.editPre = wx.TextCtrl(self, size=(70, -1))
        self.taskSizer.Add(self.editPre, flag=wx.LEFT, border=10)
        self.SetSizerAndFit(self.taskSizer)


class TaskPanel(FirstTaskPanel):
    taskDelButton = None

    def __init__(self, parent):
        FirstTaskPanel.__init__(self, parent)
        self.taskDelButton = wx.Button(self, size=(70, -1), label="Delete")
        self.taskSizer.Add(self.taskDelButton, flag=wx.LEFT, border=15)
        self.SetSizerAndFit(self.taskSizer)


def main():
    app = wx.App()
    frame = MainFrame(None, 'Real-time System Schedulability Analyse Tool')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()