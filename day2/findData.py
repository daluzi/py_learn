import re

p1 = re.compile(r"Windows NT|Mac OS|Linux|GoogleMaps")
p2 = re.compile(r'"a".*?,')
p3 = re.compile(r'"c".*?,')
def search1(file):
	ctn = []
	with open(file,'r') as f:
		for fr in f.readlines():
			p = p1.findall(fr)
			ctn.extend(p)
			pass
	# print(ctn)
	return ctn

def search2(file):
	net = []
	with open(file,'r') as f:
		for fr in f.readlines():
			n = p2.findall(fr)
			net.extend(n)
			# print(n)
			pass
	# print(net)
	return net

def search3(file):
	country = []
	with open(file,'r') as f:
		for fr in f.readlines():
			n = p3.findall(fr)
			country.extend(n)
			# print(n)
			pass
	# print(net)
	return country


if __name__ == "__main__":
	file = r'F:\py学习\file1.txt'
	ctn = search1(file)
	net = search2(file)
	country = search3(file)
	WindowsNT = ctn.count("Windows NT")
	MacOS = ctn.count("Mac OS")
	Linux = ctn.count("Linux")
	GoogleMaps = ctn.count("GoogleMaps")
	print("WindowsNT出现的次数：%d,MacOS出现的次数：%d,Linux出现的次数：%d,GoogleMaps出现的次数：%d"%(WindowsNT,MacOS,Linux,GoogleMaps))
	for a in net:
		pass
		print("浏览器访问头%s"%a)
	for cty in country:
		pass
		print("国家%s"%cty)
