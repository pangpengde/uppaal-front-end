# coding: utf-8

import Task


class Dep(object):
    origin = None
    dest = None
    data = None

    def __init__(self, origin, dest, data):
        self.origin = origin
        self.dest = dest
        self.data = data

    def get_origin(self):
        return self.origin

    def get_dest(self):
        return self.dest

    def get_data(self):
        return self.data