# coding: utf-8

from TemplateAnalyse import TemplateAnalyse
from model import UserInput

class ModelGenerate(object):
    """docstring for ModelGenerate"""
    # task number and processor number
    const = 'const'
    int = 'int'
    task_t = 'task_t'
    equal = '='
    temp_i = 0
    part1 = None
    # staDeps and tasks declaration
    part2 = None
    # model global declaration
    part3 = None
    ta = None
    ui = None
    template = None
    procs = None
    bus = None

    def __init__(self):
        pass

    def init_ta(self):
        self.ui = self.ta.get_ui()
        self.template = self.ta.get_template()
        self.procs = self.ui.get_processors()
        self.bus = self.ui.get_bus()

    def genarate(self):
        self.set_part1()
        self.set_part2()
        self.set_part3()
        self.write_model()

    def set_part1(self):
        self.part1 = self.const + ' ' + self.int + ' N ' + self.equal + ' ' + str(self.template.get_n()) + ';\n'
        self.part1 += self.const + ' ' + self.int + ' P ' + self.equal + ' ' + str(self.template.get_p()) + ';\n'

    def set_part2(self):
        self.part2 = self.const + ' ' + self.int + ' ' + '[0,1]' + ' ' + 'staDep[N][N]' + self.equal + '{\n'
        # self.part2 += str(self.template.get_stadep())
        col = self.template.get_n()
        row = self.template.get_n()
        staDep = self.template.get_stadep()
        for i in range(row): # get_stadep()=[[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.part2 += '\t{'
            for j in range(col):
                if j == col-1:
                    self.part2 += str(staDep[i][j])
                else:
                    self.part2 += str(staDep[i][j]) + ','
            if i == row-1:
                self.part2 += '}\n'
            else:
                self.part2 += '},\n'
        self.part2 += '};\n'
        self.part2 += self.const + ' ' + self.task_t + ' ' + 'Tasks[N]' + self.equal + '{\n'
        col = 6
        row = self.template.get_n()
        tasks = self.template.get_tasks()
        for i in range(row):
            self.part2 += '\t{'
            for j in range(col):
                if j == col-1:
                    self.part2 += str(tasks[i][j])
                else:
                    self.part2 += str(tasks[i][j]) + ','
            if i == row-1:
                self.part2 += '}\n'
            else:
                self.part2 += '},\n'
        self.part2 += '};'

    def set_part3(self):
        self.part3 = self.const + ' ' + 'processors' + ' ' + 'pes' + ' ' + self.equal + '{\n'
        for proc in self.procs:
            if proc.get_pid() == self.template.get_p() - 1:
                self.part3 += '\t{' + str(proc.get_pid()) + ',' + proc.get_policy() + ',' \
                              + str(proc.get_preempt()).lower() + '}\n'
            else:
                self.part3 += '\t{' + str(proc.get_pid()) + ',' + proc.get_policy() + ','\
                              + str(proc.get_preempt()).lower() + '},\n'
        self.part3 += '};\n'
        self.part3 += 'bus' + ' ' + self.equal + ' ' + 'BUS(' + str(self.bus.get_bcet()) + ','\
                      + str(self.bus.get_wcet()) + ');\n'

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

