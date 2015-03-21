# coding : utf-8

import ConfigParser

from Task import Task
from Processor import Processor
from Dep import Dep
from Bus import Bus


class UserInput(object):
    """docstring for UserInput"""
    # config flag
    PROCESSOR = 'processor'
    P = 'p'
    BUS = 'bus'
    BCET = 'bcet'
    WCET = 'wcet'
    TASK = 'task'
    T = 't'
    DEPS = 'deps'
    D = 'd'

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

    def save(self, fsave):
        config = ConfigParser.ConfigParser()
        if len(self.processors) > 0:
            config.add_section(self.PROCESSOR)
            for index, a in enumerate(self.processors):
                config.set(self.PROCESSOR, self.P + str(index), a.toString())

        if self.bus is not None:
            config.add_section(self.BUS)
            config.set(self.BUS, self.BCET, self.bus.get_bcet())
            config.set(self.BUS, self.WCET, self.bus.get_wcet())

        if len(self.tasks) > 0:
            config.add_section(self.TASK)
            for index, a in enumerate(self.tasks):
                config.set(self.TASK, self.T + str(index), a.toString())

        if len(self.deps) > 0:
            config.add_section(self.DEPS)
            for index, a in enumerate(self.deps):
                config.set(self.DEPS, self.D + str(index), a.toString())

        config.write(fsave)
        pass

    def load(self, fopen):
        config = ConfigParser.ConfigParser()
        config.readfp(fopen)
        if config.has_section(self.PROCESSOR):
            proNames = config.options(self.PROCESSOR)
            for a in proNames:
                proString = config.get(self.PROCESSOR, a)
                proList = proString.split(',')
                self.processors.append(Processor(int(proList[0]), proList[1], proList[2]))

        if config.has_option('bus', 'bcet') and config.has_option('bus', 'wcet'):
            self.bus = Bus(config.getint('bus', 'bcet'), config.getint('bus', 'wcet'))

        if config.has_section(self.TASK):
            taskNames = config.options(self.TASK)
            for a in taskNames:
                taskString = config.get(self.TASK, a)
                taskList = taskString.split(',')
                self.tasks.append(Task(
                    int(taskList[0]),
                    int(taskList[1]),
                    int(taskList[2]),
                    int(taskList[3]),
                    int(taskList[4]),
                    int(taskList[5]),
                    int(taskList[6]),
                    self.processors[int(taskList[6])]
                ))

        if config.has_section(self.DEPS):
            depsNames = config.options(self.DEPS)
            for a in depsNames:
                depsString = config.get(self.DEPS, a)
                depsList = depsString.split(',')
                self.deps.append(Dep(int(depsList[0]), self.tasks[int(depsList[0])],
                                    int(depsList[1]), self.tasks[int(depsList[1])]))
        pass


    """def test(self):
        # tid, i_offset, offset, bcet, wcet, deadline, period, pe
        t1 = Task(0, 0, 2, 2, 18, 4, p1)
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
        self.deps.append(dep1)
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
        self.deps.append(dep1)"""
