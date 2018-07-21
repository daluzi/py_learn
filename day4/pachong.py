from urllib.request import urlopen

#网页有中文，所以read之后一定要decode对文字进行转化。
html = urlopen(
	"https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)