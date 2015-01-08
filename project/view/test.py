#coding: utf-8
import time
import wx, os
import wx.animate

from operator import or_
from func import *
from threading import *


class M(object):
    idx = 0
    total = 0
    right = 0
    wrong = 0
    starticker = 0 #开始时间
    steps = []
    answer = 0
    pause = 1000
    pre = 'bmp' #0 is bmp,1 is if,2 is text



class FullScreenPanel(wx.Panel):

    def __init__(self,parent):
        wx.Panel.__init__(self,parent,name="FullScreenPanel",style= wx.DEFAULT_FRAME_STYLE | wx.WANTS_CHARS )
        self.SetBackgroundColour('black')



        self.TrialBtn = wx.Button(self,label="练习")
        self.TrialBtn.Bind(wx.EVT_BUTTON,self.BeginTrial)
        self.TestBtn = wx.Button(self,label="测试")
        self.TestBtn.Bind(wx.EVT_BUTTON,self.BeginTest)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(self.TrialBtn,0, wx.ALIGN_CENTER )
        sizer.Add(self.TestBtn,0, wx.ALIGN_CENTER )
        sizer.AddStretchSpacer()
        self.SetSizer(sizer)
        self.Layout()

    def hideImg(self):
        try:
            self.curImg.Show(False)
        except:
            pass

    def hideGif(self):
        try:
            self.curGif.Stop()
            self.curGif.Close()
            self.curGif.Show(False)
        except:
            print "hide gif error"
            pass

    def hideText(self):
        try:
            self.curText.Show(False)
        except:
            pass

    def KeyDownResponse(self,evt):
        code = evt.GetKeyCode()
        if code in (49,50):
            self.stopTimer()
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownNull)
            if code == 49:
                code = 1
            else:
                code = 2
            if code == M.answer:
                slapedTime = time.time() - M.starticker

                self.show(response['right'])
                M.right = M.right + 1
                M.total = M.total + 1
                rate = M.right/float(M.total)
            else:
                slapedTime = time.time() - M.starticker
                self.show(response['wrong'])
                M.wrong = M.wrong + 1
                M.total = M.total + 1
                rate = M.right/float(M.total)

            text = "正确率:%.3f 耗时:%.3f" % (rate,slapedTime)
            if self.practice:
                self.addText(text)
            self.fp.write(text+"\n")
            self.timer = wx.CallLater(M.pause,self.next)

        else:
            pass

    def addText(self,text):
        mm=wx.DisplaySize()
        x0 = 100
        y0 = 600
        self.curText = wx.StaticText(self,-1,text,(x0,y0),(160,0),wx.ALIGN_CENTER)
        font=wx.Font(18,wx.DECORATIVE,wx.NORMAL,wx.NORMAL)
        self.curText.SetFont(font)
        self.curText.SetForegroundColour("white")
        self.curText.SetBackgroundColour("black")
        self.curText.Show(True)

    def KeyDownNull(self,evt):
        pass

    def showText(self,text):
        mm=wx.DisplaySize()


        x0 = (mm[0] - 60) / 2
        y0 = (mm[1] - 60) / 2
        self.curText = wx.StaticText(self,-1,text,(x0,y0),(160,0),wx.ALIGN_CENTER)
        font=wx.Font(28,wx.DECORATIVE,wx.NORMAL,wx.NORMAL)
        self.curText.SetFont(font)
        self.curText.SetForegroundColour("white")
        self.curText.SetBackgroundColour("black")
        self.curText.Show(True)

    def showBmp(self,fpath):
        try:
            self.curImg.Show(False)
        except:
            pass
        mm=wx.DisplaySize()
        img = wx.Image(fpath, wx.BITMAP_TYPE_BMP)
        x0 = (mm[0] - img.GetWidth()) / 2
        y0 = (mm[1] - img.GetHeight()) / 2
        wxBitmap = img.ConvertToBitmap()
       # self.curImg.SetBitmap(wxBitmap)
        self.curImg = wx.StaticBitmap(self, -1, img.ConvertToBitmap(), (x0,y0), (img.GetWidth(), img.GetHeight()))
        self.curImg.Show(True)
        print "end.."+fpath

    def showGif(self,fpath):
        mm=wx.DisplaySize()

        img = wx.Image(fpath, wx.BITMAP_TYPE_GIF)
        x0 = (mm[0] - img.GetWidth()) / 2
        y0 = (mm[1] - img.GetHeight()) / 2
        self.curGif = wx.animate.GIFAnimationCtrl(self, -1, fpath, (x0,y0), (img.GetWidth(), img.GetHeight()))
        self.curGif.GetPlayer().UseBackgroundColour(True)
        self.curGif.Play()

    def show(self,fpath):
        type = getType(fpath)
        self.hideText()
        self.hideGif()
        if not type == M.pre:
            if type == "gif":
                self.hideText()
                self.hideImg()
                self.hideGif()

            elif type == "bmp":
                self.hideGif()
                self.hideText()
            else:
                self.hideImg()
                self.hideGif()
            M.pre = type

        print 'show '+fpath
        if  type == "bmp":
            self.hideText()
            self.showBmp(fpath)
        elif type == "gif":
            self.hideText()
            self.showGif(fpath)
        elif type == "":
            self.showText(fpath)

    def stopTimer(self):
        self.timer.Stop()

    def timeout(self):
        self.stopTimer()
        self.Bind(wx.EVT_KEY_DOWN,self.KeyDownNull)
        self.show(response['timeout'])
        M.total += 1
        rate = M.right / float(M.total)
        slapedTime = time.time() - M.starticker

        text = "正确率:%.3f %.3f" % (rate,slapedTime)
        if self.practice:
            self.addText(text)

        self.fp.write(text+"\n")
        self.timer = wx.CallLater(M.pause,self.next)



    def next(self):
        idx = M.idx
        if idx > len(M.steps)-1:
            self.stopTimer()
            print "over"
            return ""
        print 'current idx %s' %idx
        opType =  M.steps[idx][0]
        fpath = M.steps[idx][1]
        type = getType(fpath)
        sepTime = M.steps[idx][2]
        M.idx = idx+1

        self.show(fpath)
        if opType == 0: #退出
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownOver)
        if opType == 1: #等待space
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownTrigger)
        elif opType in (2,3): #空操作
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownNull)
            self.timer = wx.CallLater(sepTime, self.next)
        elif opType == 4:  #等待反映,1500ms 后
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownResponse) #多做一次也无所谓，让逻辑
            M.starticker = time.time()
            self.timer = wx.CallLater(sepTime, self.timeout)
        elif opType == 9:
            M.answer = M.steps[idx][3]
            self.Bind(wx.EVT_KEY_DOWN,self.KeyDownResponse)
            self.timer = wx.CallLater(sepTime, self.next)



    def KeyDownOver(self,evt):
        self.stopTimer()
        self.hideGif()
        self.hideText()
        self.hideImg()
        self.TrialBtn.Show()
        self.TestBtn.Show()
        try:
            self.fp.close()
        except:
            pass
        M.steps = []
        M.idx = 0
        M.total = 0
        M.right = 0
        M.wrong = 0
        M.starticker = 0 #开始时间
        M.steps = []
        M.answer = 0

    def KeyDownTrigger(self,evt):
        if evt.GetKeyCode() == 32:
            self.next()

    def getSavePath(self):
        sp = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+".txt"
        return os.path.join(os.getcwd(),sp)

    def BeginTest(self,evt):
        fpath = self.getSavePath()
        self.fp = open(fpath, 'w')

        self.practice = False
        self.TrialBtn.Hide()
        self.TestBtn.Hide()
        M.steps = getSteps(testConf)
        print M.steps
        self.next()
        self.FullScreen(evt)


    def BeginTrial(self,evt):
        fpath = self.getSavePath()
        self.fp = open(fpath, 'w')
        self.practice = True
        self.TrialBtn.Hide()
        self.TestBtn.Hide()
        M.steps = getSteps(trialConf)
        self.next()
        self.FullScreen(evt)

    def GetFlags(self):
        res = []
        val = "FULLSCREEN_ALL"
        res.append(getattr(wx,val))
        return reduce(or_,res,0)

    def FullScreen(self,evt):
        top = self.GetTopLevelParent()
        top.OnFullScreen(evt)

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, 'Test FullScreen', size=(600, 400))
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.client = FullScreenPanel(self)

        mbar = wx.MenuBar()
        the_menu = wx.Menu()
        fullscreenMI = the_menu.Append(wx.ID_ANY,"Full Screen\tF12","Toggles Full Screen Mode")
        mbar.Append(the_menu,"File")
        self.SetMenuBar(mbar)
        self.Bind(wx.EVT_MENU,self.OnFullScreen,id=fullscreenMI.GetId())


    def OnCloseWindow(self, event):
        self.Destroy()

    def OnFullScreen(self,event):
        flags = self.client.GetFlags()
        self.ShowFullScreen(not self.IsFullScreen(),flags)

class MainApp(wx.App):
    def OnInit(self):
        self.main = MainFrame(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True


def main():
    application = MainApp(redirect=False)
    application.MainLoop()

if __name__ == '__main__':
    main()