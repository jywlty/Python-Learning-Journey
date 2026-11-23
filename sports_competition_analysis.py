import random
def printInfo():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
def getInputs():
    a=eval(input("请输入选手A的能力值(0-1):"))
    b=eval(input("请输入选手B的能力值(0-1):"))
    n=eval(input("模拟比赛的场次:"))
    return a,b,n
def simNGames(proA,proB,n):
    winA,winB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(proA,proB)
        if scoreA>scoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB
def simOneGame(proA,proB):
    scoreA,scoreB=0,0
    conserve="A"
    while not gameOver(scoreA,scoreB):
        if conserve=="A":
            if random.random()<=proA:
                scoreA+=1
            else:
                conserve="B"
        else:
            if random.random()<=proB:
                scoreB+=1
            else:
                conserve="A"
    return scoreA,scoreB
def gameOver(a,b):
    return a==15 or b==15
def printsummary(winA,winB):
    n=winA+winB
    print("竞技分析开始,共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛,占比{:0.1%}".format(winA,winA/n))
    print("选手B获胜{}场比赛,占比{:0.1%}".format(winB,winB/n))
def main():
    printInfo()
    proA,proB,n=getInputs()
    winA,winB=simNGames(proA,proB,n)
    printsummary(winA,winB)
main()


    







