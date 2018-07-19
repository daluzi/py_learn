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

# def low():
#     pass
#     n = ['asD','asd']
#     print([s.lower() for s in n])
# low()

# class Compile(object):
#     """docstring for Compile"""
#     def __init__(self, arg):
#         super(Compile, self).__init__()
#         self.arg = arg

# class People:
#     #定义基本属性
#     name = 'daluzi'
#     age = 18
#     #定义私有属性，在类外部无法直接访问
#     __height = 180
#     #定义构造方法
#     def __init__(self,n,a,h):
#         self.name = n
#         self.age = a
#         self.__height = h
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))


# class animal(People):
# 	"""docstring for animal"""
# 	weight = ''
# 	def __init__(self,n,a,h,w):
# 		People.__init__(self,n,a,h)
# 		self.weight = w
# 	def speak(self):
# 		print("%s 说： 我%d岁了，我 %s重"%(self.name,self.age,self.weight))

# class robot():
# 	"""docstring for robot"""
# 	beati = ''
# 	name = ''
# 	def __init__(self, b,n):
# 		self.beati = b
# 		self.name = n
# 	def speak(self):
# 		pass
# 		print("我叫 %s，我是个皮皮怪，我 %s"%(self.name,self.beati))

# #多重继承
# class sample(robot,animal):
# 	a = ''
# 	def __init__(self,n,a,h,w,b):
# 		pass
# 		animal.__init__(self,n,a,h,w)
# 		robot.__init__(self,b,n)
		
# p = sample('dapeizi',17,165,'180kg','丑')
# p.speak()#方法名相同，默认调用的是在括号排前的父类的方法。


# fpath = r'E:/学习总结/as.txt'
# with open(fpath,'w',encoding='utf-8',errors='ignore') as f:
# 	f.write("Hello Python!")

# from io import StringIO
# f = StringIO()
# f.write('jasds')
# print(f.getvalue())#getvalue方法用于获得写入后的str
# g = StringIO('Hello~\nbai~')
# while True:
# 	s = g.readline()
# 	if s == '':
# 		break
# 	print(s.strip())

# from io import BytesIO
# f = BytesIO()
# print(f.write('中文'.encode('utf-8')))#6 请注意，写入的不是str，而是经过UTF-8编码的bytes。
# print(f.getvalue())#b'\xe4\xb8\xad\xe6\x96\x87'
# g = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(g.read())

# import os
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))#当前路径用'.'表示
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('F:/py学习/text','testdir')
# # 然后创建一个目录:
# os.mkdir('F:/py学习/text/testdir')
# # 删掉一个目录:
# os.rmdir('F:/py学习/text/testdir')
# print(os.listdir('.'))
# #利用py的特性显示当前目录下面的所有目录（文件夹）
# s = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(s)
# #要列出所有的.py文件
# q = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(q)

# #模仿输出dir -l
# from datetime import datetime
# import os

# pwd = os.path.abspath('.')

# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')

# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# import json
# d = dict(name = 'Bob',age = 20,score = 88)
# print(json.dumps(d))
# #dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# # 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
# json_str = '{"age":20,"score":88,"name":"daluzi"}'
# print(json.loads(json_str))



class University(object):
	schoolname = "CQUPT"
	def __init__(self,address,famous):
		self.__address = address
		self.__famous = famous
		pass
	def schn(self):
		print("学校名称是：%s"%self.schoolname)
		pass

class College(University):
	def __init__(self):
		pass

class Department(University):
	def __init__(self):
		pass

class Ecnomic(College):
	_address = ''
	_number = 0
	def __init__(self,address,number):
		self._address = address
		self._number = number  
	def duty(self):
		print("经济学院的号码是:%d"%self._number)
	def issue(self):
	   		pass   	
        

class ComputerScienceCollege(University):
	"""docstring for ComputerScienceCollege"""
	def  __init__(self):
		pass
		
	class CS:
		"""docstring for CS"""
		__location = "apartment 2"
		__course = ['big data', 'database', 'programing']
		__population = 0
		def __init__(self, population):
			self.__population = population
		
		def teach(self):
			print("CS teaching") 
			
		def exam(self):
			print("CS examing")

		def get_location(self):
			return self.__location

		def set_lcoation(self, location):
			self.__location = location

		def get_course(self):
			return self.__course

		def set_course(self, course):
			self.__course = course

		def get_population(self):
			return self.__population

		def set_population(self, population):
			self.__population = population

	class IS:
		"""docstring for IS"""
		__location = "apartment 2"
		__course = ['network security', 'cryptography', 'programing']
		__population = 0
		def __init__(self, population):
			self.__population = population
		
		def teach(self):
			print("IS teaching")
			
		def exam(self):
			print("IS examing")

		def get_location(self):
			return self.__location

		def set_lcoation(self, location):
			self.__location = location

		def get_course(self):
			return self.__course

		def set_course(self, course):
			self.__course = course

		def get_population(self):
			return self.__population

		def set_population(self, population):
			self.__population = population

class Teacher(University):
    def __init__(self,name,id,age,sex,course):
        self.__name=name
        self.__id=id
        self.__age=age
        self.__sex=sex
        self.__course=course
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_age(self):
        return self.__age
    def get_sex(self):
        return self.__sex
    def get_course(self):
        return self.__course

    def teach(self):
        print("负责上课")
    def answer_Q(self):
        print("负责答疑")
    def test(self):
        print('安排考试')
    def homework(self):
        print('布置作业')

