# coding: utf-8

from xml.etree import ElementTree as et

from model.Template import Template
from model.UserInput import UserInput


class TemplateAnalyse:

    userinput = None
    template = None

    def __init__(self, userinput, template):
        self.userinput = userinput
        self.template = template

    @classmethod
    def readTemplate(self, path):
        # 将指定路径的template.xml解析出来
        tp = Template()
        tp.nta = et.parse(path)


        return tp


if __name__ == '__main__':
    analyse = TemplateAnalyse()
    # tp = analyse.readTemplate(r'..\\source\\Template.xml')
