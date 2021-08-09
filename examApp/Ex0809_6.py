#  그래프

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0) # 균일 간격 점생성
x2 = np.linspace(0.0, 2.0) # 720도

#  np.pi = 3.14....(파이값)
y1 = np.cos(2 * np.pi * x1) * np.exp(- x1) # damping
y2 = np.cos(2 * np.pi * x2) # cos 그래프    

plt.subplot(2, 1, 1)
plt.plot(x1, y1,'.-')



plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'b-')



plt.show()