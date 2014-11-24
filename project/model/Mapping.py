#coding:utf-8
import model.Task
import model.Platform


class Mapping(object):
    task = None
    Platform = None

    def __init__(self, task, platform):
        self.task = task
        self.platform = platform

    def getorigin(self):
        return self.task

    def getdest(self):
        return self.platform