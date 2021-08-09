# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:58:06 2021

@author: user12
"""

# Dictionary (딕셔너리)  {}사용
# key 와 value 조합

fruit = {'사과' : 1000, '배' : 2000, '포도' : 1500} # 3개원소
print(fruit)
print(fruit['사과'])  # key를 입력하여 value를 반환

print('복숭아' in fruit.keys()) # 지정키 존재 여부 반환
print(1000 in fruit.values()) # 지정값 존재 여부 

for k, v in fruit.items() : 
    print(k,v)