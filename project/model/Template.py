# coding: utf-8


class Template:
    """模板数据结构类"""
    #nta = None
    FP = 0
    RM = 1
    EDF = 2
    #处理单元个数，包括processor和bus
    M = 0
    #每个处理器最大处理的任务数，通过统计mapping里processor对应的任务数，取最大值
    N = 0
    # 总任务数，包括task声明的个数，以及传输的data大小大于0的dependency
    MN = 0

    #处理器的调度策略数组，顺序是Bus，Proc1，Proc2……可能的值是FP,RM,EDF
    processorScheduling = {}
    #处理器的处理矩阵，m行n列，每行为该处理器可以处理的任务编号1-mn，0代表没有
    onPE = {}
    #任务调度的优先级，可能值是任务编号1-mn，貌似都是按照任务声明顺序，没有特殊说明
    fpris = {}
    #各任务的周期，长度是mn，值是正整数
    pi = {}
    #各任务的offset，长度是mn，值是正整数
    offset = {}

    #静态依赖矩阵 mn*mv
    origdep = {}
    #动态依赖矩阵 mn*mn
    depend = {}

    #EDF最短截止时间 调度策略下的优先级顺序，可能的值为任务编号1-mn？
    pri = {}
    #动态改变优先级
    NRSteps = 0
    NROffSteps = 0
    MAXOffStep = 0
    MAXListSize = 0
    #长度为NROffSteps的数组，值为0-MAXOffStep
    OffSteps = {}
    #NROffSteps*MN的矩阵，值为1-mn
    OffPrios = {}
    #长度为NRSteps的矩阵，值为0-MAXStep
    Steps = {}
    #NRSTeps*mn的矩阵，值为1-mn
    Prios = {}

    #最长周期任务的周期
    MaxPi = 0
    #最大执行时间？
    MaxExe = 0

    #System系统描述
    #处理器部分前面已经全部定义了
    #任务在处理器上的最好、最坏执行时间，与到处理器之间的映射与onPE有关，这个是我自己定义的结构现在
    #excTime[MN][2] = {},形如excTime = {{2,2},{2,3}}
    excTime = {}

    def __init__(self):
        pass

        


