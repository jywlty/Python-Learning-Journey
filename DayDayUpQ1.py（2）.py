#DayDayUpQ1.py
def dayUP(dayfactor):
    dayup=1.0
    for i in range(1,366):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+dayfactor)
    return dayup
dayfactor=0.01
while (dayUP(dayfactor)<30):
    dayfactor+=0.0000000001
print("工作日需要努力的程度：{:.10f}".format(dayfactor))