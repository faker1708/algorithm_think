

import pid


import random

import matplotlib.pyplot as plt


plt.ion()
plt.figure(1)

t_list = []
result_list = []

def get_state(old_state,action):

    # aa  =    old_state + action
    # new_state = 0

    # aa = aa + random.randint(0,2**2-1)

    # new_state = aa - 10 - action*0.1 + random.randint(0,2**2-1)
    # new_state = aa + action *0.5    # 能收敛
    # new_state = old_state - 0.5* action ** 1
    # new_state = old_state + 0.5* action ** 1

    new_state = old_state+ action -10

    return new_state


def main():




    a = pid.pid()
    a.kp = 0.8
    a.ki = 0
    a.kd = 0.00

    target = 1024
    state = 0

    pricious = 2**3
    sh = 0  # 收敛半径

    for epoch in range(2**12):

        if(epoch>2**6):
            target = 2000

        error = target -state
        if(error>pricious):
            sh = epoch
        action = a.update(error)
        state = get_state(state,action)


        # 打印

        print(error,action,sh)

        if(epoch>0):
        
            t_list.append(epoch)
            # result_list.append(error)
            result_list.append(state)

            plt.plot(t_list, result_list,c='deeppink')  ## 保存历史数据
            plt.pause(0.1)

    plt.pause(100)

main()