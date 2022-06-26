#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 20:42
# @Author : HongShaoRou
# @Site : 
# @File : cal.py
# @Software: PyCharm

# 自定义模块
def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':  # 只有从cal运行时才会执行下面的代码
    print(add(10, 20))
