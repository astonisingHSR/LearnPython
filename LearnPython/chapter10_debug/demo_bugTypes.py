#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 20:16
# @Author : HongShaoRou
# @Site : 
# @File : demo_bugTypes.py
# @Software: PyCharm

# bug的常见类型

# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print('成年人需要负法律责任了')

lst = [{'rating': [9.7, 50], 'id': '1292052', 'type': ['犯罪', '激情'], 'title': '肖申克的救赎', 'actors': ['蒂姆.罗宾斯', '摩根.弗里曼']},
       {'rating': [9.6, 50], 'id': '1291546', 'type': ['剧情', '爱情', '同性'], 'title': '霸王别姬', 'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
       {'rating': [9.6, 50], 'id': '1296141', 'type': ['剧情', '犯罪', '悬疑'], 'title': '控方证人', 'actors': ['泰隆.鲍华', '玛琳.黛德丽']}]

name = input('请输入要查询的演员姓名:')
d_flag = True
for item in lst:
    if name in item['actors']:
        print(name, '出演了', item['title'])
        d_flag = False

if d_flag:
    print('没有查询到', name, '出演的电影')

