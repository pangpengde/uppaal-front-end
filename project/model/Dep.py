# coding: utf-8


class Dep(object):
    predecessor = None
    task = None

    def __init__(self, task, predecessor):
        self.task = task
        self.predecessor = predecessor

    def get_task(self):
        return self.task

    def get_predecessor(self):
        return self.predecessor
