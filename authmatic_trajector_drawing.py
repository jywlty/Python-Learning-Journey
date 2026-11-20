#authmatic_trajector_drawing.py
import turtle as t
#准备海龟绘制窗口
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#读取数据
ls=[]
file=input()
f=open(file)
for line in f:
    line=line.replace("\n","")
    ls.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for item in ls:
    t.pencolor(item[3],item[4],item[5])
    t.fd(item[0])
    if item[1]:
        t.right(item[2])
    else:
        t.left(item[2])
t.hideturtle()
t.done()
