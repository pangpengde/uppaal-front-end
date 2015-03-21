# coding: utf-8


class Task(object):
    # task id
    t_id = None
    # the time offset for the task first released;
    i_offset = None
    # best case execution time of task.
    bcet = None
    # worst case execution time of task.
    wcet = None
    # the relative deadline,calculate at the period starts.
    deadline = None
    # period of the task
    period = None
    # the processor request to run the task
    peIndex = None
    pe = None

    def __init__(self, t_id,  i_offset, bcet, wcet, deadline, period, peIndex, pe):
        self.t_id = t_id
        self.i_offset = i_offset
        self.bcet = bcet
        self.wcet = wcet
        self.deadline = deadline
        self.period = period
        self.peIndex = peIndex
        self.pe = pe

    def get_tid(self):
        return self.t_id

    def get_ioffset(self):
        return self.i_offset

    def get_bcet(self):
        return self.bcet

    def get_wcet(self):
        return self.wcet

    def get_deadline(self):
        return self.deadline

    def get_period(self):
        return self.period

    def get_preIndex(self):
        return self.peIndex

    def get_pe(self):
        return self.pe

    def toString(self):
        return str(self.t_id) + ',' + str(self.i_offset) + ',' + str(self.bcet) + ',' + str(self.wcet) + ',' + str(self.deadline) + ',' + str(self.period) + ',' + str(self.peIndex)