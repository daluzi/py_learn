# #coding = utf-8

import os 
 
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if os.path.isfile(child):
            readFile(child)
            continue
        eachFile(child)
   
# 遍历
def readFile(filenames):
        fopen = open(filenames, 'r',encoding='utf-8')
        fileread = fopen.read()
        print(os.path.join(r'F:\testdir\w',os.path.basename(filenames)))
        fopen.close()
        with open(os.path.join(r'F:\testdir\w',os.path.basename(filenames)),'w',encoding='utf-8',errors='ignore') as f:
        	f.write(fileread)      
 
if __name__ == "__main__":
    filenames = r'F:\py学习\t' 
    eachFile(filenames)