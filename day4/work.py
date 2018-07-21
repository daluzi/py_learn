import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sale = pd.read_excel("data2.xls",index_col=0)
stat = sale.describe()
# print(sale[sale<500])
d = sale.count()
def select(low,high):
	ld = sale[sale>low].dropna(axis=0,how='any')
	hd = ld[sale<high].dropna(axis=0,how='any')
	return hd
ps = []
pl = []
lpl = []
pin = []
z = []
def selectcount():
	cd = 0
	for i in range(8):
		s = select(i*500,(i*500+500))
		cd = cd + s.describe().loc['count'][420]/d
		ps.append(s.describe().loc['count'][420])
		pl.append((s.describe().loc['count'][420]/d).values[0])
		lpl.append(cd.values[0])
		pin.append(s.describe().loc['mean'][420])
		z.append(s.median().values[0])
selectcount()

idates = pd.Series(['[0,500)','[500,1000)','[1000,1500)','[1500,2000)','[2000,2500)','[2500,3000)','[3000,3500)','[3500,4000)'])
df2 = pd.DataFrame({'频数' : pd.Series(ps,index=idates),
                    '频率' : pd.Series(pl,index=idates),
                    '累计频率' : pd.Series(lpl,index=idates),
                    '平均数' : pd.Series(pin,index=idates),
                    '中位数' : pd.Series(z,index=idates)})
                    
print(df2)
# df2.to_excel('1asdasds.xls')
