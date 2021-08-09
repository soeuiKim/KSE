# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:15:58 2021

@author: user12
"""

# 데이터 시각화

import matplotlib.pyplot as plt
import numpy as np

'''
mydata = [100,120,130,145,165,180]

plt.plot(mydata) # y축 데이터
'''
'''
Format String
Markers : . o v ^ < >
line : - -- -. :
color : b g r c m y k w
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro-.')
plt.ylabel('number') # y축 제목
plt.xlabel('ee')
plt.axis([0,6,0,20]) # [xmin, xmax, ymin, ymax]

plt.show() # 그리기 작업의 마지막 코드