# import pandas as pd
# import numpy as np 

# s = pd.Series([1,2,4,np.nan,44,1])
# print(s)#Series的字符串表现形式为：索引在左边，值在右边。
# print(s > 2)
# print(s[s>2])
# print(s * 4)

# dates = pd.date_range('20160101',periods=6)
# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])#np.random.randn(6,4)表示6到4内的正太分布
# print(df)
# print(df['b'])
# #创建一组没有给定行标签和列标签的数据
# df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
# print(df1)

# df2 = pd.DataFrame({'A':1,'B':pd.Timestamp('20130102'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),'D':np.array([3]*4,dtype='int32'),'E':pd.Categorical(["as","asd","dfd","vfvf"]),'F':'foo'})
# print(df2)
# print(df2.dtypes)
# print(df2.index)
# print(df2.columns)
# print(df2.values)
# print(df2.describe())
# print(df2.T)
# #index排序后再输出
# print(df2.sort_index(axis=1,ascending=False))
# #值排序后再输出
# print(df2.sort_values(by='B'))


# df3 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
# print(df3)
# print(df3['A'])
# print(df3.A)
# print(df3.loc[:,['A','B']])
# print(df3.iloc[3:5,1:3])
# #混合选择
# print(df3.ix[:3,['A','C']])

# #pandas读写文件,巨方便!
# import pandas as pd 

# data = pd.read_excel('x.xls',header=1,index_col=1,nrows=10)
# print(data)
# data.to_excel('write.xls')
# data1=pd.read_csv('eee.txt',nrows=10,names=["a","b","c"])
# print(data1)


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# # 随机生成1000个数据
# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
 
# # 为了方便观看效果, 我们累加这个数据
# data.cumsum()

# # # pandas 数据可以直接观看其可视化形式
# # data.plot()

# # plt.show()
# data = pd.DataFrame(
#     np.random.randn(1000,4),
#     index=np.arange(1000),
#     columns=list("ABCD")
#     )
# data.cumsum().plot()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# sale = pd.read_excel("sale.xls",index_col=u"日期")
# stat = sale.describe()
# print(stat)
# plt.figure()
# p = sale.boxplot()
# plt.show()
# print(stat.loc["max"] - stat.loc["min"])
# print()


import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
df.plot()
plt.show()