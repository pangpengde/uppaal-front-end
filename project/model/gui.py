# coding:utf-8


import wx

class mainFrame(wx.Frame):

    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title=title, size=(800, 600))
        self.init_ui()

    def init_ui(self):
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


def main():
    app = wx.App()
    frame = mainFrame(None, 'Schedulability Analyse')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()