# Python入门学习总结

*py是我一直很想学习的一门语言，趁着这次机会，我有幸认真学习了一下py最基本的知识。这门时下非常火的语言，我终于也算有所涉猎。*

-----

1. py很多的语法都和c类似，所以后面总结主要是归纳一下和c不同的、新的语法知识。

2. | 语句、函数、方法       | 描述             |
   | -------------- | -------------- |
   | +、-、*、/、//、%   | 加、减、乘、除、地板除、求余 |
   | abs()          | 求x的绝对值         |
   | pow(x,y)       | 求x的y次幂         |
   | divmod(x,y)    | 求x除以y的商和余数     |
   | x.is_integer() | 判断x是否是整数       |

3. 布尔类型使用and、or、not。

4. 浮点数的处理：

   | round(x)      | 对x四舍五入取整   |
   | ------------- | ---------- |
   | math.floor(x) | 对x向负无穷方向取整 |
   | math.ceil(x)  | 对x向正无穷方向取整 |
   | int(x)        | 对x舍去小数取整   |

5. 导入decimal模块，提供固定的精度有我们选择的十进制数。

   ```python
   import decimal
   a = decimal.Decimal(50)
   b = decimal.Decimal("50.111")
   c = decimal.Decimal(50.111)
   print(a + b)#100.111
   print(a + c)#100.1109999999999971009856381
   ```

   * 定义了复数的实部和虚部分别是：a.real和a.imag。
   * 字符串可以是单、双、三引号。
   * 获取字符编码：`print(ord('a'));print(ord(u'中'))`

6. 字符串的常用方法：

   ```python
   s = 'appp+asd+asd'
   s.find('ap',0,5)#查找子字符串，若找到返回从0开始的下标值，若找不到返回-1。
   s.split('+')#将一个字符串分裂成多个字符串组成的列表。当不带参数时以空格进行分割，当带参数时，以该参数进行分割。
   '-'.join(s.split('+'))#可以将序列的元素以’xxx’连接在一起。
   ```

   字符串格式化：%d %s %f

   ```python
   var1 = 'Hello World!'
   var2 = 'Python Runoob'

   print(var1[0])#H
   print(var2[1:5])#ytho。截取的原则是取左不取右
   ```

