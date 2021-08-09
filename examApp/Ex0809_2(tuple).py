# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:43:15 2021

@author: user12
"""

# 튜플 응용
# 리스트와 유사하나 생성후에 수정 불가능(_상품가격등 변동이없는 자료이용)

tscore = (88,76,55,90,83)
print(tscore)
print(tscore[2:4])

# lvalue = rvalue(복합구조)
tu = ("빅데이터",'프로그래밍')
var1, var2 = tu   # 2개 이상의 변수에 저장 가능
print(var1,var2)

val1, _ = tu # _ 사용하지 않는 값 표시
print(val1)
