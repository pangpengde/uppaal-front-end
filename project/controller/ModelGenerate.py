# coding: utf-8

from TemplateAnalyse import TemplateAnalyse
from model import UserInput

class ModelGenerate(object):
    """docstring for ModelGenerate"""
    # task number and processor number
    const = 'const'
    equal = '='
    part1 = None
    # staDeps and tasks declaration
    part2 = None
    # model global declaration
    part3 = None
    template = TemplateAnalyse()
    ui = template.user_input
    proc = ui.processors
    bus = ui.bus

    def __init__(self):
        self.set_part1()
        self.set_part2()
        self.set_part3()
        self.write_model()

    def set_part1(self):
        self.part1 = self.const + 'N' + self.equal + self.template.n + '\n' \
            + self.const + 'P' + self.equal + self.template.p + '\n'

    def set_part2(self):
        pass

    def set_part3(self):
        pass

    def write_model(self):
        # print self.t1
        ft1 = open('../source/t1.xml', 'r')
        t1 = ft1.read()
        ft2 = open('../source/t2.xml', 'r')
        t2 = ft2.read()
        ft3 = open('../source/t3.xml', 'r')
        t3 = ft3.read()
        ft4 = open('../source/t4.xml', 'r')
        t4 = ft4.read()

        modelxml = open('../source/model.xml', 'w')

        modelxml.write(t1)
        modelxml.write(self.part1)
        modelxml.write(t2)
        modelxml.write(self.part2)
        modelxml.write(t3)
        modelxml.write(self.part3)
        modelxml.write(t4)

        ft1.close()
        ft2.close()
        ft3.close()
        ft4.close()
        modelxml.close()

if __name__ == '__main__':
    model = ModelGenerate()

