# coding : utf-8

import Task
import Platform
import Mapping
import Dep
from Platform import Bus


class UserInput(object):
    """docstring for UserInput"""
    tasks = {}
    # platform includes bus
    platforms = {}
    mappings = {}
    deps = {}

    def __init__(self):
        pass

    def test(self):
        # tau, name, period, offset, bcet, wcet
        t1 = Task(1, 't1', 4, 0, 2, 2)
        self.tasks.append(t1)
        t2 = Task(2, 't2', 6, 0, 1, 1)
        self.tasks.append(t2)
        # TODO 把task里的变量都赋值上
        #pid, name, sch
        bus = Bus(1, 'bus', 'FP', 2)
        self.platforms.append(bus)
        p1 = Platform(2, 'p1', 'RM')
        self.platforms.append(p1)
        p2 = Platform(3, 'p2', 'RM')
        self.platforms.append(p2)
        # task, platform
        self.mappings.append(Mapping(t1, p1))
        self.mappings.append(Mapping(t2, p2))

        # dep = (origin, dest, data)
        dep1 = Dep(t1, t2, 2)
        self.deps.append(dep1)
