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

    def get_tau(self):
        return self.tau

    def get_name(self):
        return self.name

    def get_period(self):
        return self.period

    def get_offset(self):
        return self.offset

    def get_bcet(self):
        return self.bcet

    def get_wcet(self):
        return self.wcet