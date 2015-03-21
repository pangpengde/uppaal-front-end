# coding: utf-8


class Dep(object):
    taskIndex = None
    task = None
    predecessorIndex = None
    predecessor = None


    def __init__(self, taskIndex, task, predecessorIndex, predecessor):
        self.taskIndex = taskIndex
        self.task = task
        self.predecessorIndex = predecessorIndex
        self.predecessor = predecessor

    def get_task_index(self):
        return self.taskIndex

    def get_task(self):
        return self.task

    def get_pre_index(self):
        return self.predecessorIndex

    def get_predecessor(self):
        return self.predecessor

    def toString(self):
        return str(self.taskIndex) + ',' + str(self.predecessorIndex)