import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Adams
#1階常微分方程式（放射性崩壊）
def func_dydt(y, t):
    dydt = -y

    return dydt

def plot2d(t_list, y_list, t_label, y_label, labels):
    plt.xlabel(t_label)  #x軸の名前
    plt.ylabel(y_label)  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.plot(t_list, y_list, label=labels)

# Euler法
def euler(t, y, h, b):
    y_ap = [y]
    t_ap = [t]

    while t < b:

        y += h * func_dydt(y, t)
        t += h
        y_ap.append(y)
        t_ap.append(t)
    return t_ap, y_ap

# 厳密解
def Extract(t):
    return np.exp(-t)

if (__name__ == '__main__'):
    start = 0.0
    end = 10
    l_slice = 100.2*(end - start)
    plt.figure(figsize=(7,7))
    
    #Euler
    h = 0.01
    b = end
    t_elr , y_elr = euler(start, 1.0, h, b)
    plt.plot(t_elr, y_elr, label='Euler')
    
    #Adams
    y_init = 1.0  #初期値
    y_adms = odeint(func_dydt, y_init, t_elr)
    plt.plot(t_elr, y_adms[:, 0], label='Adams')

    #extract
    ex_y = [Extract(t) for t in t_elr]
    plt.plot(t_elr, ex_y, label='Extract')
    plt.xlabel("$t$")
    plt.ylabel("$y(t)$")
    plt.grid()
    plt.legend()
    plt.savefig('resolt_cal.png')
    plt.show()
    

def cal_num_error(Adams, Euler, Ext):
    num_error_adms = []
    num_error_elr = []
    num_error_adms_elr = []
    for i in range(1002):
        num_error_adms.append(abs(Ext[i] - Adams[i]))
        num_error_elr.append(abs(Ext[i] - Euler[i]))
        num_error_adms_elr.append(abs(Euler[i] - Adams[i]))
    return [num_error_adms, num_error_elr, num_error_adms_elr]

data = cal_num_error(y_adms, y_elr, ex_y)
plt.figure(figsize=(7,7))
plot2d(t_elr, data[0], "$t$", "$num\_error$", "adms")
plot2d(t_elr, data[1], "$t$", "$num\_error$", "elr")
plt.grid()
plt.legend()
plt.savefig('num_error.png')
plt.show()
