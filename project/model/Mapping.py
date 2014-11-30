# coding:utf-8
import Task
import Platform


class Mapping(object):
    task = None
    platform = None

    def __init__(self, task, platform):
        self.task = task
        self.platform = platform

    def get_task(self):
        return self.task

    def get_platform(self):
        return self.platform