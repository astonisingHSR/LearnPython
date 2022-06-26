#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/20 21:51
# @Author : HongShaoRou
# @Site : 
# @File : demo_traceback.py
# @Software: PyCharm

# traceback模块的使用,打印异常信息

import traceback

try:
    print('-----------------')
    print(1/0)
except:
    traceback.print_exc()
