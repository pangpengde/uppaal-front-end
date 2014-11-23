# coding: utf-8

from xml.etree import ElementTree as et

from model import Template


class TemplateAnalyse:

    def __init__(self):
        pass

    @classmethod
    def readTemplate(path):
        # 将指定路径的template.xml解析出来
        tp = Template()
        tp.nta = et.parse(path)


        return template


if __name__ == '__main__':
    analyse = TemplateAnalyse()
    tp = analyse.readTemplate(r'../sourcer/Template.xml')
