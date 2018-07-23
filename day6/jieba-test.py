#coding='utf-8'impo#coding='utf-8'
import csv
import jieba
import pandas as pd

file_object2=open('a.csv',encoding='utf-8').read().split('\n')  #一行行的读取内容
Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    result=[]
    seg_list = jieba.cut(file_object2[i])
    for w in seg_list :#读取每一行分词
        result.append(w)
    Rs2.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
file=open('result2.csv','w')
writer = csv.writer(file)#定义写入格式
writer.writerows(Rs2)#按行写入
#file.write(str(Rs))
file.close() 
