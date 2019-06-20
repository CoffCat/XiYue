#!/usr/bin/env python3
#coding:utf-8
import datetime
import random
import sys

now = datetime.datetime.now().strftime('今天是：%Y年%m月%d日 现在时刻：%H:%M:%S')
print("杨熙玥你好! 欢迎进入数学学习系统! "+ now)
num = int(input("你今天想做几道题?: "))

while num <= 0 :
    if num == 0 :
        sys.exit()
    else:
        num = int(input("输入错误，请重新输入！"))

zq = 0#正确数
cw = 0#错误数
sn = 1#题号

while sn <= num:
    print ('')
    a = random.randint(0,20)
    b = random.randint(0,20)
    print ("第%d题: %d + %d = ?" %(sn,a,b))
    c = int(input())
    if c == a+b:
        print("计算正确!")
        zq+=1
    else:
        print("计算错误!")
        cw+=1
    sn+=1
print ("您今天做了%d道题，正确%d道，错误%d道，得%d分。加油哦！"%(num, zq, cw, round(100*zq/num)))
