# coding: utf-8

from xml.etree import ElementTree as et

from model.Template import Template
from model.UserInput import UserInput


class TemplateAnalyse(object):

    user_input = None
    template = None

    n = 0
    p = 0

    def __init__(self):
        self.user_input = UserInput()
        self.user_input.test()
        self.template = Template()
        for task in self.user_input.tasks:
            self.n += 1
            self.template.set_tasks(task.i_offset)
            self.template.set_tasks(task.offset)
            self.template.set_tasks(task.bcet)
            self.template.set_tasks(task.wcet)
            self.template.set_tasks(task.deadline)
            self.template.set_tasks(task.period)
            self.template.set_tasks(task.pe)
        self.template.set_n(self.n)
        self.template.init_stadap()
        for pe in self.user_input.processors:
            self.p += 1
        for dep in self.user_input.deps:
            t = dep.get_task()
            pr = dep.get_predecessor()
            self.template.set_stadep(t.t_id, pr.t_id)
        self.template.set_p(self.p)
        self.template.set_n(self.n)

    def get_ui(self):
        return self.user_input

    def get_template(self):
        return self.template

if __name__ == '__main__':
    template = TemplateAnalyse()
    print template.n
    print template.p
    # analyse = TemplateAnalyse()
    # tp = analyse.read_template(r'..\\source\\Template.xml')