7. 列表：最基本常用的数据结构之一。第一个索引是0。用逗号分隔的可以是不同数据类型的使用方括号括起来的形式。其余的包括截取等等方法同上。删除元素用del。
   序号

   | 序列   | 函数                                       |
   | ---- | ---------------------------------------- |
   | 1    | [cmp(list1, list2)](http://www.runoob.com/python/att-list-cmp.html)比较两个列表的元素 |
   | 2    | [len(list)](http://www.runoob.com/python/att-list-len.html)列表元素个数 |
   | 3    | [max(list)](http://www.runoob.com/python/att-list-max.html)返回列表元素最大值 |
   | 4    | [min(list)](http://www.runoob.com/python/att-list-min.html)返回列表元素最小值 |
   | 5    | [list(seq)](http://www.runoob.com/python/att-list-list.html)将元组转换为列表 |

   | 序号   | 方法                                       |
   | :--- | ---------------------------------------- |
   | 1    | [list.append(obj)](http://www.runoob.com/python/att-list-append.html)在列表末尾添加新的对象 |
   | 2    | [list.count(obj)](http://www.runoob.com/python/att-list-count.html)统计某个元素在列表中出现的次数 |
   | 3    | [list.extend(seq)](http://www.runoob.com/python/att-list-extend.html)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
   | 4    | [list.index(obj)](http://www.runoob.com/python/att-list-index.html)从列表中找出某个值第一个匹配项的索引位置 |
   | 5    | [list.insert(index, obj)](http://www.runoob.com/python/att-list-insert.html)将对象插入列表 |
   | 6    | [list.pop([index=-1\])](http://www.runoob.com/python/att-list-pop.html)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
   | 7    | [list.remove(obj)](http://www.runoob.com/python/att-list-remove.html)移除列表中某个值的第一个匹配项 |
   | 8    | [list.reverse()](http://www.runoob.com/python/att-list-reverse.html)反向列表中元素 |
   | 9    | [list.sort(cmp=None, key=None, reverse=False)](http://www.runoob.com/python/att-list-sort.html)对原列表进行排序 |

8. 元组：元素不能修改，用小括号包括。其余同列表。修改元组非法，只能拼接新的元祖。删除元组非法，只能del整个元组。
   序号

   | 序号   | 方法及描述                                    |
   | ---- | ---------------------------------------- |
   | 1    | [cmp(tuple1, tuple2)](http://www.runoob.com/python/att-tuple-cmp.html)比较两个元组元素。 |
   | 2    | [len(tuple)](http://www.runoob.com/python/att-tuple-len.html)计算元组元素个数。 |
   | 3    | [max(tuple)](http://www.runoob.com/python/att-tuple-max.html)返回元组中元素最大值。 |
   | 4    | [min(tuple)](http://www.runoob.com/python/att-tuple-min.html)返回元组中元素最小值。 |
   | 5    | [tuple(seq)](http://www.runoob.com/python/att-tuple-tuple.html)将列表转换为元组。 |

9. 字典：采用键值对的方式，key=>value。用逗号隔开，字典用大括号包括。同一个键只出现一次，如出现两次，后一次覆盖前一次。键必须是不可变的数据结构，可以是数字，字符串或元组，不可以是列表。
   序号

   | 序号   | 函数及描述                                    |
   | ---- | ---------------------------------------- |
   | 1    | [cmp(dict1, dict2)](http://www.runoob.com/python/att-dictionary-cmp.html)比较两个字典元素。 |
   | 2    | [len(dict)](http://www.runoob.com/python/att-dictionary-len.html)计算字典元素个数，即键的总数。 |
   | 3    | [str(dict)](http://www.runoob.com/python/att-dictionary-str.html)输出字典可打印的字符串表示。 |
   | 4    | [type(variable)](http://www.runoob.com/python/att-dictionary-type.html)返回输入的变量类型，如果变量是字典就返回字典类型。 |

   | 序号   | 函数及描述                                    |
   | ---- | ---------------------------------------- |
   | 1    | [dict.clear()](http://www.runoob.com/python/att-dictionary-clear.html)删除字典内所有元素 |
   | 2    | [dict.copy()](http://www.runoob.com/python/att-dictionary-copy.html)返回一个字典的浅复制 |
   | 3    | [dict.fromkeys(seq[, val\])](http://www.runoob.com/python/att-dictionary-fromkeys.html)创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
   | 4    | [dict.get(key, default=None)](http://www.runoob.com/python/att-dictionary-get.html)返回指定键的值，如果值不在字典中返回default值 |
   | 5    | [dict.has_key(key)](http://www.runoob.com/python/att-dictionary-has_key.html)如果键在字典dict里返回true，否则返回false |
   | 6    | [dict.items()](http://www.runoob.com/python/att-dictionary-items.html)以列表返回可遍历的(键, 值) 元组数组 |
   | 7    | [dict.keys()](http://www.runoob.com/python/att-dictionary-keys.html)以列表返回一个字典所有的键 |
   | 8    | [dict.setdefault(key, default=None)](http://www.runoob.com/python/att-dictionary-setdefault.html)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
   | 9    | [dict.update(dict2)](http://www.runoob.com/python/att-dictionary-update.html)把字典dict2的键/值对更新到dict里 |
   | 10   | [dict.values()](http://www.runoob.com/python/att-dictionary-values.html)以列表返回字典中的所有值 |
   | 11   | [pop(key[,default\])](http://www.runoob.com/python/python-att-dictionary-pop.html)删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
   | 12   | [popitem()](http://www.runoob.com/python/python-att-dictionary-popitem.html)随机返回并删除字典中的一对键和值。 |

10. 集合：无序不重复元素的序列。可以用{}或set()函数创建。创建空集合必须使用set()而不是{}。
    集合和数学上的集合概念类似，

    ```python
    a = set('abracadabra')
    b = set('alacazam')
    a                                  
    #{'a', 'r', 'b', 'c', 'd'}
    a - b                              # 集合a中包含元素
    #{'r', 'd', 'b'}
    a | b                              # 集合a或b中包含的所有元素
    #{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    a & b                              # 集合a和b中都包含了的元素
    #{'a', 'c'}
    a ^ b                              # 不同时包含于a和b的元素
    #{'r', 'd', 'b', 'm', 'z', 'l'}
    ```

    添加元素s.add(x)、s.update(x)。两者都是如果元素存在，就不操作。
    移除元素x.remove(x)、s.discard(x)。前者在元素不存在是会报错，后者不会。随机删除：s.pop()。
    s.update({"字符串"})将字符串添加到集合中；s.update("字符串")将字符串拆分成单个字符再添加。

    ```python
    my_set = set(('al',))#{'al'}
    my_set = set('al')#{'a','l'}
    my_set = set(('al'))#{'a','l'}
    ```

11. 迭代器：一个可以记住遍历的位置的对象，只能往前不能后退。字符串、列表和元组对象可以创建迭代器。
    两个基本方法：iter(),next()。iter()创建迭代器对象，next()指迭代器下一个元素。
    生成器(generator)：跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。调用一个生成器函数，返回的是一个迭代器对象。

12. 时间：

    ```python
    import time
     
    # 格式化成2016-03-20 11:45:39形式
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #2018-07-16 10:37:53
     
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) #Mon Jul 16 10:37:53 2018
      
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))#1459175064.0
    ```

    日历：

    ```python
    import calendar

    cal = calendar.month(2018,7)
    print(cal)
    #     July 2018
    #Mo Tu We Th Fr Sa Su
    #                   1
    # 2  3  4  5  6  7  8
    # 9 10 11 12 13 14 15
    #16 17 18 19 20 21 22
    #23 24 25 26 27 28 29
    #30 31
    ```

    ```python
    import datetime

    i = datetime.datetime.now()
    print ("当前的日期和时间是 %s" % i)
    print ("ISO格式的日期和时间是 %s" % i.isoformat() )
    print ("当前的年份是 %s" %i.year)
    print ("当前的月份是 %s" %i.month)
    print ("当前的日期是  %s" %i.day)
    print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
    print ("当前小时是 %s" %i.hour)
    print ("当前分钟是 %s" %i.minute)
    print ("当前秒是  %s" %i.second)

    #当前的日期和时间是 2018-07-16 10:42:59.898981
    #ISO格式的日期和时间是 2018-07-16T10:42:59.898981
    #当前的年份是 2018
    #当前的月份是 7
    #当前的日期是  16
    #dd/mm/yyyy 格式是  16/7/2018
    #当前小时是 10
    #当前分钟是 42
    #当前秒是  59
    ```

13. 函数：以def关键字开头。实例：

    ```python
    def SayLove(str):
        print("I love ",str)
        return

    ```

14. **注意点：** 

    * python中，字符串、元组、数字是不可更改的对象。列表和字典是可更改的对象。
    * 函数的参数和js类似，可以是关键字参数、缺省参数。不定长参数时，最后面加*号的变量名存放所有未命名的变量参数。
    * 匿名函数：不同js匿名函数复杂的知识，py中匿名函数用lambda创建，只是一个表达式，函数体很简单，如：`sum = lambda arg1,arg2: arg1 + arg2; `

15. * Module:模块是一个以.py后缀名结尾的Python文件，包含了Python对象定义和语句。

    * 可以用import语句导入模块：`import module1[,module2[,...moduleN]]`，引用：模块名.函数名

    * 一个模块只会被导入一次。

    * from...import语句：从模块中导入制定的部分，语法如：`from modname import name1[,name2[,...nameN]]`，导入模块的全部内容到当前的命名空间：`from modname import *`

    * 搜索路径：当导入一个模块，Python 解析器对模块位置的搜索顺序是：

      - 1、当前目录
      - 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
      - 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

      模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

16. * 命名空间和作用域和其他语言基本相似，但是，如果想在函数内给全局变量赋值，使用global语句，`global VarName`告诉Python，VarName是一个全局变量，这样Python 就不会在局部命名空间里寻找这个变量了。
    * dir()函数的内容是一个模块里定义过的模块、变量、函数名，字符串列表。

17. Python的包。包下面必须存在`__init__.py`文件。

18. 读取键盘输入时，可以raw_input和input。前者读取一行，并且返回字符串。后者可以接受键入的是一个Python表达式。

-----

剩下的py较高阶的用法，比如面向对象等等后面再总结，有点累。告辞！