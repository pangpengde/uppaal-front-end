# coding: utf-8


class Template:
    """模板数据结构类"""
    # nta = None
    FP = 0
    RM = 1
    EDF = 2
    # 处理单元个数，包括processor和bus
    M = None
    # 每个处理器最大处理的任务数，通过统计mapping里processor对应的任务数，取最大值
    N = None
    # 总任务数，包括task声明的个数，以及传输的data大小大于0的dependency
    MN = None

    # 处理器的调度策略数组，顺序是Bus，Proc1，Proc2……可能的值是FP,RM,EDF
    processorScheduling = []
    # 处理器的处理矩阵，m行n列，每行为该处理器可以处理的任务编号1-mn，0代表没有
    onPE = []
    # 任务调度的优先级，可能值是任务编号1-mn，貌似都是按照任务声明顺序，没有特殊说明
    fpris = []
    # 各任务的周期，长度是mn，值是正整数
    pi = []
    # 各任务的offset，长度是mn，值是正整数
    offset = []

    # 静态依赖矩阵 mn*mv
    origdep = []
    # 动态依赖矩阵 mn*mn
    depend = []

    # EDF最短截止时间 调度策略下的优先级顺序，可能的值为任务编号1-mn？
    pri = []
    # 动态改变优先级
    NRSteps = None
    NROffSteps = None
    MAXOffStep = None
    MAXListSize = None
    # 长度为NROffSteps的数组，值为0-MAXOffStep
    OffSteps = []
    # NROffSteps*MN的矩阵，值为1-mn
    OffPrios = []
    # 长度为NRSteps的矩阵，值为0-MAXStep
    Steps = []
    # NRSTeps*mn的矩阵，值为1-mn
    Prios = []

    # 最长周期任务的周期
    MaxPi = None
    # 最大执行时间？
    MaxExe = None

    def __init__(self):
        pass

    def set_m(self, m):
        self.M = m

    def set_n(self, n):
        self.N = n

    def set_mn(self, mn):
        self.MN = mn

    def set_ps(self, ps):
        self.processorScheduling.append(ps)

    def set_onpe(self, onpe):
        self.onPE.append(onpe)

    def set_fpris(self, fpris):
        self.fpris.append(fpris)

    def set_pi(self, pi):
        self.pi.append(pi)

    def set_offset(self, offset):
        self.offset.append(offset)

    def set_origdep(self, i, j):
        self.origdep[i][j] = 1

    def set_depend(self, i, j):
        self.depend[i][j] = 1

    def set_pri(self, pri):
        self.pri.append(pri)

    def set_nrsteps(self, nrsteps):
        self.NRSteps = nrsteps

    def set_nroffsteps(self, nroffsteps):
        self.NROffSteps = nroffsteps

    def set_maxoffstep(self, maxoffstep):
        self.MAXOffStep = maxoffstep

    def set_maxlistsize(self, maxlistsize):
        self.MAXListSize = maxlistsize

    def set_offsteps(self, offstep):
        self.OffSteps.append(offstep)

    def set_offprios(self, offprios):
        self.OffPrios.append(offprios)

    def set_steps(self, step):
        self.Steps.append(step)

    def set_prios(self, prio):
        self.Prios.append(prio)

    def set_maxpi(self, pi):
        self.MaxPi = pi

    def set_maxexe(self, exe):
        self.MaxExe = exe




