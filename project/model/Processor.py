# coding:utf-8


class Processor(object):
    pid = None
    policy = None
    is_preemptible = None

    def __init__(self, pid, policy, is_preemptible):
        self.pid = pid
        self.policy = policy
        self.is_preemptible = is_preemptible

    def get_pid(self):
        return self.pid

    def get_policy(self):
        return self.policy

    def get_preempt(self):
        return self.is_preemptible

    def toString(self):
        return str(self.pid) + ',' + str(self.policy) + ',' + str(self.is_preemptible)
