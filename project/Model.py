# coding : utf-8

class Model(object):
    """docstring for Model"""

    template = None
    userInput = None

    def __init__(self, template, userInput):
        self.template = template
        self.userInput = userInput

    @classmethod
    def modelGen(path):
        # 将本类写成model.xml放在指定路径下
        pass