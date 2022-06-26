#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 21:51
# @Author : HongShaoRou
# @Site : 
# @File : demo_file_read_write.py
# @Software: PyCharm

# 编码格式
"""
常见的字符编码格式
    python的解释器使用的是unicode(内存)
    .py文件在磁盘上使用UTF-8存储(外存)
"""

# 文件的读写原理
"""
文件的读写俗称'IO'操作
文件读写操作流程：
    python操作文件-->打开或新建文件-->读、写文件-->关闭资源
操作原理
"""

# 文件的读写操作
"""
内置函数open()创建文件对象
语法规则：
    文件对象名 = open(文件名, (mode(打开模式), encoding(编码格式)))
文件的类型：
    文本文件：存储的是普通'字符'文本，默认为unicode字符集，可以使用记事本程序打开
    二进制文件：把数据内容用'字节'进行存储，无法用记事本打开，必须使用专用的软件打开
文件打开模式：
模式                  描  述
r           以只读模式打开文件，文件的指针将会放在文件的开头
w           以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
a           以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
b           以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb或wb
+           以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
"""

fp1 = open('readFile.txt', mode='r', encoding='utf-8')
print(fp1.readlines())
fp1.close()

fp2 = open('writeFile.txt', mode='w', encoding='utf-8')
fp2.write('Python')
fp2.close()

fp3 = open('writeFile.txt', mode='a', encoding='utf-8')
fp3.write('Python')
fp3.close()

src_file = open('state.png', 'rb')

tar_file = open('copystate.png', 'wb')
tar_file.write(src_file.read())
src_file.close()
tar_file.close()

