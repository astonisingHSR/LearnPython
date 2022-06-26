#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 21:34
# @Author : HongShaoRou
# @Site : 
# @File : demo_schedule.py
# @Software: PyCharm

import schedule
import time


def job():
    print('Haha -------')


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

