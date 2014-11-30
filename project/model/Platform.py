# coding:utf-8


class Platform(object):
    pid = None
    name = None
    sch = None

    def __init__(self, pid, name, sch):
        self.pid = pid
        self.name = name
        self.sch = sch

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_sch(self):
        return self.sch


class Bus(Platform):
    speed = None

    def __init__(self, pid, name, sch, speed):
        Platform.__init__(self, pid, name, sch)
        self.speed = speed

    def get_speed(self):
        return self.speed