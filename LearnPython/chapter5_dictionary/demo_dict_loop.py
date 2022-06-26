#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 20:21
# @Author : HongShaoRou
# @Site : 
# @File : demo_dict_loop.py
# @Software: PyCharm

# 字典元素的遍历
"""
for 变量名 in 字典名
    操作
"""

scores = {'张三': 100, '李四': 95, '王五': 76}
print(scores)

for item in scores:
    print(item)  # 只输出key
    print(scores[item])  # 获取value
    print(scores.get(item))

