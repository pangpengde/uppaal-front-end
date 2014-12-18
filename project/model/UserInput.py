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
    bus = None
    deps = []

    def __init__(self):
       pass

    def get_tasks(self):
        return self.tasks

    def get_processors(self):
        return self.processors

    def get_bus(self):
        return self.bus

    def get_deps(self):
        return self.deps

    def test(self):
        # tid, i_offset, offset, bcet, wcet, deadline, period, pe
        '''t1 = Task(0, 0, 2, 2, 18, 4, p1)
        self.tasks.append(t1)
        t2 = Task(1, 2, 1, 1, 17, 6, p2)
        self.tasks.append(t2)
        t3 = Task(2, 3, 2, 2, 20, 6, p2)
        self.tasks.append(t3)
        t4 = Task(3, 3, 2, 3, 20, 6, p2)
        self.tasks.append(t4)
        #bus(bcet, wcet)
        self.bus = Bus(1, 2)
        # pid, policy, is_preemptible
        p1 = Processor(0, 'RMS', True)
        self.processors.append(p1)
        p2 = Processor(1, 'RMS', True)
        self.processors.append(p2)

        # dep = (task, predecessor)
        dep1 = Dep(t2, t1)
        self.deps.append(dep1)'''
        p1 = Processor(0, "RMS", True)
        p2 = Processor(1, "EDF", True)
        self.processors.append(p1)
        self.processors.append(p2)

        t1 = Task(0, 0, 2, 2, 4, 4, p1)
        t2 = Task(1, 0, 1, 1, 6, 6, p1)
        t3 = Task(2, 0, 2, 2, 6, 6, p2)
        t4 = Task(3, 40, 2, 3, 6, 6, p2)
        self.tasks.append(t1)
        self.tasks.append(t2)
        self.tasks.append(t3)
        self.tasks.append(t4)

        self.bus = Bus(1, 1)

        dep1 = Dep(t3, t2)
        self.deps.append(dep1)
