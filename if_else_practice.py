#分支语句用法.py
scale=eval(input())
if scale>=90:
    grade="A"
elif scale>=80:
    grade="B"
elif scale>=70:
    grade="C"
elif scale>=60:
    grade="C"
else:
    grade="E"
print("你的成绩所在的等级为{}级".format(grade))