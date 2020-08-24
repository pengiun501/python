# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:13:54 2020

@author: Alice
"""

性別你=str(input('你是男生還是女生?(填男生/女生)'))
性別我=str(input('我是男生還是女生?(填男生/女生)'))
愛我=str(input('你喜歡我嗎?(填喜歡/不喜歡)'))
愛你=str(input('我喜歡你嗎?(填喜歡/不喜歡)'))
if 性別你=='男生' and 性別我=='女生' and 愛我=='喜歡' and 愛你=='喜歡':
    print('我們結婚吧!')
elif 性別你=='女生' and 性別我=='男生' and 愛我=='喜歡' and 愛你=='喜歡':
    print('我們結婚吧!')
else:
    print('哼!不跟你結婚了!掰掰!')