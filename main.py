#!/usr/bin/env python3
#coding:utf-8
import datetime
import random
import sys
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()


now = datetime.datetime.now().strftime('今天是：%Y年%m月%d日      现在时刻：%H:%M:%S')
print("杨熙玥你好! 欢迎进入数学学习系统! " )
print(now,end='\n')
num = int(input("你今天想做几道题?: "))

while num.isdigit():
    break

while num <= 0 :
    if num == 0 :
        sys.exit()
    else:
        num = int(input("输入错误，请重新输入！"))

cw = 0#错误数
sn = 1#题号

while sn <= num:
    print ('')
    a = random.randint(0,20)
    b = random.randint(0,20)
    print ("第%d题: %d + %d = " %(sn,a,b),end='')
    c = int(input())

    while c != a+b:
        c = int(input("计算错误，请仔细检查!"))
        cw+=1

    sn+=1

print ("您今天做了%d道题，计算错误%d次，得%d分。加油哦！"%\
       (num, cw, (100-100*cw/num)))
