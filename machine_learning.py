#机械学习.py
from sklearn.linear_model import LinearRegression
X=[[80],[85],[90],[95],[100]]
y=[75,80,85,90,95]
model=LinearRegression()
model.fit(X,y)
x=eval(input("请输入作业成绩："))
print("预测分数：",model.predict([[x]]))