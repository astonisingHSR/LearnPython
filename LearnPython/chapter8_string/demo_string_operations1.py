#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 14:52
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_operations1.py
# @Software: PyCharm

# 字符串的常用操作
"""
查询操作：
    index()；查找子串substr第一次出现的位置，如果不存在，则抛出ValueError
    rindex()；查找子串substr最后一次出现的位置，如果不存在，则抛出ValueError
    find()；查找子串substr第一次出现的位置，如果不存在，则返回-1
    rfind()；查找子串substr最后一次出现的位置，如果不存在，则返回-1
"""

myStr = 'hello,hello'
print(myStr.index('lo'))  # 3
print(myStr.find('lo'))

print(myStr.rindex('lo'))  # 9
print(myStr.rfind('lo'))

# print(myStr.index('k'))  # 抛出异常
print(myStr.find('k'))


"""
字符串的大小写转换操作：
    upper():把字符串中所有字符都转成大写字母
    lower():把字符串中所有字符都转成小写字母
    swapcase():把字符串中所有大写字母都转成小写字母，所有小写字母都转成大写字母
    capitalize():把第一个字符转换为大写，其余字符转换为小写字母
    title():把每个单词的第一个字符转换为大写，每个单词剩余字符转换为小写
"""

myStr = 'hello,world'
myStr1 = myStr.upper()   # 转成大写后会产生一个新的字符串
print(myStr, id(myStr))
print(myStr1, id(myStr1))

myStr2 = myStr.lower()
print(myStr is myStr2)  # 即使未发生改变，依然产生了一个新的字符串

myStr = 'Hello,WORLD'
myStr1 = myStr.swapcase()  # 大小写互换
print(myStr1)

myStr1 = myStr.capitalize()
print(myStr1)

myStr1 = myStr.title()  # 单词第一个字符大写
print(myStr1)


"""
字符串内容对齐操作的方法：
    center():居中对齐，
        第1个参数指定宽度；如果指定宽度小于实际宽度，则返回原字符串
        第2个参数指定填充符，可省略，默认为空格
    ljust():左对齐，
        第1个参数指定宽度；如果指定宽度小于实际宽度，则返回原字符串
        第2个参数指定填充符，可省略，默认为空格
    rjust():右对齐
        第1个参数指定宽度；如果指定宽度小于实际宽度，则返回原字符串
        第2个参数指定填充符，可省略，默认为空格
    zfill():右对齐，左边用0填充。
        只接受一个参数，用于指定字符串宽度，如果指定宽度小于实际宽度，则返回原字符串
"""

s1 = 'hello,World'
print(s1.center(20, '*'))
print(s1.ljust(20, '*'))
print(s1.rjust(20))
print(s1.zfill(20))

print('-8910'.zfill(10))  # 0填充到负号后面
