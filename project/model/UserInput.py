# coding : utf-8

from Task import Task
from Processor import Processor
from Dep import Dep
from Bus import Bus


class UserInput(object):
    """docstring for UserInput"""
    tasks = []
    # platform includes bus
    processors = []
    bus = []
    deps = []

    def __init__(self):
       pass

    def test(self):
        # tau, i_offset, offset, bcet, wcet, deadline, period, pe
        t1 = Task(0, 0, 1, 2, 2, 18, 4, 0)
        self.tasks.append(t1)
        t2 = Task(1, 2, 1, 1, 1, 17, 6, 1)
        self.tasks.append(t2)
        t3 = Task(2, 3, 1, 2, 2, 20, 6, 1)
        self.tasks.append(t3)
        t4 = Task(3, 3, 1, 2, 3, 20, 6, 1)
        self.tasks.append(t4)
        # TODO 把task里的变量都赋值上
        #bus(bcet, wcet)
        bus = Bus(1, 2)
        self.bus.append(bus)
        # pid, policy, is_preemptible
        p1 = Processor(0, 'RM', True)
        self.processors.append(p1)
        p2 = Processor(1, 'RM', True)
        self.processors.append(p2)

        # dep = (task, predecessor)
        dep1 = Dep(t2, t1)
        self.deps.append(dep1)
