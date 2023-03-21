

class pid():

    def __init__(self):

        self.kp = 0.5
        self.ki = 1
        self.kd = 0.01


        # self.current_time = 0
        # self.total_time = 0
        self.i = 0  # 积分

        self.max_i = 20 #　限制积分有界

        self.old_error = 0     # 微分时要用 # 这个不好设，就设为0吧

        

    def get_p(self):
        p = self.error
        return p

    def get_i(self):


        # 解码
        i = self.i      
        error = self.error

        # 计算积分
        i += error


        # 无界变换成有界有多种函数 ，这里随便写一种简单的。不是我们的重点。

        if(abs(i)>self.max_i):
            if i>0:
                i = self.max_i
            else:
                i = -self.max_i

        # 更新
        self.i = i

        return i
    
    def get_d(self):

        oe = self.old_error
        e = self.error

        d = e-oe

        # 更新
        self.old_error = self.error

        return d


    def update(self,error):
        # interval 时间间隔，距离上次汇报过去了多久？
        # error 误差 这个误差有可能是个张量啊兄弟们


        # sp = self.sample_period
        
        # 间隔可以比采样间隔大，但太复杂 了，懒得写了，不重要
        # 简单点，默认固定时间采一次样，我们专注于pid 算法本身，不折腾采样的分析。

        self.error = error

        p = self.get_p() 
        i = self.get_i()
        d = self.get_d()

        # 

        kp = self.kp
        ki = self.ki
        kd = self.kd

        # 向量内积
        out = kp*p + ki *i + kd *d
        return out


