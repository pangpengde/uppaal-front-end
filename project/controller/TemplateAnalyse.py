# coding: utf-8

from xml.etree import ElementTree as et

from model.Template import Template
from model.UserInput import UserInput


class TemplateAnalyse(object):

    userinput = None
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
            self.template.set_stadep(dep.get_task().t_id, dep.get_predecessor().t_id)

    """@classmethod
    def read_template(self, path):
        # 将指定路径的template.xml解析出来
        tp = Template()
        tp.nta = et.parse(path)
        return tp"""


if __name__ == '__main__':
    analyse = TemplateAnalyse()
    # tp = analyse.read_template(r'..\\source\\Template.xml')
