#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 12:10
# @Author : HongShaoRou
# @Site : 
# @File : demo_set_operations.py
# @Software: PyCharm

# 集合的相关操作

# 判断元素是否在集合中
mySet = {10, 20, 30, 405, 60}
print(10 in mySet)  # True
print(100 in mySet)  # False
print(100 not in mySet)  #False

# 集合元素的新增操作
"""
使用add()方法，一次添加一个元素
使用update()方法，至少添加一个元素
"""
# 使用add()方法
print(id(mySet))
mySet.add(50)
print(mySet, id(mySet))

# 使用update()方法
mySet.update({100, 200, 300})  # 使用集合
print(mySet, id(mySet))

mySet.update([101, 11, 22])   # 使用列表
print(mySet, id(mySet))

mySet.update((101, 111, 202))   # 使用元组
print(mySet, id(mySet))

mySet.update(range(0, 5))
print(mySet, id(mySet))

# 集合元素的删除操作
"""
remove()方法：一次删除一个指定元素，如果指定元素不存在抛出KeyError
discard()方法：一次删除一个指定元素，如果指定元素不存在不抛出异常
pop()方法：一次删除一个任意元素
clear()方法：清空集合所有元素
"""

mySet.remove(10)
print(mySet)
# mySet.remove(500)  # 抛出异常
mySet.discard(500)  # 不会抛出异常
mySet.discard(0)
print(mySet)

mySet.pop()
mySet.pop()
print(mySet)

mySet.clear()
print(mySet)
