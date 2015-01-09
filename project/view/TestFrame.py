import wx


class Panel(wx.Panel):
    def __init__(self, parent, id, pos, size):
        wx.Panel.__init__(self, parent, id, pos, size)


class Frame(wx.Frame):
    def __init__(self, parent, id, title, pos, size, style):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        framePanel = wx.Panel(self)
        self.userpanel = Panel(framePanel, -1, (0,0), (300,180))
        self.userpanel.SetBackgroundColour('Gold')


class Application(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        frame = Frame(None, -1, "Internet Login Tool", (-1,-1), (300,400),\
        wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        frame.Show()
        self.SetTopWindow(frame)

if __name__ == '__main__':
    app = Application()
    app.MainLoop()