# coding : utf-8

import os

class Controller(object):

    """docstring for Controller"""
    def __init__(self):
       self.persistence = XmlDataPersistence() 
       
    @classmethod
    def modelValidate(path):
        #调用uppaal，验证model.xml,生成结果文件result.trace放在path路径下
        cmd = ''
        os.system(cmd)
        pass