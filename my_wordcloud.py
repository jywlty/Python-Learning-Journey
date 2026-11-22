import wordcloud
import jieba
import os
import numpy as np
from PIL import Image
file=input("请输入词云文本：")
f=open(os.path.abspath(file),"r",encoding='utf=8')
ls=jieba.lcut(f.read())
t=" ".join(ls)
p=Image.open(os.path.abspath(input("输入词云形状的文件："))).convert("RGBA")
pt=Image.new('RGBA',p.size,(255,255,255,255))
p = Image.alpha_composite(pt, p)
mk=np.array(p.convert("L"))
w=wordcloud.WordCloud(font_path='msyh.ttc',width=1000,height=700\
                      ,background_color='white',mask=mk)
w.generate(t)
w.to_file(input("输出词云图片的文件名："))
