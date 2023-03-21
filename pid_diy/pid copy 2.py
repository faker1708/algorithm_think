

class pid():

    def __init__(self):

        self.kp = 2
        self.ki = 0
        self.kd = 0


        # self.current_time = 0
        self.total_time = 0
        
        sp = 10
        self.sample_period = sp # 采样间隔 一般是常量。
        self.sample_patience = sp # 采样耐心度，如果没到采样 的时候，就不采样 ，但要计时。





    def update(self,error,interval):
        # interval 时间间隔，距离上次汇报过去了多久？
        # error 误差 这个误差有可能是个张量啊兄弟们


        sp = self.sample_period
        
        shang = interval // sp
        yu = interval% sp

        

