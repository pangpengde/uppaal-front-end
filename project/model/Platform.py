#coding:utf-8


class Platform(object):
    pid = None
    name = None
    sch = None

    def __init__(self, pid, name, sch):
        self.pid = pid
        self.name = name
        self.sch = sch

    def getpid(self):
        return self.pid

    def getname(self):
        return self.name

    def getsch(self):
        return self.sch


class Bus(Platform):
    speed = None

    def __init__(self, pid, name, sch, speed):
        Platform.__init__(self, pid, name, sch)
        self.speed = speed

    def getspeed(self):
        return self.speed