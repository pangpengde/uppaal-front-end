# coding: utf-8

import wx
from view import MainFrame3


class MainApp(MainFrame3.MainFrame):
    def __init__(self, parent, title):
        MainFrame3.MainFrame.__init__(self, parent, title=title)


def main():
    app = wx.App()
    window = MainApp(None, 'Real-time System Schedulability Analyse Tool')
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()