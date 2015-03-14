# coding:utf-8

import string
import re
import pprint


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
    trace = []
    #the time from
    clock = 0

    def __init__(self):
        self.systemName = 'model'
        self.read_result()
        if self.resultToShow == 'Verification Failed.\n':
            # wtf, sometimes it gives 'EXCEPTION: Failed to generate trace.'
            # have to make it robuster
            self.trace_analyse()
            self.trace_generate()
            self.add_trace_to_result()
        print self.resultToShow

    def read_result(self):
        self.resultFile = file('../source/%s.result' % self.systemName, 'r')
        lines = self.resultFile.readlines()
        for l in lines:
            if l == 'Showing counter example.':
                self.trace_analyse()
            elif 'Property is satisfied'in l:
                self.resultToShow = 'These tasks are schedulable.\n'
            else:
                self.resultToShow = 'Verification Failed.\n'
            self.resultFile.close()

    def trace_analyse(self):
        self.traceFile = file('../source/%s.trace' % self.systemName, 'r')
        #tempfile = open('../source/temp.txt', 'w')
        lines = self.traceFile.readlines()
        # next line, what if there is no lines[2], make it robust
        self.N = lines[2].count('Task')
        i = 0
        flag = False
        for l in lines:
            if 'State:' in l:
                flag = True
                i += 1
                continue
            elif flag is True:
                if i == 1:
                    i += 1
                    self.read_state(l)
                    continue
                elif i == 2:
                    flag = False
                    i = 0
                    self.read_time(l)
                    continue
            else:
                continue
        self.traceFile.close()

    def read_state(self, line):
        pattern = r"Task\(\d\)\.(\w+)"
        states = re.findall(pattern, line)
        self.taskState.append(states)

    def read_time(self, line):
        time_pattern = r"time\[\d\]\=(\d)"
        exc_pattern = r"exec\[\d\]\=(\d)"
        t = re.findall(time_pattern, line)
        e = re.findall(exc_pattern, line)
        new_t = [int(i) for i in t]
        new_e = [int(i) for i in e]
        self.time.append(new_t)
        self.excTime.append(new_e)

    def trace_generate(self):
        # print self.taskState
        # print self.time
        # print self.excTime
        lenth = len(self.taskState)
        self.trace = [[] for i in range(self.N+1)]
        self.trace[0].append('Time  ')
        for i in range(self.N):
            # print self.trace[i+1][0]
            self.trace[i+1].append('Task%d ' % i)
        elapse = 0
        for l in range(lenth):
            if l == 0:
                continue
            for i in range(self.N):
                if elapse <= 0:
                    elapse = self.excTime[l][i] - self.excTime[l-1][i]
            if elapse > 0:
                self.clock += elapse
                for i in range(self.N):
                    stat = self.taskState[l][i]
                    if stat == self.init or stat == self.finish:
                        c = ' '
                    elif stat == self.running:
                        c = '+'
                    elif stat == self.error:
                        c = 'X'
                    else:
                        c = 'O'
                    for n in range(elapse):
                        self.trace[i+1].append(c)
                elapse = 0
        for i in range(self.clock):
            self.trace[0].append(str(i))

    def test_print_trace(self):
        for l in self.trace:
            print l

    def add_trace_to_result(self):
        for l in self.trace:
            for i in l:
                self.resultToShow += '%s ' % i
            self.resultToShow += '\n'


if __name__ == '__main__':
    ra = ResultAnalyse()




