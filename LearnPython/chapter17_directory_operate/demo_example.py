#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/25 15:53
# @Author : HongShaoRou
# @Site : 
# @File : demo_example.py
# @Software: PyCharm

# 列出指定目录下的所有.py文件

import os

path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

# 递归获取指定目录下所有.py文件
print('===================================')
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('--------------------------------')
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    print('-----------------------------------')
    for file in filename:
        print(os.path.join(dirpath, file))
    print('------------------------------------')


