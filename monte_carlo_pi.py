#蒙特卡罗方法求圆周率.py
from time import perf_counter
from random import random
dites=10000000
hits=0
start=perf_counter()
for i in range(1,dites+1):
    x,y=random(),random()
    if pow(x**2+y**2,1/2)<=1:
        hits+=1
pi=4*(hits/dites)
print("圆周率是{:.5f}".format(pi))
print("执行时间是{}s".format(perf_counter()-start))