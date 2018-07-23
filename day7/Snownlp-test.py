from snownlp import SnowNLP
import xlrd
import jieba

def open_excel(file= '京东商品卫龙评论.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excel_table_byname(file= u'京东商品卫龙评论.xlsx',colnameindex=0,by_name=u'Sheet1'):#修改自己路径
     data = open_excel(file)
     table = data.sheet_by_name(by_name) #获得表格
     nrows = table.nrows  # 拿到总共行数
     colnames = table.row_values(colnameindex)  # 某一行数据 ['姓名', '用户名', '联系方式', '密码']
     list = []
     for rownum in range(1, nrows): #也就是从Excel第二行开始，第一行表头不算
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                 app[colnames[i]] = row[i] #表头与数据对应
             list.append(app)
     return list

def main():
    tables = excel_table_byname()
    for row in tables:
    	# print(row['评价内容'])
    	r.append(row['评价内容'])
    	# print(r)
    file_name = open('restxtweilong.txt','w',encoding='utf-8')
    file_name.writelines(r)
    file_name.close()

if __name__ =="__main__":
	r = []
	main()
	p = []
	with open('restxtweilong.txt','r',encoding='utf-8') as f:
		for fline in f.readline():
			# print(fline)
			textjd = SnowNLP(fline)
			# print(textjd.sentences,textjd.sentiments)
			p.append(textjd.sentiments)
	print(p)
	jieba.load_userdict("user.dict")
	stop_words = ''
	with open("stopword.dict",encoding='utf-8') as f:
		stop_words = f.read().split('\n')
	# print(stop_words)
	words_jieba = jieba.cut()