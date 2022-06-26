#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 20:37
# @Author : HongShaoRou
# @Site : 
# @File : demo_main.py
# @Software: PyCharm

# 以主程序形式运行
"""
在每个模块的定义中都包括一个记录模块名称的变量__name__，程序可以检查该变量，以确定他们在哪个模块中执行。
如果一个模块不是被导入到其他程序中执行，那么它可能在解释器的顶级模块中执行。顶级模块的__name__变量的值为__main__

if __name__ = '__main__':
    pass
"""

import cal
print(cal.add(100, 20))



