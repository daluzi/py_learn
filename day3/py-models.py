# import numpy as np
# a = np.array([0,2,5,6,8])
# print(a)

# a1 = np.zeros(10)#默认情况下创建的是浮点型
# print(a1)

# a2 = np.zeros((3,4))
# print(a2)

# a3 = np.ones((3,4,2))
# print(a3)

# a4 = np.empty((2,3))
# print(a4)

# a5 = np.ones_like(a4)
# print(a5)

# a6 = np.eye(5)
# print(a6)

# a7 = np.arange(3,15)
# print(a7)

# b = np.array([[1,2,4],[4,5,6]])
# print(b.dtype)
# print(b.shape)
# print(b + 3)
# print(b + b)
# print(b * 10)
# print(2/b)

# c1 = np.arange(12)
# print(c1)
# print(c1[2:9])
# c1[2:7] = 7
# print(c1)#给一个切片赋值，该值会自动广播到整个区间

# L1 = range(12)
# #L1[2:9] = 7这句是错误的，因为列表不支持对切片广播赋值

# c2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c2)
# print(c2[2][1])#8
# print(c2[0:2][1])#[4,5,6]
# print(c2[:,0:2])#[[1 2]
# 				# [4 5]
# 				# [7 8]]
# print(c2[0:2,1])#[2,5]

# name = np.array(['zhang','li','wang','zhang'])
# print(name == 'zhang')#[ True False False  True]

# score = np.array([95,95,49,30,80,34,34,87,93,78,88,100])
# mark = score >= 60
# print(score[mark])
# score[score <= 60] = 60
# print(score)

# #合并
# aa = np.array([1,1,1])
# bb = np.array([2,2,2])
# print(np.vstack((aa,bb)))
# print(np.hstack((aa,bb)))

# print(np.exp(300))
# print(np.sign(-11))
# print(np.isnan(np.inf))
# print(np.tan(1.2))
# print(np.arcsin(1/np.pi))
# print(np.add(4,5))
# print(np.maximum(np.random.randn(10),np.random.randn(10)))



# import matplotlib.pyplot as plt
# t = np.linspace(0,2*np.pi,100)
# xs,ys = np.meshgrid(t,t)
# x = np.linspace(-1,1,50)
# y1 = 2*x +1
# y2 = x**2
# x0 = 1
# y0 = 2**x0
# plt.figure()
# plt.xlim((-2,1))
# plt.ylim((2,3))
# plt.xlabel('daluzi')
# plt.ylabel('daluzi')
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data',0))
# #set line styles
# l1, = plt.plot(x,y1,label="linear line")
# l2, = plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--',label='square line')
# #legend为我们添加图例
# plt.legend(loc='upper right')#loc那句话的意思是将图例添加在右上角
# plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# plt.scatter([x0, ], [y0, ], s=50, color='b')
# plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# plt.plot(x,y1)
# plt.plot(x,y2,color = 'red',linewidth = 1.0,linestyle = '--')
# plt.show()

# #散点图
# import matplotlib.pyplot as plt
# import numpy as np

# n = 2014
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# T = np.arctan2(Y,X)

# plt.scatter(X,Y,s=75,c = T,alpha = .5)
# plt.xlim(-1.5, 1.5)
# plt.xticks(())  # ignore xticks
# plt.ylim(-1.5, 1.5)
# plt.yticks(())  # ignore yticks

# plt.show()

#3D图
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap=plt.get_cmap('rainbow'))
plt.show()