# coding: utf-8

import os


class Controller(object):
    modelPath = None
    propertyPath = None
    resultPath = None
    tracePath = None
    verifytaPath = None
    cmd = None

    """docstring for Controller"""

    def __init__(self):
        self.modelPath = r'..\source\model.xml'
        self.propertyPath = r'..\source\model.q'
        self.resultPath = r'..\source\model.result'
        self.tracePath = r'..\source\model.trace'
        self.verifytaPath = r'..\..\uppaal-4.1.18\bin-Win32\verifyta.exe'

    def model_validate(self):
         # 调用uppaal,验证model.xml,生成结果文件result.trace放在source文件夹下
        self.cmd = self.verifytaPath + ' -qst 1 ' + self.modelPath + ' ' + self.propertyPath \
                   + ' 1>' + self.resultPath + ' 2>' + self.tracePath
        os.system(self.cmd)


if __name__ == '__main__':
    test = Controller()
    test.model_validate()
