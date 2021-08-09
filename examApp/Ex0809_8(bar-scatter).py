# 막대그래프(bar), 산점도(scatter plot)

import matplotlib.pyplot as plt
import numpy as np

names = ['group_a','group_b','group_c']
values = [1,10,100]

plt.figure(figsize=(9,3)) # 가로세로 9인치, 3인치
plt.subplot(1, 3, 1) # 1행 3열의 첫번째
plt.bar(names, values) # 세로막대 그래프

plt.subplot(1, 3, 2)
plt.scatter(names, values) # 산점도

plt.subplot(1, 3, 3)
plt.plot(names, values)


plt.show()
