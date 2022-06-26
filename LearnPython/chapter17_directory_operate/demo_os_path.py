#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/25 15:43
# @Author : HongShaoRou
# @Site : 
# @File : demo_os_path.py
# @Software: PyCharm

# os.path模块的
"""
    函 数                        说  明
abspath(path)           用于获取文件或目录的绝对路径
exists(path)            用于判断文件或目录是否存在，如果存在返回True，否则返回False
join(path, name)        将目录与目录或者文件名拼接起来
splitext()              分离文件名和扩展名
basename(path)          从一个目录中提取文件名
dirname(path)           从一个路径中提取文件路径，不包括文件名
isdir(path)             用于判断是否为路径
"""

import os.path as path
print(path.abspath("demo_os_module.py"))
print(path.exists('demo_os_path.py'), path.exists('demo11.py'))
print(path.join('D:\\Python', 'demo13.py'))
print(path.split('D:\\AICode\\LearnPython\\chapter17_directory_operate\\demo_os_module.py'))
print(path.splitext('demo_os_module.py'))
print(path.basename('D:\\AICode\\LearnPython\\chapter17_directory_operate\\demo_os_module.py'))
print(path.dirname('D:\\AICode\\LearnPython\\chapter17_directory_operate\\demo_os_module.py'))
print(path.isdir('D:\\AICode\\LearnPython\\chapter17_directory_operate\\demo_os_module.py'))
