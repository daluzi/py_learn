# def plotcos():
# 	import matplotlib.pyplot as plt
# 	import numpy as np
# 	x = np.linspace(0,2*np.pi,50)
# 	y = np.cos(x)
# 	plt.plot(x,y)
# 	plt.show()
# plotcos()

# # from PIL import Image
# # im = Image.open(r'C:\Users\陈露\Pictures\Saved Pictures\西瓜.png')

# # w,h = im.size
# # print('image size: %sx%s'%(w,h))

# # #缩放到50%
# # im.thumbnail((w//2,h//2))
# # print('image resize:%sx%s'%(w//2,h//2))

# # im.save('thumbnail.png','jpeg')

# # #模糊效果：
# # from PIL import Image,ImageFilter
# # im = Image.open(r'C:\Users\陈露\Pictures\Saved Pictures\西瓜.png')
# # #应用模糊滤镜
# # im2 = im.filter(ImageFilter.BLUR)
# # im2.save(r'C:\Users\陈露\Pictures\Saved Pictures\blur.jpg','jpeg')


# #PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
# from PIL import Image,ImageDraw,ImageFont,ImageFilter

# import random

# #随机字母
# def rndChar():
# 	return chr(random.randint(65,90))

# #随机颜色1：
# def rndColor():
# 	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# #随机颜色2：
# def rndColor2():
# 	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# width = 60 * 4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# #创建Font对象
# font = ImageFont.truetype(r'C:\python\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmb10.ttf',36)
# #创建Draw对象：
# draw = ImageDraw.Draw(image)
# #填充每个像素
# for x in range(width):
# 	for y in range(height):
# 		draw.point((x,y),fill=rndColor())
# #输出文字：
# for t in range(4):
# 	draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())

# #模糊：
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')


# import re
# def is_valid_email(self,addr):
# 	re_email = re.compile(r'^(\w+)(\.w+)?(@\w+\.com)$')
# 	return re_email.match(addr)


import os
import re
import json

p1 = re.compile("Windows NT|Mac OS|Linux|GoogleMaps")
def search(file):
	ctn = []
	with open(file,'r') as f:
		for fr in f.readlines():
			p = p1.findall(fr)
			ctn.extend(p)
			pass
	return ctn

def detaile(self,file):

	pass

if __name__ == "__main__":
	file = r'F:\py学习\file1.txt'
	ctn = search(file)
	WindowsNT = ctn.count("Windows NT")
	MacOS = ctn.count("Mac OS")
	Linux = ctn.count("Linux")
	GoogleMaps = ctn.count("GoogleMaps")
	print("WindowsNT出现的次数：%d,MacOS出现的次数：%d,Linux出现的次数：%d,GoogleMaps出现的次数：%d"%(WindowsNT,MacOS,Linux,GoogleMaps))