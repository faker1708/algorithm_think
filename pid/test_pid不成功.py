import pid #导入上面的PID算法
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def test_pid(P, I , D, L):

    pid_a = pid.pid(P, I, D)

    pid_a.SetPoint=1.1
    pid_a.setSampleTime(0.01)

    END = L
    feedback = 0
    feedback_list = []
    time_list = []
    setpoint_list = []

    for i in range(1, END):
        pid_a.update(feedback)
        output = pid_a.output
        feedback +=output #PID控制系统的函数
        time.sleep(0.01)
        feedback_list.append(feedback)
        setpoint_list.append(pid_a.SetPoint)
        time_list.append(i)

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    feedback_smooth = interp1d(time_list, feedback_list, time_smooth)
    plt.figure(0)
    plt.grid(True)
    plt.plot(time_smooth, feedback_smooth,'b-')
    plt.plot(time_list, setpoint_list,'r')
    plt.xlim((0, L))
    plt.ylim((min(feedback_list)-0.5, max(feedback_list)+0.5))
    plt.xlabel('time (s)')
    plt.ylabel('pid (PV)')
    plt.title('PythonTEST pid--xiaomokuaipao',fontsize=15)

    plt.ylim((1-0.5, 1+0.5))

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_pid(1.2, 1, 0.001, L=100)