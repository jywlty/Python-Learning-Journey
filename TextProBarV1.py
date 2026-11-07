#TextProBarV1.py
import math
import time
scale=100
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    y=i+(1-math.sin(i*math.pi*2+math.pi/2))/-8
    c=(y/scale)*100
    a="*"*int(y//1)
    b="."*int(100-(y//1))
    d=time.perf_counter()-start
    print("\r{:^4.1f}%[{}->{}]{:.2f}s".format(c,a,b,d),end="")
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2,"-"))