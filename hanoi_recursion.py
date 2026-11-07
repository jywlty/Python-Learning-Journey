count=0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print(f"{n}:{src}->{dst}")
        count+=1
    else:
        hanoi(n-1,src,mid,src)
        print(f"{n}:{src}->{dst}")
        count+=1
        hanoi(n-1,mid,dst,src)
n=eval(input())
src,dst,mid="A","C","B"
hanoi(n,src,dst,mid)
print(count)