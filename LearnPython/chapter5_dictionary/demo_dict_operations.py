#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 19:42
# @Author : HongShaoRou
# @Site : 
# @File : demo_dict_operations.py
# @Software: PyCharm

# 字典的操作
"""
字典中元素的获取：
    []取值：字典名[key]
    get()取值：字典名.get(key)
区别：
    []：如果字典中不存在指定的key，抛出keyError异常
    get()：如果字典中不存在指定的key，不会抛出keyError异常，而是返回None，
        可以通过参数设置默认的value,以便指定key不存在时返回
"""
scores = {'张三': 100, '李四': 95, '王五': 76}
print(scores)

# []取值
print(scores['李四'])
# print(scores['赵六'])  # 抛出KeyError

# get()取值
print(scores.get('李四'))
print(scores.get('赵六'))  # None
print(scores.get('李二', 99))  # 若key不存在，返回99

"""
字典的常用操作：
    key的判断：in, not in
    字典元素的删除： del 字典名[key]
    字典元素的新增： 字典名[new_key] = new_value
"""
print('张三' in scores)  # True
print('张三' not in scores)  # False

# 删除元素
print('删除元素前：', scores)
del scores['张三']
print('删除元素后：', scores)

# 清空字典
scores.clear()
print('字典清空后：', scores)

# 添加元素
scores['赵六'] = 83
print('添加元素后：', scores)

# 修改元素
scores['赵六'] = 60
print('修改后', scores)


