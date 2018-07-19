# Python进阶学习



# os 模块
os.sep    可以取代操作系统特定的路径分隔符。windows下为 '\\'
os.name    字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是 'posix'
os.getcwd()    函数得到当前工作目录，即当前Python脚本工作的目录路径
os.getenv()    获取一个环境变量，如果没有返回none
os.putenv(key, value)    设置一个环境变量值
os.listdir(path)    返回指定目录下的所有文件和目录名
os.remove(path)    函数用来删除一个文件
os.system(command)    函数用来运行shell命令
os.linesep    字符串给出当前平台使用的行终止符。例如，Windows使用 '\r\n'，Linux使用 '\n' 而Mac使用 '\r'
os.path.split(path)        函数返回一个路径的目录名和文件名
os.path.isfile()    和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
os.path.exists()    函数用来检验给出的路径是否真地存在
os.curdir        返回当前目录 ('.')
os.mkdir(path)    创建一个目录
os.makedirs(path)    递归的创建目录
os.chdir(dirname)    改变工作目录到dirname          
os.path.getsize(name)    获得文件大小，如果name是目录返回0L
os.path.abspath(name)    获得绝对路径
os.path.normpath(path)    规范path字符串形式
os.path.splitext()        分离文件名与扩展名
os.path.join(path,name)    连接目录与文件名或目录
os.path.basename(path)    返回文件名
os.path.dirname(path)    返回文件路径
os.walk(top,topdown=True,onerror=None)        遍历迭代目录
os.rename(src, dst)        重命名file或者directory src到dst 如果dst是一个存在的directory, 将抛出OSError. 在Unix, 如果dst在存且是一个file, 如果用户有权限的话，它将被安静的替换. 操作将会失败在某些Unix 中如果src和dst在不同的文件系统中. 如果成功, 这命名操作将会是一个原子操作 (这是POSIX 需要). 在 Windows上, 如果dst已经存在, 将抛出OSError，即使它是一个文件. 在unix，Windows中有效。
os.renames(old, new)    递归重命名文件夹或者文件。像rename()

# shutil 模块
shutil.copyfile( src, dst)    从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)        移动文件或重命名
shutil.copymode( src, dst)    只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst)    复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)        复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)        在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)        如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase)
把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src )    递归删除一个目录以及目录内的所有内容





## 模块

一个标准的模块模板：

第1行和第2行是标准注释，第1行注释可以让这个`hello.py`文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用`__author__`变量把作者写进去

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'daluzi'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':#Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()
```

在py中，我们可以有大量的第三方模块资源供我们选择（或者我们自己写了传上社区。。。）

下面仅用到matplotlib、pil等一些处理图案的模块：

```python
def plotcos():
	import matplotlib.pyplot as plt
	import numpy as np
	x = np.linspace(0,2*np.pi,50)
	y = np.cos(x)
	plt.plot(x,y)
	plt.show()
plotcos()

# from PIL import Image
# im = Image.open(r'C:\Users\陈露\Pictures\Saved Pictures\西瓜.png')

# w,h = im.size
# print('image size: %sx%s'%(w,h))

# #缩放到50%
# im.thumbnail((w//2,h//2))
# print('image resize:%sx%s'%(w//2,h//2))

# im.save('thumbnail.png','jpeg')

# #模糊效果：
# from PIL import Image,ImageFilter
# im = Image.open(r'C:\Users\陈露\Pictures\Saved Pictures\西瓜.png')
# #应用模糊滤镜
# im2 = im.filter(ImageFilter.BLUR)
# im2.save(r'C:\Users\陈露\Pictures\Saved Pictures\blur.jpg','jpeg')


#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

#随机字母
def rndChar():
	return chr(random.randint(65,90))

#随机颜色1：
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2：
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font = ImageFont.truetype(r'C:\python\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmb10.ttf',36)
#创建Draw对象：
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
#输出文字：
for t in range(4):
	draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())

#模糊：
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')


import re
def is_valid_email(self,addr):
	re_email = re.compile(r'^(\w+)(\.w+)?(@\w+\.com)$')
	return re_email.match(addr)

```

读取文件时（千万注意读取或者写入都是针对文件，不是针对文件夹（或者叫目录））：

​	read()会一次性读取文件的全部内容;

​	read(size)读取size个字节

​	readline()读取一行的内容

​	readlines()读取完所有内容并按行返回list



### 正则表达式：

用`\d`可以匹配一个数字，`\w`可以匹配一个字母或数字，所以：

- `'00\d'`可以匹配`'007'`，但无法匹配`'00A'`；
- `'\d\d\d'`可以匹配`'010'`；
- `'\w\w\d'`可以匹配`'py3'`；

`.`可以匹配任意字符，所以：

- `'py.'`可以匹配`'pyc'`、`'pyo'`、`'py!'`等等。

用`*`表示任意个字符（包括0个），用`+`表示至少一个字符，用`?`表示0个或1个字符，用`{n}`表示n个字符，用`{n,m}`表示n-m个字符。

* `\d{3}`表示匹配3个数字，例如`'010'`；
* `\s`可以匹配一个空格（也包括Tab等空白符），所以`\s+`表示至少有一个空格，例如匹配`' '`，`' '`等；
* `\d{3,8}`表示3-8个数字，例如`'1234567'`。

要做更精确地匹配，可以用`[]`表示范围，比如：

- `[0-9a-zA-Z\_]`可以匹配一个数字、字母或者下划线；
- `[0-9a-zA-Z\_]+`可以匹配至少由一个数字、字母或者下划线组成的字符串，比如`'a100'`，`'0_Z'`，`'Py3000'`等等；
- `[a-zA-Z\_][0-9a-zA-Z\_]*`可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
- `[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}`更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

`A|B`可以匹配A或B，所以`(P|p)ython`可以匹配`'Python'`或者`'python'`。

`^`表示行的开头，`^\d`表示必须以数字开头。

`$`表示行的结束，`\d$`表示必须以数字结束。

你可能注意到了，`py`也可以匹配`'python'`，但是加上`^py$`就变成了整行匹配，就只能匹配`'py'`了。

在python中，re模块包含所有的正则表达式功能，re.match(r'^\d{3}\-\d{3,8}$', '010-12345')表示前面是匹配的规则，第二个参数是要匹配的字符串。match之后的分组可以用group()表示，group(0)永远表示原字符串。



### extend和append方法

list的两个方法的不同：

extend()方法接受的参数总是一个list，然后把list里面的每一个元素分别添加到原list上。

append()方法可以接受任意类型，并且只是单纯的追加到原list尾部。

list的一个方法：count()用于查找某元素出现的次数。