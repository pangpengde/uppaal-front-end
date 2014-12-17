# coding: utf-8


class Template:
    """模板数据结构类"""
    # 处理单元个数，processor
    P = None
    # 总任务数，task声明的个数
    N = None

    # 静态依赖矩阵 n*n
    staDep = []

    #任务矩阵 n*7
    Tasks = []

    def __init__(self):
        pass

    def set_p(self, p):
        self.P = p

    def get_p(self):
        return self.P

    def set_n(self, n):
        self.N = n

    def get_n(self):
        return self.N

    def set_stadep(self, i, j):
        self.staDep[i][j] = 1

    def get_stadep(self):
        return self.staDep

    def set_tasks(self, attribute):
        self.Tasks.append(attribute)

    def get_tasks(self):
        return self.Tasks

    def init_stadap(self):
        self.staDep = [[0 for col in range(self.N)] for row in range(self.N)]


