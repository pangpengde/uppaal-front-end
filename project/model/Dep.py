# coding: utf-8

import Task


class Dep(object):
    predecessor = None
    taskName = None
    data = None

    def __init__(self, predecessor, taskName, data):
        self.predecessor = predecessor
        self.taskName = taskName
        self.data = data

    def get_predecessor(self):
        return self.predecessor

    def get_taskname(self):
        return self.taskName

    def get_data(self):
        return self.data