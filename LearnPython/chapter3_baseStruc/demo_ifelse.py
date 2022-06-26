#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 16:14
# @Author : HongShaoRou
# @Site : 
# @File : demo_assignment.py
# @Software: PyCharm

# if-else结构

money = 1000  # 余额
s = int(input('请输入取款金额：'))  # 获取取款金额
# 判断余额是否充足
if s<=money:
    money -= s
    print('取款成功,剩余余额为：', money)
else:
    print('余额不足！剩余余额为：', money)

score = int(input('请输入得分：'))
if score < 0 or score > 100:
    print('请输入正确的分数！')
elif 100 < score < 90:
    print('优秀！')
elif score > 80:
    print('良好！')
elif score > 70:
    print('及格！')
else:
    print('不及格')
