#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/25 15:12
# @Author : HongShaoRou
# @Site : 
# @File : demo_os_module.py
# @Software: PyCharm

# 目录操作
"""
os模块：
    os模块是python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，
    在不同的操作系统上运行，得到的结果可能不一样
    os模块与os.path模块用于对目录和文件进行操作
"""

import os
import shutil

# os.system('notepad.exe')
# os.system('calc.exe')

# 直接调用可执行文件
# os.startfile('D:\\软件\\WeChat\\WeChat.exe')

"""
os模块操作目录相关函数：
    函  数                                    说   明
getcwd()                                返回当前的工作目录
listdir(path)                           返回指令路径下的文件和目录信息
mkdir(path[,mode])                      创建目录
makedirs(path1/path2,...[,mode])        创建多级目录
remdir(path)                            删除目录
removedirs(path1/path2,...)             删除多级目录
chdir(path)                             将path设置为当前工作目录
"""

print(os.getcwd())
lst = os.listdir('../chapter16_file_operate')
print(lst)
# os.mkdir('newdir')
# os.makedirs('A/B/C')
# os.remove('newdir')   # 会报错，没有权限,要用rmdir()
# os.rmdir('A')  # 不能删除非空目录
# os.rmdir('newdir')
# shutil.rmtree('A')

