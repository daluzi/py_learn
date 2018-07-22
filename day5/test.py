import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_excel("data721.xls",index_col=0,header=None)
# print(data.describe())
data.index.name='date'
data.columns=["sale1","sale2","sale3"]
# print(data.isnull())
# print(data.isnull().sum())
data["sale1"] = data["sale1"].fillna(data["sale1"].mean())
data["sale2"] = data["sale2"].fillna(data["sale2"].median())
#处理缺失值
data.interpolate(method='cubic')
data = data.dropna()
#数据离散化
d = pd.cut(data["sale1"],bins=range(0,5000,500),right=False,labels=list("ABCDEFGHI"))
data["sale1"] = d.values
print(data)
# data.hist()
# data.plot()
# plt.show()