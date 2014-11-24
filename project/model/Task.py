# coding: utf-8


class Task(object):
    #task id
    tau = None
    name = None
    period = None
    offset = None
    bcet = None
    wcet = None

    def __init__(self, tau, name, period, offset, bcet, wcet):
        self.tau = tau
        self.name = name
        self.period = period
        self.offset = offset
        self.bcet = bcet
        self.wcet = wcet

    def gettau(self):
        return self.tau

    def getname(self):
        return self.name

    def getperiod(self):
        return self.period

    def getoffset(self):
        return self.offset

    def getbcet(self):
        return self.bcet

    def getwcet(self):
        return self.wcet