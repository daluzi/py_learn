# #coding = utf-8
# import urllib.request
# import re

# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html

# def getImg(html):
#     reg = 'src="(.+?\.png)" alt='
#     imgre = re.compile(reg)
#     imglist = re.findall('imgre', 'html')
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl, '%s.png' % x)
#         x+=1
#     return imglist

# html = getHtml("http://www.cqupt.edu.cn/cqupt/index.shtml")

# print (getImg(html))

# import urllib.parse
# import urllib.request

# # params  CategoryId=808 CategoryType=SiteHome ItemListActionName=PostList PageIndex=3 ParentCategoryId=0 TotalPostCount=4000
# def getHtml(url,values):
#     user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
#     headers = {'User-Agent':user_agent}
#     data = urllib.parse.urlencode(values)
#     response_result = urllib.request.urlopen(url+'?'+data).read()
#     html = response_result.decode('utf-8')
#     return html

# #获取数据
# def requestCnblogs(index):
#     print('请求数据')
#     url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
#     value= {
#          'CategoryId':808,
#          'CategoryType' : 'SiteHome',
#          'ItemListActionName' :'PostList',
#          'PageIndex' : index,
#          'ParentCategoryId' : 0,
#         'TotalPostCount' : 4000
#     }
#     result = getHtml(url,value)
#     return result

# import requests
# import re

# # 获取网页源码
# url = 'http://www.ivsky.com/tupian/xiaohuangren_t21343/'
# data = requests.get(url).text

# #正则表达式三部曲
# #<img src="http://img.ivsky.com/img/tupian/t/201411/01/xiaohuangren-009.jpg" width="135" height="135" alt="卑鄙的我小黄人图片">
# regex = r'<img src="(.*?.jpg)"'#匹配网址
# pa = re.compile(regex)#转为pattern对象
# ma = re.findall(pa, data)#findall 方法找到所有的符合pa的对象，添加到一个列表中并返回
# #print(ma)#图片网址列表
# print('本次爬取共获取图片'+str(len(ma))+'张')#列表长度，即找到图片个数

# i = 0#这里的i， 只是为了给图片命名。。。
# for imgurl in ma:
#     i += 1
#     print('正在爬取'+imgurl)
#     imgdata = requests.get(imgurl).content
#     with open(str(i)+'.jpg', 'wb') as f:
#         f.write(imgdata)

# print('爬取完毕！')

# #抓取时间
# import time

# localtime = time.localtime(time.time())#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=15, tm_hour=14, tm_min=10, tm_sec=27, tm_wday=6, tm_yday=196, tm_isdst=0)
# localtime = time.asctime(localtime)
# print ("本地时间为：",localtime)
# print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# import datetime
# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)

# L1 = ['www','baidu','com']
# print('.'.join(L1))

# def printme(str):
#     "打印传入的字符串到标准显示设备上"
#     print(str)
#     return
# printme("asd")

# def ChangeInt( a ):
#     a = 10
 
# b = 2
# ChangeInt(b)
# print (b)

# print(divmod(1,2))

# s1 = 'apple+peach+banana+pear'
# s2 = s1.split('+')
# s3 = '-'.join(s2)
# print(s2)
# print(s3)

# import decimal
# a = decimal.Decimal(50)
# b = decimal.Decimal(50.111)
# print(a + b)

# var1 = 'Hello World!'
# var2 = 'Python Runoob'

# print(var1[0])
# print(var2[1:])

# import time
 
# # 格式化成2016-03-20 11:45:39形式
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
 
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
  
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# import calendar

# cal = calendar.month(2018,7)
# print(cal)

# import datetime

# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)

# def SayLove(str):
#     print("I love ",str)
#     return

# SayLove("as")

# def IsRun(year):
#     if year % 4 == 0 and year % 100 != 0:
#         pass
#         print("这是闰年")
#     else:
#         print("这不是闰年")

# IsRun(input("enter year:"))


# def addNum():
#     sum = 0
#     for x in range(1,100,2):
#         sum += x
#     return sum
# print(addNum())

# thesum = 0
# thelist = list(range(1,101))
# for x in thelist:
#     thesum += x
# print(thesum)

# # sing = int(input("enter a single number:"))
# a = input("请输入一个数，0表示结束")
# def ISingle(num):
#     x = 2
#     if x < num and x > 1:
#         pass
#         num % x != 0
#         print(num,"是质数")
#         x += 1

# # ISingle(5)

# if a != 0:
#     pass
#     ISingle(a)
#     input("请输入一个数，0表示结束")
# else:
#     print (输入结束)

# def volum(r):
#     v = 3 / 4 * 3.14 * pow(r,3)
#     print("体积为：",v)
# volum(1)

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

def low():
    pass
    n = ['asD','asd']
    print([s.lower() for s in n])
low()