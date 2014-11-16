# coding : utf-8

class Controller(object):

    persistence = None
    data = None

    """docstring for Controller"""
    def __init__(self):
       self.persistence = XmlDataPersistence() 
       
    @classmethod
    def load(path):
        data = self.persistence.input(path)

    @classmethod
    def operation():
        if data == None:
            return
        # TODO

    @classmethod
    def output(path):
        self.persistence.output(self.data, path)