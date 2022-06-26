#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 20:52
# @Author : HongShaoRou
# @Site : 
# @File : demo_software_package.py
# @Software: PyCharm

# python中的包
"""
定义：
    包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
作用：
    代码规范
    避免模块名称冲突
包与目录的区别：
    包含__init__.py文件的目录称为包
    目录里通常不包含__init__.py文件
包的导入：
    import 包名.模块名
"""

import myPackage.module_A as m_A
print(m_A.a)
