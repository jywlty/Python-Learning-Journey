#三国演义词频统计.py
import jieba
txt=open(r"C:\Users\Administrator\Desktop\Python-Learning-Journey\三国演义.txt","r",encoding="utf-8").read()
excludes={"东吴","于是","天下","引兵","次日","大喜","商议","如何","军士","左右","军马","将军","却说","荆州","二人","不可","不能","如此"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮"or word == "孔明曰":
        rword ="孔明"
    elif word == "关公"or word == "云长":
        rword ="关羽"
    elif word == "玄德"or word == "玄德曰"or word=="主公"or word=="刘皇叔":
        rword="刘备"
    elif word == "孟德"or word == "丞相":
        rword="曹操"
    else:
        reword=word
    counts[reword]=counts.get(reword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print(f"{word}:{count}")

    
