#科赫雪花实例.py
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main():
    t.setup(600,600)
    t.speed(0)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    t.pencolor("blue")
    level=4
    for i in range(3):
        koch(400,level)
        t.right(120)
    t.hideturtle()
    t.done()
main()