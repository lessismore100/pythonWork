#coding:utf-8
__author__ = 'jason'
#从日志文件中提取指定字符开始之后的内容，然后写入新文件
import re
import os,shutil,string,time
from fileutil import FileUtil
path = "D:\\techworkspace\\python\\domainHandler\\"
fp = open(path + 'parent-cn.txt', 'r', encoding="utf-8")
print('start!')
while 1:
    line = fp.readline()
    if not line:
        fp.close()
        break
    s = line.find('\"')
    if s > -1:
        result = line[s:]

        # write content
        fileUtil = FileUtil(path, result)# 这里每次都创建？有没有其他传参方式？
        fileUtil.write_content()
    # else:
    #     print('not found --> ' + line)
print('completed!')
