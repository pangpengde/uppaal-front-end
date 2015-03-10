# coding:utf-8

import string
import re


class ResultAnalyse(object):
    resultFile = None
    traceFile = None
    init = 'Initial'
    waitingD = 'WaitingDependency'
    dResolved = 'DependencyResolved'
    ready = 'Ready'
    running = 'Running'
    finish = 'Finish'
    error = 'Error'
    state = {init, waitingD, dResolved, ready, running, finish, error}
    time = []
    excTime = []
    taskState = []
    N = None
    systemName = None
    resultToShow = None
    #the time from
    totalTime = 0

    def __init__(self):
        self.systemName = 'model2'
        self.read_result()
        self.trace_analyse()

    def read_result(self):
        self.resultFile = file('../source/%s.result' % self.systemName, 'r')
        lines = self.resultFile.readlines()
        for l in lines:
            if l == 'Showing counter example.':
                self.trace_analyse()
            elif 'Property is satisfied'in l:
                self.resultToShow = 'These tasks are schedulable.'
            else:
                self.resultToShow = 'Verification Failed.'
            self.resultFile.close()

    def trace_analyse(self):
        self.traceFile = file('../source/%s.trace' % self.systemName, 'r')
        #tempfile = open('../source/temp.txt', 'w')
        lines = self.traceFile.readlines()
        self.N = lines[2].count('Task')
        print self.N
        temp = 0
        for l in lines:
            #tempfile.write(l)
            if l == 'State:':
                pass
        self.traceFile.close()
        #tempfile.close()


if __name__ == '__main__':
    ra = ResultAnalyse()




