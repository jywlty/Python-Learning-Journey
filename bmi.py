#肥胖测评.py
height,weight=eval(input("请依次输入您的身高和体重，中间用逗号隔开"))
bmi=weight/pow(height,2)
num,nut="",""
if bmi>=30:
    num,nut="肥胖","肥胖"
elif bmi>=28:
    num,nut="偏胖","肥胖"
elif bmi>=25:
    num,nut="偏胖","偏胖"
elif bmi>=24:
    num,nut="正常","偏胖"
elif bmi>=18.5:
    num,nut="正常","正常"
else:
    num,nut="偏瘦","偏瘦"
print("你的bmi指标是{}和{}".format(num,nut))
