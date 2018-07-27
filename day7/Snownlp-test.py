from snownlp import SnowNLP
import xlrd
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

font = r'F:\py学习\text-py\day6\msyh.ttf'
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
	# print(p)
	#分词
	jieba.load_userdict("user.dict")
	stop_words = ''
	with open("stopword.dict",encoding='utf-8') as f:
		stop_words = f.read().split('\n')
	# print(stop_words)
	file_name1 = 'restxtweilong.txt'
	data = []
	for line in open(file_name1,encoding='utf-8'):
		line = line.split()
		data.append(line)
	# text = open('restxtweilong.txt',encoding='utf-8')
	words_jieba = jieba.cut(data,cut_all=False)
	# words_cut = "".join(words_jieba)
	#词云
	words_uni = [x for x in words_jieba if x not in stop_words]
	words_cut2 = "".join(words_uni)
	words_wordcloud = WordCloud(font_path = font).generate(words_cut2)
	plt.imshow(words_wordcloud)
	plt.show()