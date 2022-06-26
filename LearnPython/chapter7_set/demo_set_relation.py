#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 12:21
# @Author : HongShaoRou
# @Site : 
# @File : demo_set_relation.py
# @Software: PyCharm

# 集合之间的关系
"""
两个集合是否相等：
    使用运算符 == 或者 != 判断
一个集合是否是另一个集合的子集：
    调用方法issubset()进行判断
    B是A的子集
一个集合是否是另一个集合的超集：
    调用方法issuperset()进行判断
    A是B的超集
两个集合是否存在交集：
    调用方法isdisjoint()进行判断
"""
# 两个集合是否相等
A = {10, 20, 30, 40}
B = {30, 40, 20, 10}

print(A == B)  # True
print(A != B)  # False

# 一个集合是否是另一个集合的子集
A = {10, 20, 30, 40, 50, 60}
B = {30, 40, 20, 10}
C = {10, 20, 90}
D = {0, 1, 2}
print(B.issubset(A))  # True
print(C.issubset(A))  # False

# 一个集合是否是另一个集合的超集
print(A.issuperset(B))  # True
print(A.issuperset(C))  # False

# 两个集合是否存在交集
print(A.isdisjoint(B))  # False表示有交集
print(A.isdisjoint(C))  # False表示有交集
print(A.isdisjoint(D))  # True表示无交集


