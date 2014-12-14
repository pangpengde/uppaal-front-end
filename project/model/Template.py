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

    def set_n(self, n):
        self.N = n

    def set_stadep(self, i, j):
        self.staDep[i][j] = 1

    def set_tasks(self, attribute):
        self.Tasks.append(attribute)

    def init_stadap(self):
        for i in range(0, self.N-1):
            for j in range(0, self.N-1):
                self.staDep[i][j] = 0