class Student(University):
    def __init__(self,name,id,age,sex):
        self.__name = name
        self.__id=id
        self.__age=age
        self.__sex=sex
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_age(self):
        return self.__age
    def get_sex(self):
        return self.__sex

    def study(self):
        print("学习")
    def takeTest(self):
        print('考试')
    def finishHomework(self):
        print('完成作业')

class Marxcollege(University):
    def __init__(self,centeraddress,major,introduction,studentnumber):
        self.__centeraddress = centeraddress
        self.__major = major
        self.__introduction = introduction
        self.__studentnumber = 537
    def centeraddress(self):
        print("学院坐落于重庆邮电大学二教学楼后")
    def major(self):
        print("马克思学院主要教学哲学方面的专业知识")
    def introduction(self):
        print("主要从事于马克思主义的各种发展理论与中国近现代理论的发展研究即教学")
    def studentnumber(self):
        print("当前在读学生人数为537人")
    def get_centeraddress(self):
        return self.__centeraddress
    def get_major(self):
        return self.__major
    def get_introduction(self):
        return self.__introduction
    def get_studentnumber(self):
        return self.__studentnumber
class Office(Marxcollege):
    def __init__(self, officer,teacherduty,address):
        self.__officer = officer
        self.__teacherduty = teacherduty
        self.__address = address
    def officer(self):
        print("主要负责一个学院的正常运作，并负责该学院学生在校期间的事情处理与管理")
    def teacherduty(self):
        print("负责教授学生们相关知识的职能")
    def address(self):
        print("坐落于马克思大楼里二层")
    def get_officer(self):
        return self.__officer
    def get_teacherduty(self):
        return self.__teacherduty
    def get_address(self):
        return self.__address
class Studyroom(Marxcollege):
    def __init__(self, manager, function, address):
        self.__manager = manager
        self.__function = function
        self.__address = address
    def manager(self):
        print("负责该教学教室的日常事务")
    def function(self):
        print("作为学生学习及复习场所")
    def address(self):
        print("二教学楼")
    def get_manager(self):
        return self.__manager
    def get_function(self):
        return self.__function
    def get_address(self):
        return self.__address


class Cofl(University):
    def __init__(self):
        self.__stuNumber=550
        self.__teaNumber=88
        self.__proNumber=33
        self.__masterNumber=57
        self.__docNumber=13
    def CollegeName(self):
        print('College of Foreign Languages')
    def Location(self):
        print('重邮外国语学院位于重庆邮电大学第五教学楼')
    def Introduction(self):
        print('重邮外国语学院成立于2001年，1999年开始招收英语专业本科生。目前有英语和翻译两个本科专业以及翻译硕士专业学位授权点，是培养高层次、应用型、信息技术语言服务人才的摇篮')
    def Specialty(self):
        return ['英语','翻译','翻译硕士']
    def get__stuNumber(self):
        return self.__stuNumber
    def get__teaNumber(self):
        return self.__teaNumber
    def get__proNumber(self):
        return self.__proNumber
    def get__masterNumber(self):
        return self.__masterNumber
    def get__docNumber(self):
        return self.__docNumber
class MajorinEnglish(Cofl):
    def __init__(self):
        self.__majorName='English'
        self.__address='Fifth teaching buildings'
        self.__number=223
    def TeacherFunction(self):
        print('（1）传播和传递人类科学文化知识，使之延续和发展\n')
        print('（2）发展学生智力和体力，培养学生良好的思想道德品质\n')
        print('（3）宣传社会思想，发展和创造新的科学文化知识')       
    def TeacherRight(self):
        print('教育教学权，科学研究权，指导评价权，获取报酬权，民主管理权，进修培训权')
    def TeacherDuty(self):
        print('（1）遵守宪法、法律和职业道德，为人师表；\n')
        print('（2）贯彻国家教育方针，遵守规章制度，执行学校的教学计划，完成教育工作任务；\n')
        print('（3）对学生进行宪法所确定的基本原则的教育和爱国主义、民族团结的教育，法制教育及思想品德，文化，科学技术教育，组织开展有益的社会活动；\n')
        print('（4）关心爱护全体学生，尊重学生人格，促进学生的全面发展；\n')
        print('（5）制止有害于学生的活动，批评抵制有害于学生健康成长的现象；\n')
        print('（6）不断提高思想政治觉悟和教育教学业务水平。')
    def StudentFunctionAndDuty(self):
        print('有坚定正确的政治方向，热爱社会主义国家，拥护中国共产党的领导和社会主义制度，志存高远，坚定信念，勤奋学习，自强不息。')
    def get__majorName(self):
        return self.__majorName
    def get__address(self):
        return self.__address
    def get__number(self):
        return self.__number
class MajorinTranslation(MajorinEnglish):
    def __init__(self):
        self.__majorName='Translation'
        self.__address='Fifth teaching buildings'
        self.__number=376
    def get__majorName(self):
        return self.__majorName
    def get__address(self):
        return self.__address
    def get__number(self):
        return self.__number



teacher1=Teacher('张老师','TC211',29,'女','英语')
teacher1.teach()
teacher1.homework()
teacher1.test()
teacher1.answer_Q()
student1=Student('汪同学','SD212',20,'男')
student1.study()
student1.takeTest()
student1.finishHomework()


#ComputerScienceCollege.IS(120).teach()
college = ComputerScienceCollege()
profession = college.IS(120)
profession.teach()

my_ecnomic=Ecnomic('ad',10)
my_ecnomic.duty()
my_ecnomic.schn()

a=MajorinTranslation()
a.get__majorName()
a.StudentFunctionAndDuty()
