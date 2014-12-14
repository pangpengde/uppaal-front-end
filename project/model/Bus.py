# coding:utf-8


class Bus(object):
    bcet = None
    wcet = None

    def __init__(self, bcet, wcet):
        self.bcet = bcet
        self.wcet = wcet

    def get_bcet(self):
        return self.bcet

    def get_wcet(self):
        return self.wcet