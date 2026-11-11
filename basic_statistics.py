#基本统计值计算.py
def getNum():
    num=[]
    n=input()
    while n!="":
        num.append(eval(n))
        n=input()
    return num
def mean(numbers):
    s=0
    for item in numbers:
        s+=item
    return s/len(numbers)
def dev(numbers,mean):
    s=0
    for item in numbers:
        s+=(item-mean)**2
    return (s/(len(numbers)-1))**0.5
def median(numbers):
    numbers.sort()
    n=len(numbers)
    if n%2==0:
        return (numbers[n//2-1]+numbers[n//2])/2
    else:
        return numbers[n//2]
num=getNum()
m=mean(num)
print(f"平均值：{m}，方差：{dev(num,m)}，中位数：{median(num)}")

